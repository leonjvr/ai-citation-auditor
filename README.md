# AI-Powered Citation Auditor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude CLI](https://img.shields.io/badge/Claude%20CLI-v2.0.21-blue.svg)](https://docs.anthropic.com/claude/docs/claude-cli)
[![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)](https://github.com)

> A rigorous, AI-powered methodology for conducting comprehensive reference and citation audits in academic manuscripts using Agentic AI with tool access.

## ⚠️ Important Disclaimer

**This repository contains methodology validation data, NOT evaluations of specific papers or authors.**

The validation dataset includes AI-generated audit reports on 24 open-access academic papers. These reports:
- Are **methodology demonstrations** showing the AI tool's capabilities
- Were generated to **validate the auditing technique**, not to assess the papers themselves
- Involved only **sample-based human verification** by researchers
- May contain errors (false positives/negatives) inherent to AI systems

**We make NO claims about the quality of any specific paper or author's work.** See [`DISCLAIMER.md`](DISCLAIMER.md) for full legal and ethical disclaimers.

## Overview

This repository contains a **zero-assumption protocol** for systematic citation verification in academic work, developed as part of research on AI agents in scholarly quality assurance. The methodology employs Agentic Generative AI with access to academic search tools to detect fabricated references, citation errors, orphan references, and content misrepresentation.

**Key Features:**
- 🔍 **Systematic verification** of references against Semantic Scholar, Google Scholar, and academic databases
- 🚫 **Zero-assumption policy** - explicitly documents when verification fails and why
- 📊 **Comprehensive reporting** with verification status, journal quality (SJR), and actionable recommendations
- ⚡ **Time-efficient** - processes 100+ references in ~10 minutes vs. months of manual review
- 🎯 **Detection capabilities** - identifies fabricated sources, citation-reference mismatches, orphan references/citations
- 📈 **Scalable** - tested on documents from 19 to 916 references

## Current Status & Research Context

**Project Status:**
- **Software Version**: v1.0.0 (stable, functional, tested)
- **Conference Submission**: Prepared for Agents4Science 2025 conference
- **Empirical Validation**: Completed on 30 documents, 2,581 references across two validation phases
- **Replication**: Full methodology documented and open source
- **Future Work**: Extended validation, Zenodo DOI, potential journal submission

This methodology was developed for academic conference submission and has been empirically tested across diverse academic contexts in two phases:

**Phase 1 - Initial Validation (6 documents):**
- **1 Honours project** (19 references)
- **3 Masters dissertations** (65-196 references)
- **1 Conference paper** (46 references)
- **1 Doctoral thesis** (916 references)

**Phase 2 - Extended Validation (24 documents):**
- **24 PLOS open-access papers** spanning 5 disciplines:
  - Machine Learning & AI (5 papers)
  - Psychology & Education (7 papers)
  - Economics & Social Science (4 papers)
  - Biology & Genetics (5 papers)
  - Climate Science & Public Health (3 papers)
- **1,212 references** extracted and verified
- **Multi-disciplinary representation** ensuring methodology robustness

**Combined Empirical Results:**
- **Best case**: 100% verification rate (excellent citation practices)
- **Worst case**: 83% of references rejected (orphan references, fabricated sources)
- **Phase 1 average**: 76.8% verification rate
- **Phase 2 average**: 91.7% verification rate
- **Critical issues detected**: Fabricated references, retracted articles, predatory journals, citation-reference mismatches

## Quick Start

### Prerequisites

- **Claude CLI v2.0.21** or later
- Python 3.8+ with `python-docx` library
- Academic document in .docx format

### Installation

```bash
# Clone the repository
git clone https://github.com/leonjvr/ai-citation-auditor.git
cd ai-citation-auditor

# Install Python dependencies
pip install python-docx

# Install Claude CLI (if not already installed)
# Follow instructions at: https://docs.anthropic.com/claude/docs/claude-cli
```

### Basic Usage

```bash
# Navigate to your data directory
cd /path/to/your/documents

# Copy the protocol file
cp /path/to/ai-citation-auditor/protocol/CLAUDE.md ./

# Run Claude CLI with dangerous mode (required for full automation)
claude --dangerously-skip-permissions

# In Claude prompt, request citation audit:
# "Process [document-name].docx using the CLAUDE.md protocol"
```

The system will generate a comprehensive audit report: `[DocumentName]_ReferenceAudit.md`

## Methodology

### Zero-Assumption Protocol

The core principle is **making NO assumptions** about reference accuracy. Every reference must be independently verified or marked with a specific reason for failure.

**Verification Process:**

1. **Extract** all references from the document's reference list
2. **Extract** all in-text citations from the document body
3. **Cross-reference** to identify orphan references and citations
4. **Verify** each reference independently via:
   - Semantic Scholar API
   - Google Scholar search
   - CrossRef DOI lookup
   - Publisher websites
5. **Assess** content accuracy against how sources are cited
6. **Evaluate** journal quality via SCImago Journal Rank (SJR)
7. **Report** with full transparency and actionable recommendations

### Verification Standards

A reference is marked as **VERIFIED** only when:
- Title matches exactly (or semantically equivalent)
- All authors confirmed (names and order)
- Publication year matches
- Venue (journal/book/conference) matches
- Abstract or key findings retrieved

**If verification fails**, the protocol requires documenting the **specific reason**:
- "Exhaustive search yielded no results"
- "Multiple ambiguous matches found"
- "Incomplete reference information provided"
- "Abstract not available for content verification"
- "Source identified but behind paywall"

### Output Format

Each audit generates a structured markdown report with:

- **Executive Summary** - Key statistics and critical issues
- **Verification Table** - Status, evidence, accuracy, journal quality for each reference
- **Detailed Analysis** - Reference-by-reference deep dive
- **Orphan Analysis** - References not cited, citations not referenced
- **Quality Distribution** - Journal quartile breakdown
- **Critical Findings** - Fabricated references, misrepresentations, low-quality sources
- **Recommendations** - Specific, actionable remediation steps

See [`examples/`](examples/) for sample audit reports.

## Repository Structure

```
ai-citation-auditor/
├── README.md                          # This file
├── DISCLAIMER.md                      # Legal and ethical disclaimers
├── METHODOLOGY.md                     # Detailed methodology and replication guide
├── VALIDATION_STATUS.md               # Validation dataset progress tracking
├── CITATION.md                        # How to cite this work
├── LICENSE                            # MIT License
├── protocol/
│   ├── CLAUDE.md                      # Core zero-assumption protocol
│   └── extract_docx.py               # Python script for .docx text extraction
├── audit-reports/                     # Phase 1 audit reports (6 documents)
│   ├── MASTER_AUDIT_SUMMARY.md       # Overview of 6-document batch
│   └── [Individual audit reports]    # Initial validation audits
├── validation_audits/                 # Phase 1 raw validation data
│   └── [Student project audits]      # Honours, Masters, Doctoral audits
├── analysis/                          # Validation dataset (Phase 2)
│   ├── audit_reports/                # 24 PLOS paper audits
│   ├── extracted_references/         # Extracted reference data (24 files)
│   ├── audit_inputs/                 # Prepared audit input files
│   ├── COMPREHENSIVE_VALIDATION_REPORT.md  # Complete validation analysis
│   ├── aggregate_statistics.md       # Statistical summary
│   ├── aggregate_statistics.json     # JSON export of metrics
│   ├── collect_papers.py             # Paper collection script
│   ├── download_papers.py            # PDF download script
│   ├── extract_references.py         # Reference extraction script
│   ├── prepare_audit_inputs.py       # Audit input preparation
│   ├── run_all_audits.py             # Batch processing plan
│   └── statistics.py                 # Aggregate statistics calculator
├── datasets/
│   ├── validation_dataset.json       # Dataset metadata (24 papers)
│   └── README.md                     # Dataset documentation
├── examples/                          # Sample data and demonstrations
│   └── sample_references.md          # Example reference formats
└── docs/                              # Additional documentation
    ├── TROUBLESHOOTING.md            # Common issues and solutions
    ├── INTERPRETING_RESULTS.md       # How to read audit reports
    └── BEST_PRACTICES.md             # Recommendations for supervisors
```

## Key Findings

### Detection Capabilities

The methodology successfully detected:

| Issue Type | Count | Example |
|------------|-------|---------|
| **Fabricated references** | 8 | SSRN ID not found in database |
| **Fiction sources** | 1 | Marvel Comics novel cited as academic work |
| **Citation-reference mismatches** | 16+ | Year errors, author name variations |
| **Orphan references** | 225 | Listed but never cited (up to 83% of list) |
| **Orphan citations** | 48 | Cited but missing from reference list |
| **Journal name errors** | 5 | Wrong journal name in citation |
| **Duplicate references** | 8 | Same source listed multiple times |

### Time Efficiency

| Document Size | Traditional Review | AI-Powered Audit | Time Savings |
|--------------|-------------------|------------------|--------------|
| 19 references | 2-4 hours | ~5 minutes | 95%+ |
| 100 references | 1-2 days | ~10 minutes | 98%+ |
| 916 references | Weeks-Months | ~90 minutes | 99%+ |

### Quality Stratification

The methodology effectively stratifies document quality:

- **Excellent** (100% verified, <1% issues) - Ready for submission
- **High Quality** (85-95% verified, minor errors) - Minor revisions needed
- **Moderate** (60-85% verified, several issues) - Substantial revision required
- **Critical** (35-60% verified, major issues) - Complete rewrite needed

## Use Cases

### For Supervisors and Educators

- **Proactive screening** - Run audits at proposal stage, not final submission
- **Quality triage** - Identify high-risk students early
- **Time efficiency** - Reduce manual verification burden
- **Objective feedback** - Provide evidence-based recommendations

### For Students and Researchers

- **Self-audit** - Quality-check your work before submission
- **Learning tool** - Understand citation accuracy requirements
- **Integrity check** - Verify reference management software output
- **Competitive advantage** - Ensure highest citation standards

### For Institutions

- **Quality assurance** - Systematic review of theses/dissertations
- **Training programs** - Demonstrate proper citation practices
- **Academic integrity** - Early detection of problematic sources
- **Writing center support** - Scale citation assistance services

## Limitations

This methodology has important limitations:

1. **Abstract-only verification** - Cannot verify nuanced content claims requiring full-text analysis
2. **Recent publications** - 2024-2025 references may not yet be indexed
3. **Grey literature** - Working papers, theses, reports harder to verify
4. **Language barriers** - Non-English sources may be missed
5. **Context windows** - Large bibliographies (>500 refs) may require sampling
6. **Database coverage** - Sources not in Semantic Scholar/Google Scholar cannot be verified

**Important**: This is a **screening tool**, not a replacement for human expert review. Supervisors should use it for triage and initial quality assessment, followed by detailed human verification of flagged issues.

## Ethical Considerations

### Academic Integrity

- Tool detects potential issues but does not make definitive judgments
- "Unverifiable" ≠ "fabricated" - legitimate reasons for verification failure exist
- Students should be given opportunity to explain and correct issues
- Focus on constructive feedback, not punishment

### Transparency

- All search attempts documented
- All limitations explicitly stated
- No "black box" decisions - full audit trail provided
- Conservative assessments when uncertain

### Privacy

- Audit reports focus on reference quality, not student competence
- Language is objective, not judgmental
- Suitable for formative feedback and quality improvement

## Contributing

This is a research project developed for academic purposes. Contributions, suggestions, and feedback are welcome:

- **Issues** - Report bugs or suggest improvements
- **Examples** - Share your audit results (anonymized)
- **Extensions** - Propose methodology enhancements
- **Replication** - Document your replication attempts

## Citation

If you use this methodology in your research, please cite:

```bibtex
@software{ai_citation_auditor_2025,
  author = {Janse van Rensburg, LJ and orcid:0000-0002-0104-2865},
  title = {AI-Powered Citation Auditor: A Zero-Assumption Protocol for Reference Verification},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/leonjvr/ai-citation-auditor},
  note = {Research on AI-powered reference verification methodology}
}
```

**Conference Paper** (under review):
```
Janse van Rensburg, LJ. (2025). AI-Powered Methodology for Comprehensive Reference
and Citation Audits in Academic Manuscripts. [Manuscript under review for conference
proceedings].
```

**Note**: Conference paper citation will be updated upon acceptance and publication.

See [`CITATION.md`](CITATION.md) for additional citation formats.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Technical Details

### System Requirements

- **Claude CLI**: v2.0.21 or later
- **Claude Model**: Sonnet 4.5 (claude-sonnet-4-5-20250929) or equivalent
- **Python**: 3.8+ with `python-docx` library
- **Operating System**: Cross-platform (tested on Windows, macOS, Linux)
- **Permissions**: Requires `--dangerously-skip-permissions` flag for automated processing

### API Access

The methodology uses web search and does not require direct API keys for:
- Semantic Scholar (rate-limited public access)
- Google Scholar (search via web)
- SCImago Journal Rank (public database)
- CrossRef (open API)

**Note**: Heavy usage may hit rate limits; implement delays if processing many documents.

## Acknowledgments

- Powered by **Anthropic Claude** (Sonnet 4.5)
- Built on **Claude CLI v2.0.21**
- Tested on academic documents from the University of Johannesburg

## Contact

For questions, collaboration, or replication support:

- **GitHub Issues**: [github.com/leonjvr/ai-citation-auditor/issues](https://github.com/leonjvr/ai-citation-auditor/issues)
- **GitHub**: [@leonjvr](https://github.com/leonjvr)

---

**Version**: 1.0.0
**Last Updated**: 2025-10-17
**Status**: Active Research Project
