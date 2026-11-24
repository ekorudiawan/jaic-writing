#!/usr/bin/env python3
"""
Build a JAIC manuscript (.docx) on top of the official JAIC Paper Template 2027.

The template is used as-is (styles, embedded Cambria fonts, header/footer,
Article Info table, CC BY-SA badge, page setup). Only the text placeholders
are replaced and the body (INTRODUCTION ... REFERENCES) is regenerated.

Usage:
    python3 build_jaic_docx.py content.json output.docx [--template path.docx]

content.json schema (all strings may use light inline markup:
**bold**, *italic*, ^{superscript}, _{subscript}):

{
  "title": "Paper title (<= 10 words)",
  "running_title": "Short title for footer (optional, defaults to title)",
  "running_author": "Surname et al. (optional)",
  "authors": [{"name": "Eko Rudiawan Jamzuri", "affil": [1]}, ...],
  "affiliations": ["Department of ..., Politeknik Negeri Batam, Indonesia", ...],
  "corresponding": {"name": "...", "department": "...", "address": "...", "email": "..."},
  "abstract": "100-200 words, no citations",
  "keywords": ["k1", "k2", "k3", "k4", "k5"],
  "sections": [
    {"heading": "INTRODUCTION", "blocks": [
        {"type": "p", "text": "..."},
        {"type": "h2", "text": "Dataset"},              # auto-numbered 2.1.
        {"type": "h3", "text": "Augmentation"},         # auto-numbered 2.1.1.
        {"type": "bullets", "items": ["...", "..."]},
        {"type": "equation", "text": "E = mc^{2}"},     # auto-numbered (1)
        {"type": "figure", "image": "path/or/null.png", "caption": "...", "width_cm": 12},
        {"type": "table", "caption": "...", "header": ["A","B"], "rows": [["1","2"]]}
    ]}
  ],
  "acknowledgements": "optional",
  "funding": "mandatory (e.g. 'Authors state no funding involved.')",
  "credit": {"Author Name 1": ["C","M","O"], ...},     # CRediT roles, mandatory
  "conflict_of_interest": "mandatory (e.g. 'Authors state no conflict of interest.')",
  "informed_consent": "optional",
  "ethical_approval": "optional",
  "data_availability": "mandatory",
  "ai_declaration": "optional but required if generative AI was used substantively",
  "references": ["A. Author, \"Title,\" *J. Abbrev.*, vol. 1, no. 2, pp. 1-10, 2024, doi: 10.xxxx/xxxx.", ...]
}

Mandatory back-matter fields that are missing are filled with a visible
"[TO BE COMPLETED BY AUTHORS: ...]" placeholder and reported as warnings —
the script never invents funding, conflict, or data statements.
"""
import argparse
import json
import os
import re
import struct
import sys
import zipfile
from xml.dom import minidom

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEMPLATE = next((p for p in (os.path.join(HERE, "..", "assets", "JAIC_Paper_Template_2027.docx"),
                         os.path.join(HERE, "JAIC_Paper_Template_2027.docx")) if os.path.exists(p)),
                        os.path.join(HERE, "JAIC_Paper_Template_2027.docx"))

CREDIT_ROLES = ["C", "M", "So", "Va", "Fo", "I", "R", "D", "O", "E", "Vi", "Su", "P", "Fu"]
CREDIT_LEGEND = ("C: Conceptualization; M: Methodology; So: Software; Va: Validation; "
                 "Fo: Formal analysis; I: Investigation; R: Resources; D: Data Curation; "
                 "O: Writing - Original Draft; E: Writing - Review & Editing; Vi: Visualization; "
                 "Su: Supervision; P: Project administration; Fu: Funding acquisition")
TEXT_WIDTH_TWIPS = 11907 - 1701 - 1418  # A4 width minus template left/right margins = 8788

WARNINGS = []


