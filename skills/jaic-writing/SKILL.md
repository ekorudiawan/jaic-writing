---
name: jaic-writing
description: >
  Use this skill whenever the user wants to write, draft, format, review, improve, or
  check a manuscript for the Journal of Applied Informatics and Computing (JAIC).
  Trigger this skill for any task involving JAIC paper writing, abstract drafting,
  section structuring, reference formatting (IEEE style), title creation, reference
  validation (DOI, journal/conference source check), generating a .docx on the
  JAIC Paper Template 2027, writing the mandatory back-matter statements (funding,
  CRediT author contributions, conflict of interest, data availability, generative-AI
  declaration), or compliance checking against JAIC author guidelines. Also trigger
  when the user mentions "JAIC", "Journal of Applied Informatics and Computing", or
  asks for help with a paper submission to this journal. Always use this skill if the
  user wants to prepare, revise, evaluate, or check any part of a JAIC manuscript —
  even if they don't explicitly say "JAIC skill". Trigger also when the user asks to
  write a paper about robotics, informatics, computing, or related topics that could
  be submitted to JAIC.
---

# JAIC Writing Skill

Writing, reviewing, and formatting manuscripts for the **Journal of Applied
Informatics and Computing (JAIC)**, Politeknik Negeri Batam.

> **Rules last verified: 23 Nov 2026** against the JAIC homepage, Author Guidelines,
> Submissions, Plagiarism and Generative-AI policy pages, and the **JAIC Paper
> Template 2027**. The 2027 template replaced the old *Template Jurnal JAIC v3_2020*
> (Times New Roman, two-column, Roman-numeral headings) — don't apply the 2020 layout
> rules any more. If a task happens long after this date, re-check the Author
> Guidelines page, because JAIC revises its template roughly yearly.

---

## 1. Journal Profile

| Item | Detail |
|---|---|
| Full name | Journal of Applied Informatics and Computing (JAIC) |
| Publisher | Politeknik Negeri Batam (Department of Informatic Engineering) |
| e-ISSN | 2548-6861 — Crossref DOI prefix 10.30871 |
| Accreditation | SINTA 3 (SK No. 79/E/KPT/2023) |
| Indexing | DOAJ, SINTA 3, EBSCO, Crossref |
| Frequency | 6 issues/year (end of Feb, Apr, Jun, Aug, Oct, Dec) |
| License | CC BY-SA 4.0, open access |
| Language | English (**preferred**) or Bahasa Indonesia (EYD) |
| Article types | Original research; review articles (SLR/structured reviews must state search strategy, selection criteria, analysis and synthesis method) |
| Scope | Applied informatics, applied computing, applied mathematics, applied network computing |
| Similarity | iThenticate: **< 20 % overall, ≤ 3 % from any single source**; plagiarism/self-plagiarism → immediate rejection |
| Author Guidelines | https://jurnal.polibatam.ac.id/index.php/JAIC/authorGuidelines |
| Template 2027 (Google Docs) | https://docs.google.com/document/d/1sX-P19U60-hrDAWml5DeOyfhrTLlGjgn/edit |
| Template as .docx | append `/export?format=docx` in place of `/edit` (Section 9 explains how to obtain it) |

---

## 2. Manuscript Requirements

