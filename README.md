# jaic-writing — Agent Skill for JAIC manuscripts

An [Agent Skills](https://agentskills.io) skill for writing, formatting and checking manuscripts for the
**Journal of Applied Informatics and Computing (JAIC)**, Politeknik Negeri Batam (e-ISSN 2548-6861).

Rules verified against the JAIC Author Guidelines and **JAIC Paper Template 2027** (23 Nov 2026).

## What it does
- Drafts and reviews manuscripts in the JAIC IMRaD structure (title ≤ 10 words, abstract 100–200 words, 5 keywords)
- Writes the mandatory back matter: Funding, CRediT author contributions, Conflict of Interest, Data & Code Availability, Generative-AI declaration
- Checks IEEE references (≥ 15, ≥ 60 % journals) plus stricter rules: verified DOI, no preprints, ≥ 50 % from the last 5 years
- Generates a `.docx` on the official JAIC Paper Template 2027 with `scripts/build_jaic_docx.py`

## Install
With the [skills CLI](https://github.com/vercel-labs/skills) (Claude Code, Codex, Cursor, Gemini CLI, Copilot, …):

```bash
npx skills add ekorudiawan/jaic-writing
```

Or copy `skills/jaic-writing/` into your agent's skills folder, e.g. `~/.claude/skills/`, `.agents/skills/`, `~/.cursor/skills/` or `~/.gemini/skills/`.

## Requirements for .docx generation
Python 3 (standard library only). The script uses the official template, downloaded once:

```bash
curl -L -o JAIC_Paper_Template_2027.docx \
  "https://docs.google.com/document/d/1sX-P19U60-hrDAWml5DeOyfhrTLlGjgn/export?format=docx"
python3 skills/jaic-writing/scripts/build_jaic_docx.py content.json out.docx --template JAIC_Paper_Template_2027.docx
```

The template belongs to JAIC and is not redistributed here.

## License
MIT — see [LICENSE](LICENSE). Journal templates are not included and remain the property of their journals.

## Author
Eko Rudiawan Jamzuri — Politeknik Negeri Batam