# ----------------------------------------------------------------- helpers
def xe(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


TOKEN = re.compile(r"(\*\*.+?\*\*|\*.+?\*|\^\{.+?\}|_\{.+?\})")


def runs(text, base_rpr=""):
    """Convert light markup into a sequence of <w:r> elements."""
    out = []
    for tok in TOKEN.split(text):
        if not tok:
            continue
        extra = ""
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            tok, extra = tok[2:-2], "<w:b/><w:bCs/>"
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            tok, extra = tok[1:-1], "<w:i/><w:iCs/>"
        elif tok.startswith("^{") and tok.endswith("}"):
            tok, extra = tok[2:-1], '<w:vertAlign w:val="superscript"/>'
        elif tok.startswith("_{") and tok.endswith("}"):
            tok, extra = tok[2:-1], '<w:vertAlign w:val="subscript"/>'
        rpr = base_rpr + extra
        rpr_xml = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
        parts = tok.split("\t")
        inner = "<w:tab/>".join(f'<w:t xml:space="preserve">{xe(p)}</w:t>' for p in parts)
        out.append(f"<w:r>{rpr_xml}{inner}</w:r>")
    return "".join(out)


def para(ppr, text, base_rpr=""):
    return f"<w:p><w:pPr>{ppr}</w:pPr>{runs(text, base_rpr)}</w:p>"


def ptext(p):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))


def first_rpr(p):
    m = re.search(r"<w:r\b[^>]*>\s*(<w:rPr>.*?</w:rPr>)", p, re.S)
    if not m:
        return ""
    inner = m.group(1)[len("<w:rPr>"):-len("</w:rPr>")]
    inner = re.sub(r'<w:rStyle w:val="[^"]*"/>', "", inner)  # drop Hyperlink char style etc.
    inner = re.sub(r'<w:u w:val="[^"]*"/>', "", inner)
    return inner.replace('<w:vertAlign w:val="superscript"/>', "")


def replace_para(p, text, base_rpr=None):
    """Keep the paragraph's <w:p ...> tag and pPr, replace all runs with new text."""
    open_tag = re.match(r"<w:p\b[^>]*>", p).group()
    ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
    ppr = ppr.group() if ppr else ""
    rpr = first_rpr(p) if base_rpr is None else base_rpr
    return f"{open_tag}{ppr}{runs(text, rpr)}</w:p>"


# ----------------------------------------------------------- body blocks
def heading1(text, numbered=True):
    num = '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr><w:ind w:hanging="720"/>' if numbered else ""
    return para(f'<w:pStyle w:val="Heading1"/>{num}', text.upper())


def heading2(text):
    return para('<w:pStyle w:val="Heading2"/><w:rPr><w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/></w:rPr>',
                text, '<w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/>')


def heading3(text):
    rpr = '<w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/><w:i w:val="0"/><w:color w:val="000000"/><w:szCs w:val="20"/>'
    return para(f'<w:pStyle w:val="Heading3"/><w:rPr>{rpr}</w:rPr>', text, rpr)


def body_p(text, indent=True):
    return para('<w:ind w:firstLine="720"/>' if indent else "", text)


def bullets(items):
    return "".join(para('<w:ind w:left="1080" w:hanging="360"/>', "•\t" + it) for it in items)


def equation(text, n, omml=None):
    tabs = (f'<w:tabs><w:tab w:val="center" w:pos="{TEXT_WIDTH_TWIPS // 2}"/>'
            f'<w:tab w:val="right" w:pos="{TEXT_WIDTH_TWIPS}"/></w:tabs>'
            '<w:spacing w:before="120" w:after="120"/><w:jc w:val="left"/>')
    if omml:
        return (f"<w:p><w:pPr>{tabs}</w:pPr><w:r><w:tab/></w:r>{omml}"
                f'<w:r><w:tab/><w:t xml:space="preserve">({n})</w:t></w:r></w:p>')
    return para(tabs, f"\t{text}\t({n})")


CAPTION_PPR = ('<w:keepNext/><w:spacing w:before="60" w:after="120"/><w:jc w:val="center"/>'
               '<w:rPr><w:sz w:val="16"/><w:szCs w:val="16"/></w:rPr>')
CAPTION_RPR = '<w:color w:val="000000"/><w:sz w:val="16"/><w:szCs w:val="16"/>'