The website guidelines and the prose inside the 2027 template disagree on a few
numbers (the template text was adapted from another journal's template). To be safe
against both, apply the **stricter value** and tell the author when you do, so they
know why.

| Item | Website guideline | Template text | **Apply** |
|---|---|---|---|
| Length | 4–15 pages incl. refs, tables, figures, appendices (>15 only with editor approval) | max 12 pages (research), 16 (review) | **4–12 pages** research; **≤ 15** review |
| Title | ≤ 10 words | ≈ 12 words | **≤ 10 words** |
| Abstract | ≤ 250 words | 100–200 words | **100–200 words** |
| Keywords | number per template | 5–7 (template shows 5 slots) | **5** (max 7) |

### 2.1 Title
- **≤ 10 words**, specific and informative (titles drive indexing and retrieval).
- No acronyms/abbreviations unless universally recognised; no long formulas or subscripts.
- Don't name the method unless the paper proposes a new method.
- Drop filler openers: "A Study of", "Investigation of", "Implementation of",
  "Observations on", "Effect of", "Analysis of", "Design of".
- Title Case (capitalise all words except conjunctions/prepositions).
- Format: Cambria 16 pt, bold, centered (style *Title*).

### 2.2 Authors & affiliations
- Names 10 pt bold, centered, numeric superscripts linking to affiliations; no academic titles.
- Affiliations 9 pt: Department, Institution, Country.
- **At least two authors recommended**, one designated corresponding author.
- Corresponding-author block (inside the Article Info table): name, department & institution,
  full postal address, email.
- *Received / Revised / Accepted* stay as "…" — the editor fills them.

### 2.3 Abstract
- **100–200 words**, one self-contained paragraph, 9 pt.
- Cover: problem/objective → approach/method → main (quantitative) results → conclusion.
- **No citations**, no undefined or non-standard abbreviations (define at first use if essential).
- Write it in English even if the body is in Indonesian.

### 2.4 Keywords
- **5** (max 7), right after the abstract (one per line in the Article Info column).
- American spelling; avoid general terms, plurals, multi-concept phrases ("and", "of"),
  and words already in the title. Abbreviations only if firmly established.

### 2.5 Structure (IMRaD, numbered headings)
```
1. INTRODUCTION
2. THE COMPREHENSIVE THEORETICAL BASIS AND/OR PROPOSED METHOD/ALGORITHM (optional)
3. METHOD
4. RESULTS AND DISCUSSION
5. CONCLUSION
   ACKNOWLEDGEMENTS                      (if applicable)
   FUNDING INFORMATION                   (mandatory)
   AUTHOR CONTRIBUTIONS STATEMENT        (mandatory — CRediT table)
   CONFLICT OF INTEREST STATEMENT        (mandatory)
   INFORMED CONSENT                      (if applicable)
   ETHICAL APPROVAL                      (if applicable)
   DATA & CODE AVAILABILITY              (mandatory)
   DECLARATION OF GENERATIVE AI AND AI-ASSISTED TECHNOLOGIES  (if AI used substantively)
   REFERENCES
```
Back-matter headings are unnumbered. Renumber main sections when the optional theory
section is omitted (Method becomes 2, etc.).

**Section content guidance (from the template):**
- **Introduction — 3 to 6 paragraphs**: (i) background, (ii) problem statement,
  (iii) relevant literature, (iv) proposed approach/solution, (v) novelty/innovation.
  Literature here shows how this paper differs from prior work. Ending with a short
  paragraph outlining the rest of the paper is optional but helps reviewers.
- **Method** — describe the research *chronologically*: design, procedure (algorithm,
  pseudocode, flowchart), testing method, data acquisition; support steps with references.
  If generative AI is part of the methodology, describe it here too.
- **Results and Discussion** — results in figures/tables plus a comprehensive discussion
  and comparison with prior work; sub-sections allowed.
- **Conclusion** — show that what the Introduction promised was delivered in Results;
  may add limitations and future work; **no new data or claims**.

---

## 3. Formatting Rules (JAIC Paper Template 2027)

### 3.1 Page layout
- A4, **single column**, single line spacing.
- Margins come from the template file (top/right/bottom 2.5 cm, left 3.0 cm). The
  template prose says 2.5/2 cm, but keep the file's page setup — never re-set margins.
- Headers/footers (journal name, e-ISSN, volume, DOI, running title + author) come from
  the template; keep them and update the running title/author in the even-page footer.

### 3.2 Fonts and sizes (Cambria throughout)

| Element | Size | Style |
|---|---|---|
| Title | 16 pt | Bold, centered (style *Title*) |
| Author names | 10 pt | Bold, centered, superscript affiliation numbers |
| Affiliations | 9 pt | Centered |
| Abstract body | 9 pt | Justified |
| Heading level 1 | 10 pt | Bold, ALL CAPS, numbered `1.`, `2.` (style *Heading 1*) |
| Heading level 2 | 10 pt | Bold italic, `3.1.` (style *Heading 2*, Cambria) |
| Heading level 3 | 10 pt | Bold, non-italic, `3.2.1.` (style *Heading 3*, Cambria) |
| Body text | 10 pt | Justified, first-line indent 1.27 cm |
| Figure / table captions | 8 pt | Centered — "Figure 1. …" below figure; "Table 1. …" above table |
| References | 8 pt | Hanging indent 0.75 cm, `[n]` + tab |

### 3.3 Figures
- Centered; Arabic numbering, **"Figure 1."** caption **below** the figure.
- Sub-figures labelled (a), (b)… with one overall caption describing each panel.
- Cite every figure in the text before it appears (e.g., "Figure 2(a) shows…").
- High resolution, legible in grayscale; acknowledge and obtain permission for reused material.
- AI-generated or AI-altered figures must be disclosed and must not misrepresent results.

### 3.4 Tables
- Centered; **"Table 1."** (Arabic, not Roman) caption **above** the table.
- Clean three-line style (top rule, rule under header, bottom rule), 8 pt.
- Cite every table in the text before it appears.

### 3.5 Equations
- Centered, numbered consecutively in parentheses flush right: (1), (2)…
- Microsoft Equation Editor or MathType; refer to them as "in (1)".
- Define every symbol in the text right after the equation.

### 3.6 Other conventions
- Foreign-language terms in *italics* (e.g., English terms inside an Indonesian manuscript).
- Each heading on its own line.

---

## 4. References — Critical Rules

There are two layers: what JAIC requires, and this author's **stricter house rules**.
Enforce both, and when reporting a problem say which layer it comes from.

### 4.1 JAIC requirements
- **IEEE style**, numbered by order of first citation, managed with Zotero/Mendeley/EndNote.
- **At least 15 references** (15–20+ recommended); **≥ 60 % journal articles**.
- Every reference cited in the text; authors, title, year, volume/issue, pages and DOI verified.
- Prefer relevant, credible, recent publications; seminal works allowed when needed.
- Never let generative AI fabricate references — verify every entry.

### 4.2 Author's house rules (stricter — always apply)
- **No preprints** (arXiv, ResearchGate uploads, bioRxiv, SSRN, TechRxiv…) — find the
  peer-reviewed version or replace. (The 2027 template shows an arXiv example; ignore it.)
- **Every reference must have a valid, verified DOI.** No DOI → replace the reference.
  Never invent or guess DOIs; verify via doi.org or Crossref.
- **≥ 50 % from the last 5 years.**
- Source priority: (1) international peer-reviewed journals (Scopus/WoS/DOAJ) →
  (2) international conference proceedings (IEEE, ACM, Springer, Elsevier) →
  (3) SINTA 1–2 national journals → (4) books from reputable publishers.
- Aim for 20+ references so the 60 % journal ratio survives conference/self-citations.

### 4.3 IEEE format (as in the 2027 template)
```
Journal:    [2] G. Nguyen et al., "Machine learning and deep learning frameworks and
                libraries for large-scale data mining: a survey," Artif. Intell. Rev.,
                vol. 52, no. 1, pp. 77–124, 2019, doi: 10.1007/s10462-018-09679-z.
Conference: [11] Y. Wu et al., "Large scale incremental learning," in Proc. IEEE/CVF
                Conf. Comput. Vis. Pattern Recognit. (CVPR), 2019, pp. 374–382,
                doi: 10.1109/CVPR.2019.00046.
Book:       [23] S. Leonelli and N. Tempini, Eds., Data Journeys in the Sciences. Cham,
                Switzerland: Springer, 2020, doi: 10.1007/978-3-030-37177-7.
```
- Initials before surname; abbreviated, *italic* journal names.
- DOI as `doi: 10.xxxx/xxxx` at the end (not `https://doi.org/...` or `[Online]. Available:`).
- In-text: `[1]`, `[16], [17]`, ranges `[20]–[25]`. At sentence start: "Ref. [18] shows…".
  In running text for 3+ authors: "Nguyen et al. [2]".

---

## 5. Mandatory Back-Matter Statements

These sections are new in the 2027 template and a common reason for desk return.
Don't invent facts for them — ask the author, or leave a clearly marked placeholder.

| Section | What to write | Wording when nothing applies |
|---|---|---|
| Funding Information | Funder name + grant number(s) | "Authors state no funding involved." |
| Author Contributions | CRediT table; each author needs ≥ 1 of C/M/Fo/I **and** ≥ 1 of O/E | — |
| Conflict of Interest | Financial, personal, professional or non-financial competing interests | "Authors state no conflict of interest." |
| Informed Consent | Only if identifiable people are involved | "We have obtained informed consent from all individuals included in this study." |
| Ethical Approval | Human/animal research: national rules, institutional board, Helsinki Declaration | (standard sentences in template) |
| Data & Code Availability | Repository + DOI/URL, embargo, on request, third party, or not applicable | e.g. "The data that support the findings of this study are available from the corresponding author, [initials], upon reasonable request." |
| Generative AI declaration | Tool name, version/model, purpose, extent of human review, authors take full responsibility; placed **just before References** | Not needed for basic spelling/grammar checks only |

**CRediT codes:** C Conceptualization · M Methodology · So Software · Va Validation ·
Fo Formal analysis · I Investigation · R Resources · D Data Curation ·
O Writing – Original Draft · E Writing – Review & Editing · Vi Visualization ·
Su Supervision · P Project administration · Fu Funding acquisition.

AI tools can never be authors. Since this author drafts with Claude, whenever Claude
wrote or substantially edited text, remind the author to include the declaration, e.g.:
*"During the preparation of this work the authors used Claude (Anthropic) to
[improve language / draft sections / …]. After using this tool, the authors reviewed
and edited the content as needed and take full responsibility for the content of the
publication."*

---

## 6. Writing Workflow

1. **Understand the paper** — topic & contribution, method, key results, target sections,
   authors and affiliations, funding, data availability, AI-tool use. Ask only for what's missing.
2. **Draft in IMRaD order** (Section 2.5) — numbered sub-sections (`3.1.`, `3.2.1.`),
   every figure/table/equation referenced before it appears, formal tone (avoid first person where possible).
3. **Compile & validate references** — type (journal/conference, no preprint), DOI resolves,
   count ≥ 15 (aim 20), journal share ≥ 60 %, ≥ 50 % within 5 years, all cited in text.
4. **Title, abstract, keywords** — ≤ 10 words; 100–200 words, no citations; 5 keywords not repeating the title.
5. **Back matter** (Section 5) — missing facts → ask, or mark `[TO BE COMPLETED BY AUTHORS: …]`.
6. **Build the .docx** (Section 9), then run the **checklist** (Section 7) and report results.

### Versioned copies after major updates
After a significant revision of a manuscript .docx, save a versioned copy next to the main
file as `<BaseName>_v<N>.docx` (e.g. `JAIC_Manuscript_YOLOv11OBB_v2.docx`), starting at `_v1`.
Major = structural changes, rewritten paragraphs/new results, multi-part compliance fixes
(reference reorganisation, abstract rewrite), or anything the author asks to preserve.
Typos, single-word tweaks and formatting-only changes don't need a new version. Save to the
author's workspace/connected folder when available so they can open it on their computer.

---

## 7. JAIC Compliance Checklist

```
TEMPLATE & LENGTH
[ ] Built on JAIC Paper Template 2027 (Cambria, single column) — not the 2020 template
[ ] 4–12 pages (research) / ≤ 15 (review), incl. references, tables, figures, appendices
[ ] Template headers/footers kept; running title + author updated

TITLE & AUTHORS
[ ] Title ≤ 10 words, no unnecessary acronyms, no filler openers
[ ] No academic titles in names; superscript affiliation numbers
[ ] ≥ 2 authors recommended; corresponding-author block complete (name, dept, address, email)

ABSTRACT & KEYWORDS
[ ] 100–200 words, English, single paragraph
[ ] No citations, no undefined abbreviations
[ ] Covers problem/objective, method, quantitative results, conclusion
[ ] 5 keywords (≤ 7), American spelling, not repeating title words

STRUCTURE
[ ] Numbered IMRaD: Introduction → (Theory/Proposed Method) → Method → Results and Discussion → Conclusion
[ ] Introduction 3–6 paragraphs incl. explicit novelty statement
[ ] Conclusion adds no new data/claims
[ ] Funding Information present
[ ] Author Contributions (CRediT table) present; every author has ≥1 of C/M/Fo/I and ≥1 of O/E
[ ] Conflict of Interest present
[ ] Data & Code Availability present
[ ] Informed Consent / Ethical Approval if human or animal subjects
[ ] Generative-AI declaration before References if AI used substantively

FIGURES, TABLES, EQUATIONS
[ ] "Figure n." captions below, "Table n." captions above (Arabic numerals)
[ ] All cited in text before they appear; centered
[ ] Equations centered, numbered (n) flush right, symbols defined

REFERENCES
[ ] ≥ 15 (aim 20+), all cited in text, IEEE style, numbered by first citation
[ ] ≥ 60 % journal articles
[ ] [house] zero preprints; every entry has a verified DOI; ≥ 50 % from last 5 years
[ ] Managed in Zotero (IEEE) — no hand-typed [n] numbers

ORIGINALITY & LANGUAGE
[ ] iThenticate similarity < 20 % overall, ≤ 3 % per source
[ ] Not under review elsewhere
[ ] English proofread (Grammarly etc.) or Indonesian per EYD; foreign terms italic
```

---

## 8. Common Mistakes to Avoid

1. **Using the old 2020 template** (Times New Roman, two columns, Roman numerals, "TABLE I") — JAIC now expects the 2027 Cambria single-column layout with Arabic numbering.
2. **Missing mandatory back matter** — Funding, CRediT contributions, Conflict of Interest, Data & Code Availability.
3. **Abstract outside 100–200 words** or containing citations.
4. **Title > 10 words** or starting with "Analysis of / Design of / Implementation of".
5. **Fewer than 15 references** or < 60 % journal articles.
6. **Preprints / missing DOIs** (house rule) — always find the published version.
7. **Undisclosed AI assistance** or AI-fabricated references — both violate the JAIC AI policy.
8. **Figures/tables not cited before they appear**, or caption on the wrong side.
9. **High similarity to one source** (> 3 %), including self-plagiarism from the author's own earlier papers or theses.
10. **Manual reference renumbering** — renumbering by hand silently breaks in-text citations (e.g., `[8]` suddenly points to the wrong paper). Use Zotero so numbers update automatically; if Zotero wasn't used, audit every in-text citation against the list (parsing `word/document.xml` programmatically catches mismatches invisible in Word).

---

## 8a. Zotero Workflow (Author Preference)

This author uses **Zotero** with the Word plugin.

- Citation style **IEEE** (Preferences → Cite → Styles → search "IEEE").
- Add items to the library first, then use **Insert Citation** in Word — never type `[n]` manually.
- Fill the **DOI field** for every item (right-click → Lookup / CrossRef).
- After adding/removing references click **Refresh** in the Zotero toolbar so citations and bibliography renumber together.
- For a clean standalone list use **Edit → Copy Bibliography** (IEEE); check the DOI prints as `doi: 10.xxxx/xxxx`.
- If Zotero was not used, audit every in-text citation against the list after any reorganisation (Section 8, item 10).
- JAIC's own Mendeley/Zotero handout: https://jurnal.polibatam.ac.id/index.php/JAIC/announcement/view/64

---

## 9. Generating the .docx from the 2027 Template

Always build on the **real template file** — recreating it with python-docx or docx-js
loses the embedded Cambria fonts, headers/footers, Article Info table, heading numbering
and CC BY-SA badge. Use the generator script from **Appendix A**.

**Setup (once per session, in a working folder, e.g. `/tmp/jaic/`):**
- Script: if `<skill-dir>/scripts/build_jaic_docx.py` exists use it; otherwise write the
  code in Appendix A verbatim to `build_jaic_docx.py`.
- Template: use, in order, `<skill-dir>/assets/JAIC_Paper_Template_2027.docx`; a copy the
  author supplies (e.g. in their connected folder); or download it next to the script:
  ```bash
  curl -L -o JAIC_Paper_Template_2027.docx \
    "https://docs.google.com/document/d/1sX-P19U60-hrDAWml5DeOyfhrTLlGjgn/export?format=docx"
  ```
  (≈ 5.7 MB because of embedded fonts). If none works, ask the author to attach the template.

```bash
python3 build_jaic_docx.py content.json "JAIC_Manuscript_<Topic>_v1.docx" \
        [--template JAIC_Paper_Template_2027.docx]
```

1. Write `content.json` (schema in the script docstring): title, running_title, authors
   (+ affiliation numbers), affiliations, corresponding author, abstract, keywords,
   `sections` (blocks `p`, `h2`, `h3`, `bullets`, `equation`, `figure`, `table`),
   back-matter fields, `credit`, `references`.
   Inline markup: `**bold**`, `*italic*`, `^{sup}`, `_{sub}`; text is XML-escaped automatically.
2. Run the script. It fills the template placeholders, regenerates the body
   (auto-numbered sections `1.`, sub-sections `3.1.` / `3.2.1.`, figures, tables, equations),
   builds the CRediT table, updates the footer running title, and checks XML well-formedness.
3. Read its **WARNING** lines — empty mandatory statements (inserted as
   `[TO BE COMPLETED BY AUTHORS: …]`), missing images (yellow `[INSERT FIGURE n HERE]`),
   fewer than 15 references. Relay them to the author.
4. Verify visually: `soffice --headless --convert-to pdf out.docx`, rasterise with
   `pdftoppm -r 70 -png`, look at the pages, and count them against the 12-page limit.
   (The JAIC logo overlapping the header text on page 1 is a LibreOffice rendering quirk
   of the original template; it looks fine in Word.)
5. Save a versioned copy (Section 6) and deliver the file.

**Template facts (for manual edits or troubleshooting):**
- One `<w:sectPr>` only (body-level): A4 11907×16840 twips; margins top/right/bottom 1418, left 1701; single column.
- Body = from the "INTRODUCTION (10 PT)" Heading1 paragraph up to the body-level `<w:sectPr>`; everything before it is the title/author/Article-Info header block.
- Heading 1 = style `Heading1` + `numPr numId=1` (auto "1."); back-matter Heading 1 has no `numPr`.
- Heading 2/3 = styles `Heading2`/`Heading3` with a Cambria `rFonts` override; numbers typed in the text.
- Body paragraph `<w:ind w:firstLine="720"/>`; captions `sz=16` centered; references `ind left=426 hanging=426`, `sz=16`.
- The even-page footer (`footer2.xml`) holds the running title and "(First Author)".
- If the author's edited copy of the template lacks the "INTRODUCTION (10 PT)" placeholder,
  build on the pristine bundled template and merge, rather than hand-patching XML.

---

## 10. Resources

- Author Guidelines: https://jurnal.polibatam.ac.id/index.php/JAIC/authorGuidelines
- Submissions & checklist: https://jurnal.polibatam.ac.id/index.php/JAIC/about/submissions
- Template 2027: https://docs.google.com/document/d/1sX-P19U60-hrDAWml5DeOyfhrTLlGjgn/edit
  (as .docx: replace `/edit` with `/export?format=docx`)
- Plagiarism policy: https://jurnal.polibatam.ac.id/index.php/JAIC/plagiarism
- Generative AI policy: https://jurnal.polibatam.ac.id/index.php/JAIC/ai
- Publication ethics: https://jurnal.polibatam.ac.id/index.php/JAIC/publication_ethics
- Focus & scope: https://jurnal.polibatam.ac.id/index.php/JAIC/focus-scoupe
- Zotero: https://www.zotero.org · DOI lookup: https://doi.org or https://search.crossref.org
- Grammarly: https://www.grammarly.com
- Contact: https://jurnal.polibatam.ac.id/index.php/JAIC/contact_us (editor email previously used: jaic.polibatam@gmail.com)

---

## Appendix A — `build_jaic_docx.py`

Tested 23 Nov 2026 against JAIC Paper Template 2027 (renders correctly in LibreOffice). Write it to disk unchanged when no bundled copy exists.

```python
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
```
