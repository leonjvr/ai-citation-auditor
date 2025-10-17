# Citation Audit Input Files

## Purpose

This directory contains prepared input files for systematic citation auditing using the **AI-Powered Citation Auditor** methodology described in the CLAUDE.md protocol.

## Contents

- **24 audit input files** (one per paper in validation dataset)
- **audit_batch_manifest.json** - Batch processing manifest
- **README.md** - This file

## Input File Format

Each `*_AuditInput.md` file contains:

1. **Document metadata** - Paper filename and reference count
2. **Complete reference list** - All extracted references from the paper
3. **Verification requirements** - Detailed checklist following CLAUDE.md protocol
4. **Output format specification** - Required audit report structure
5. **Strict verification standards** - Zero-assumption policy and marking criteria

## How to Use These Files

### Option 1: Manual Audit (Using Claude or ChatGPT with Agentic Mode)

1. Open one `*_AuditInput.md` file
2. Copy the entire content
3. Paste into Claude (Projects mode) or ChatGPT (with web search enabled)
4. The AI agent will systematically audit all references
5. Save the generated `*_ReferenceAudit.md` report

### Option 2: Batch Processing (Programmatic)

1. Load `audit_batch_manifest.json`
2. Iterate through each paper's input file
3. Submit to AI agent API with tool access (Semantic Scholar, Google Scholar, CrossRef)
4. Collect generated audit reports
5. Run aggregate statistics analysis

## Expected Output

For each input file, the audit process should generate:

- `[PaperName]_ReferenceAudit.md` - Comprehensive citation audit report
- Verification status for all references
- Quality metrics (SJR scores, quartiles)
- Critical findings (fabricated refs, misrepresentations)
- Recommendations for authors and supervisors

## Validation Metrics to Track

When running audits, track:

- **Verification rate**: % of references successfully verified
- **Time per paper**: How long each audit takes
- **Issue detection rate**: % of papers with critical issues
- **Fabricated reference detection**: Count of suspected fabrications
- **Quality distribution**: Q1/Q2/Q3/Q4 journal breakdown

## Next Steps

1. Run audits on all 24 papers
2. Collect audit reports in `../audit_reports/` directory
3. Run `statistics.py` to generate aggregate statistics
4. Analyze results for Agents4Science 2025 paper

---

**Protocol**: CLAUDE.md v1.0
**Methodology**: AI-Powered Citation Auditor
**Purpose**: Statistical validation for conference publication