def fig_caption(n, text):
    ppr = CAPTION_PPR.replace("<w:keepNext/>", "")
    return f"<w:p><w:pPr>{ppr}</w:pPr>{runs(f'Figure {n}. ', CAPTION_RPR)}{runs(text, CAPTION_RPR)}</w:p>"


def tbl_caption(n, text):
    return f"<w:p><w:pPr>{CAPTION_PPR}</w:pPr>{runs(f'Table {n}. ', CAPTION_RPR)}{runs(text, CAPTION_RPR)}</w:p>"


def image_size(path):
    """Return (w, h) pixels for PNG/JPEG without PIL."""
    with open(path, "rb") as f:
        head = f.read(26)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", head[16:24])
        f.seek(0)
        data = f.read()
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return 1600, 1000


def figure_xml(rid, n, w_cm, path):
    pw, ph = image_size(path)
    cx = int(w_cm * 360000)
    cy = int(cx * ph / pw)
    return (
        '<w:p><w:pPr><w:keepNext/><w:spacing w:before="120"/><w:jc w:val="center"/></w:pPr><w:r><w:drawing>'
        f'<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
        f'<wp:docPr id="{1000 + n}" name="Figure {n}"/>'
        '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        f'<pic:nvPicPr><pic:cNvPr id="{1000 + n}" name="fig{n}"/><pic:cNvPicPr/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
        "</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>"
    )


def figure_placeholder(n):
    return para('<w:keepNext/><w:spacing w:before="120"/><w:jc w:val="center"/>',
                f"[INSERT FIGURE {n} HERE]", '<w:highlight w:val="yellow"/>')


def table_xml(header, rows, font_sz=16, center=True, first_col_w=None):
    """Three-line academic table: top rule, rule under header, bottom rule."""
    ncol = len(header)
    colw = TEXT_WIDTH_TWIPS // ncol
    widths = [colw] * ncol
    if first_col_w:
        widths = [first_col_w] + [(TEXT_WIDTH_TWIPS - first_col_w) // (ncol - 1)] * (ncol - 1)
    jc = '<w:jc w:val="center"/>' if center else ""
    rpr = f'<w:sz w:val="{font_sz}"/><w:szCs w:val="{font_sz}"/>'

    def cell(t, bold=False, borders="", w=colw, left=False):
        r = rpr + ("<w:b/><w:bCs/>" if bold else "")
        j = '<w:jc w:val="left"/>' if left else jc
        return (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{borders}</w:tcPr>'
                f'<w:p><w:pPr><w:spacing w:before="20" w:after="20"/>{j}</w:pPr>{runs(str(t), r)}</w:p></w:tc>')

    def row_xml(cells, bold, borders):
        return "".join(cell(c, bold, borders, widths[k], left=(first_col_w is not None and k == 0))
                       for k, c in enumerate(cells))

    hb = '<w:tcBorders><w:top w:val="single" w:sz="8" w:color="000000"/><w:bottom w:val="single" w:sz="4" w:color="000000"/></w:tcBorders>'
    lb = '<w:tcBorders><w:bottom w:val="single" w:sz="8" w:color="000000"/></w:tcBorders>'
    out = ['<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/><w:jc w:val="center"/>'
           '<w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>' + "".join(f'<w:gridCol w:w="{w}"/>' for w in widths) + "</w:tblGrid>"]
    out.append('<w:tr><w:trPr><w:tblHeader/></w:trPr>' + row_xml(header, True, hb) + "</w:tr>")
    for i, row in enumerate(rows):
        b = lb if i == len(rows) - 1 else ""
        out.append("<w:tr>" + row_xml(row, False, b) + "</w:tr>")
    out.append("</w:tbl>")
    out.append('<w:p><w:pPr><w:spacing w:after="120"/></w:pPr></w:p>')
    return "".join(out)


def ref_para(n, text):
    ppr = ('<w:widowControl w:val="0"/><w:ind w:left="426" w:hanging="426"/>'
           '<w:rPr><w:rFonts w:asciiTheme="majorHAnsi" w:hAnsiTheme="majorHAnsi"/><w:sz w:val="16"/><w:szCs w:val="16"/></w:rPr>')
    rpr = '<w:rFonts w:asciiTheme="majorHAnsi" w:hAnsiTheme="majorHAnsi"/><w:noProof/><w:sz w:val="16"/><w:szCs w:val="16"/>'
    text = re.sub(r"^\s*\[\d+\]\s*", "", text)
    return para(ppr, f"[{n}]\t{text}", rpr)


def mandatory(content, key, label):
    v = (content.get(key) or "").strip()
    if not v:
        WARNINGS.append(f"Mandatory section '{label}' is empty — placeholder inserted.")
        return f"[TO BE COMPLETED BY AUTHORS: {label}]"
    return v


# ----------------------------------------------------------------- build
def build_body(content, media):
    out = []
    fig_n = tbl_n = eq_n = 0
    for s_i, sec in enumerate(content.get("sections", []), start=1):
        out.append(heading1(sec["heading"]))
        h2 = h3 = 0
        for b in sec.get("blocks", []):
            t = b.get("type", "p")
            if t == "p":
                out.append(body_p(b["text"]))
            elif t == "h2":
                h2 += 1
                h3 = 0
                out.append(heading2(f"{s_i}.{h2}.  {b['text']}"))
            elif t == "h3":
                h3 += 1
                out.append(heading3(f"{s_i}.{h2}.{h3}. {b['text']}"))
            elif t == "bullets":
                out.append(bullets(b["items"]))
            elif t == "equation":
                eq_n += 1
                out.append(equation(b.get("text", ""), eq_n, b.get("omml")))
            elif t == "figure":
                fig_n += 1
                img = b.get("image")
                if img and os.path.exists(img):
                    ext = os.path.splitext(img)[1].lower().lstrip(".")
                    rid = f"rIdJaicFig{fig_n}"
                    media.append((rid, f"media/jaic_fig{fig_n}.{ext}", img, ext))
                    out.append(figure_xml(rid, fig_n, float(b.get("width_cm", 12)), img))
                else:
                    if img:
                        WARNINGS.append(f"Figure {fig_n}: image '{img}' not found — placeholder inserted.")
                    out.append(figure_placeholder(fig_n))
                out.append(fig_caption(fig_n, b.get("caption", "")))
            elif t == "table":
                tbl_n += 1
                out.append(tbl_caption(tbl_n, b.get("caption", "")))
                out.append(table_xml(b["header"], b["rows"]))
            else:
                WARNINGS.append(f"Unknown block type '{t}' skipped.")

    # ---- back matter (order follows the 2027 template)
    if content.get("acknowledgements"):
        out += [heading1("ACKNOWLEDGEMENTS", False), body_p(content["acknowledgements"])]
    out += [heading1("FUNDING INFORMATION", False),
            body_p(mandatory(content, "funding", "Funding Information"))]

    out.append(heading1("AUTHOR CONTRIBUTIONS STATEMENT", False))
    credit = content.get("credit") or {}
    if not credit:
        WARNINGS.append("Mandatory CRediT author contribution table is empty — placeholder rows inserted.")
        credit = {a["name"]: [] for a in content.get("authors", [])} or {"Author Name 1": []}
    rows = [[name] + ["✓" if r in roles else "" for r in CREDIT_ROLES] for name, roles in credit.items()]
    out.append(table_xml(["Name of Author"] + CREDIT_ROLES, rows, font_sz=14, first_col_w=2800))
    out.append(para('<w:jc w:val="left"/>', CREDIT_LEGEND, '<w:sz w:val="14"/><w:szCs w:val="14"/>'))

    out += [heading1("CONFLICT OF INTEREST STATEMENT", False),
            body_p(mandatory(content, "conflict_of_interest", "Conflict of Interest Statement"))]
    if content.get("informed_consent"):
        out += [heading1("INFORMED CONSENT", False), body_p(content["informed_consent"])]
    if content.get("ethical_approval"):
        out += [heading1("ETHICAL APPROVAL", False), body_p(content["ethical_approval"])]
    out += [heading1("DATA & CODE AVAILABILITY", False),
            body_p(mandatory(content, "data_availability", "Data & Code Availability"))]
    if content.get("ai_declaration"):
        out += [heading1("DECLARATION OF GENERATIVE AI AND AI-ASSISTED TECHNOLOGIES", False),
                body_p(content["ai_declaration"])]

    out.append(heading1("REFERENCES", False))
    refs = content.get("references", [])
    if len(refs) < 15:
        WARNINGS.append(f"Only {len(refs)} references — JAIC requires at least 15.")
    out += [ref_para(i, r) for i, r in enumerate(refs, start=1)]
    return "".join(out)


def build_header(head, content):
    paras = list(re.finditer(r"<w:p\b[^>]*?(?:/>|>.*?</w:p>)", head, re.S))
    repl = {}  # (start,end) -> new xml
    title_done = False
    kw_paras, aff_paras = [], []
    for m in paras:
        p, t = m.group(), ptext(m.group())
        span = (m.start(), m.end())
        if '<w:pStyle w:val="Title"/>' in p:
            repl[span] = "" if title_done else replace_para(p, content["title"])
            title_done = True
        elif "First Author" in t and "Second Author" in t:
            open_tag = re.match(r"<w:p\b[^>]*>", p).group()
            ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S).group()
            r = '<w:b/><w:color w:val="000000"/>'
            parts = []
            for i, a in enumerate(content["authors"]):
                sep = ", " if i < len(content["authors"]) - 1 else ""
                sup = ",".join(str(x) for x in a.get("affil", [1]))
                parts.append(runs(a["name"], r) + runs("^{" + sup + "}", r) + runs(sep, r))
            repl[span] = f"{open_tag}{ppr}{''.join(parts)}</w:p>"
        elif "Politeknik Negeri Batam, Indonesia (9 pt)" in t:
            aff_paras.append(m)
        elif t.startswith("An abstract is often presented"):
            repl[span] = replace_para(p, content["abstract"])
        elif re.fullmatch(r"(First|Second|Third|Fourth|Fifth) keyword", t.strip()):
            kw_paras.append(m)
        elif t.startswith("Name of Corresponding Author"):
            repl[span] = replace_para(p, content["corresponding"]["name"] + ",")
        elif t.startswith("Department of Informatics, Politeknik Negeri Batam, Batam"):
            repl[span] = replace_para(p, content["corresponding"]["department"])
        elif t.startswith("Jl. Ahmad Yani"):
            repl[span] = replace_para(p, content["corresponding"]["address"])
        elif t.strip().startswith("Email:"):
            repl[span] = replace_para(p, "Email: " + content["corresponding"]["email"])

    # affiliations: first template paragraph is the model, others removed
    if aff_paras:
        model = aff_paras[0].group()
        open_tag = re.match(r"<w:p\b[^>]*>", model).group()
        ppr = re.search(r"<w:pPr>.*?</w:pPr>", model, re.S).group()
        rpr = '<w:color w:val="000000"/>'
        new = "".join(f"{open_tag}{ppr}{runs('^{' + str(i) + '}', rpr)}{runs(a, rpr)}</w:p>"
                      for i, a in enumerate(content["affiliations"], start=1))
        repl[(aff_paras[0].start(), aff_paras[0].end())] = new
        for m in aff_paras[1:]:
            repl[(m.start(), m.end())] = ""

    # keywords: reuse slots, clone if more than 5, drop unused
    kws = content.get("keywords", [])
    if kw_paras:
        model = kw_paras[0].group()
        for i, m in enumerate(kw_paras):
            if i < len(kws):
                txt = replace_para(m.group(), kws[i])
                if i == len(kw_paras) - 1 and len(kws) > len(kw_paras):
                    txt += "".join(replace_para(model, k) for k in kws[len(kw_paras):])
                repl[(m.start(), m.end())] = txt
            else:
                repl[(m.start(), m.end())] = ""

    for key in ("title", "authors", "affiliations", "abstract", "keywords", "corresponding"):
        if not content.get(key):
            raise SystemExit(f"content.json is missing required field '{key}'")

    out, last = [], 0
    for (s, e) in sorted(repl):
        out.append(head[last:s])
        out.append(repl[(s, e)])
        last = e
    out.append(head[last:])
    return "".join(out)


def build_footer(xml, content):
    short = content.get("running_title") or content["title"]
    first = content["authors"][0]["name"].split()[-1]
    auth = content.get("running_author") or (first + (" et al." if len(content["authors"]) > 1 else ""))
    texts = list(re.finditer(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", xml))
    idx = [i for i, m in enumerate(texts) if "Paper" in m.group(1) or "accurately" in m.group(1)
           or m.group(1) in ("…", " ") or "(First Author)" in m.group(1)]
    if not idx:
        return xml
    out, last = [], 0
    for j, i in enumerate(idx):
        m = texts[i]
        if j == 0:
            new = f'<w:t xml:space="preserve">{xe(short)}</w:t>'
        elif "(First Author)" in m.group(1):
            new = f'<w:t xml:space="preserve"> ({xe(auth)})</w:t>'
        else:
            new = '<w:t xml:space="preserve"></w:t>'
        out += [xml[last:m.start()], new]
        last = m.end()
    out.append(xml[last:])
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content")
    ap.add_argument("output")
    ap.add_argument("--template", default=DEFAULT_TEMPLATE)
    a = ap.parse_args()

    content = json.load(open(a.content, encoding="utf8"))
    if not os.path.exists(a.template):
        sys.exit(f"Template not found: {a.template}. Download it with:\n  curl -L -o JAIC_Paper_Template_2027.docx "
                 "'https://docs.google.com/document/d/1sX-P19U60-hrDAWml5DeOyfhrTLlGjgn/export?format=docx'")
    zin = zipfile.ZipFile(a.template)
    doc = zin.read("word/document.xml").decode("utf8")

    # Body starts at the INTRODUCTION heading paragraph, ends at body-level sectPr.
    i = doc.find("INTRODUCTION (10 PT)")
    if i < 0:
        sys.exit("Template not recognised: 'INTRODUCTION (10 PT)' placeholder not found. "
                 "Use the original JAIC Paper Template 2027.")
    body_start = max(doc.rfind("<w:p ", 0, i), doc.rfind("<w:p>", 0, i))
    body_end = doc.rfind("<w:sectPr")
    if doc.count("<w:sectPr") != 1:
        sys.exit("Template not recognised: expected exactly 1 <w:sectPr> (single-column 2027 template).")

    media = []
    new_doc = build_header(doc[:body_start], content) + build_body(content, media) + doc[body_end:]
    minidom.parseString(new_doc.encode("utf8"))  # well-formedness check

    rels = zin.read("word/_rels/document.xml.rels").decode("utf8")
    for rid, target, _, _ in media:
        rels = rels.replace("</Relationships>",
                            f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{target}"/></Relationships>')
    ctypes = zin.read("[Content_Types].xml").decode("utf8")
    for ext, mime in (("jpg", "image/jpeg"), ("jpeg", "image/jpeg"), ("png", "image/png")):
        if any(m[3] == ext for m in media) and f'Extension="{ext}"' not in ctypes:
            ctypes = ctypes.replace("<Default ", f'<Default Extension="{ext}" ContentType="{mime}"/><Default ', 1)

    with zipfile.ZipFile(a.output, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = new_doc.encode("utf8")
            elif item.filename == "word/_rels/document.xml.rels":
                data = rels.encode("utf8")
            elif item.filename == "[Content_Types].xml":
                data = ctypes.encode("utf8")
            elif item.filename == "word/footer2.xml":
                data = build_footer(data.decode("utf8"), content).encode("utf8")
            zout.writestr(item, data)
        for _, target, src, _ in media:
            zout.write(src, "word/" + target)

    print(f"Wrote {a.output}")
    for w in WARNINGS:
        print("WARNING:", w)


if __name__ == "__main__":
    main()
