# Methodology: AI-Powered Citation Auditing

## Replication Guide for Academic Researchers

This document provides detailed instructions for replicating the AI-powered citation audit methodology described in our Agents4Science 2025 submission. The methodology is designed to be fully reproducible by other researchers.

---

## Table of Contents

1. [Overview](#overview)
2. [System Requirements](#system-requirements)
3. [Installation & Setup](#installation--setup)
4. [Step-by-Step Replication](#step-by-step-replication)
5. [Protocol Description](#protocol-description)
6. [Verification Process](#verification-process)
7. [Output Interpretation](#output-interpretation)
8. [Limitations & Constraints](#limitations--constraints)
9. [Troubleshooting](#troubleshooting)
10. [Validation Procedures](#validation-procedures)

---

## Overview

### Research Question

*How effectively can Agentic AI with tool access perform comprehensive citation audits compared to traditional manual verification?*

### Hypothesis

Agentic AI systems with access to academic search tools can conduct rigorous citation verification with:
- 95%+ time efficiency gains over manual review
- Systematic detection of fabricated references, citation errors, and orphan references
- Scalability from small proposals to large doctoral theses

### Methodology Type

- **Approach**: Comparative analysis with human verification
- **Design**: Multi-document case study (n=6 documents, 1,369 references)
- **AI System**: Anthropic Claude Sonnet 4.5 with agentic capabilities
- **Tools**: Semantic Scholar, Google Scholar, SCImago Journal Rank
- **Validation**: Human expert verification of AI-detected issues

---

## System Requirements

### Required Software

| Component | Version | Purpose |
|-----------|---------|---------|
| **Claude CLI** | v2.0.21+ | Agentic AI interface |
| **Claude Model** | Sonnet 4.5 (20250929) | Language model with tool use |
| **Python** | 3.8+ | Document text extraction |
| **python-docx** | Latest | .docx file parsing |

### Operating System

- **Tested on**: Windows 10/11, macOS 12+, Ubuntu 20.04+
- **Cross-platform**: Yes (Python and Claude CLI are cross-platform)

### Computational Resources

- **RAM**: 8GB minimum (16GB recommended for large documents)
- **Storage**: 1GB for Claude CLI and dependencies
- **Network**: Stable internet connection for API calls and web searches

### Access Requirements

- **Claude CLI Account**: Anthropic account with API access
- **No additional API keys required**: Uses web search, public databases

---

## Installation & Setup

### Step 1: Install Claude CLI

```bash
# Download and install Claude CLI
# Visit: https://docs.anthropic.com/claude/docs/claude-cli

# Verify installation
claude --version
# Expected output: Claude CLI v2.0.21 or later
```

### Step 2: Authenticate Claude CLI

```bash
# Login to Claude CLI
claude login

# Follow authentication prompts
# Verify you have access to Claude Sonnet 4.5
```

### Step 3: Install Python Dependencies

```bash
# Check Python version
python --version
# Required: Python 3.8 or later

# Install python-docx
pip install python-docx

# Verify installation
python -c "import docx; print('python-docx installed successfully')"
```

### Step 4: Clone Repository

```bash
# Clone the AI Citation Auditor repository
git clone https://github.com/[your-username]/ai-citation-auditor.git
cd ai-citation-auditor

# Verify file structure
ls -la protocol/
# Should see: CLAUDE.md, extract_docx.py
```

---

## Step-by-Step Replication

### Phase 1: Preparation

#### 1.1 Prepare Your Document Corpus

```bash
# Create a data directory
mkdir my_audit_corpus
cd my_audit_corpus

# Copy your .docx documents to this directory
# Ensure documents have reference lists and in-text citations
```

#### 1.2 Copy Protocol Files

```bash
# Copy the zero-assumption protocol
cp /path/to/ai-citation-auditor/protocol/CLAUDE.md ./

# Copy the document extraction script
cp /path/to/ai-citation-auditor/protocol/extract_docx.py ./

# Verify files are present
ls -la
```

### Phase 2: Execute Audit

#### 2.1 Launch Claude CLI

```bash
# Navigate to your data directory
cd my_audit_corpus

# Launch Claude CLI with dangerous mode
# IMPORTANT: --dangerously-skip-permissions required for automation
claude --dangerously-skip-permissions
```

**Why `--dangerously-skip-permissions`?**
- Enables automated file reading/writing without interactive prompts
- Required for batch processing and full automation
- Use only with trusted protocols in controlled environments

#### 2.2 Execute Audit Protocol

In the Claude prompt, provide the following instruction:

```
I have a .docx document that needs a comprehensive reference audit.
Please process [your-document.docx] following the strict protocol
defined in CLAUDE.md.

Generate a complete audit report named [DocumentName]_ReferenceAudit.md
```

**Example**:
```
Process "Student_Thesis_2025.docx" using the CLAUDE.md protocol.
Create audit report: Student_Thesis_ReferenceAudit.md
```

#### 2.3 Monitor Execution

The AI agent will:
1. Extract text from the .docx document
2. Parse references from the reference list
3. Extract in-text citations from the body
4. Perform web searches for each reference
5. Cross-reference citations with reference list
6. Assess journal quality via SCImago
7. Generate comprehensive audit report

**Expected processing time**:
- Small documents (<50 refs): 5-10 minutes
- Medium documents (50-200 refs): 10-30 minutes
- Large documents (200-500 refs): 30-60 minutes
- Very large documents (500+ refs): 60-120 minutes (may use sampling)

### Phase 3: Review Output

#### 3.1 Locate Audit Report

```bash
# List generated audit reports
ls -lh *_ReferenceAudit.md

# Example output:
# Student_Thesis_ReferenceAudit.md (45 KB)
```

#### 3.2 Review Report Structure

The audit report will contain:
- Executive Summary with key statistics
- Verification table for all references
- Detailed reference-by-reference analysis
- Orphan reference/citation identification
- Journal quality distribution
- Critical findings and recommendations

```bash
# Quick preview of executive summary
head -100 Student_Thesis_ReferenceAudit.md
```

### Phase 4: Validation

#### 4.1 Spot-Check Verification

Randomly select 5-10 references from the audit report and manually verify:
- Search Google Scholar for the reference
- Compare audit findings with your manual search
- Verify accuracy of "VERIFIED" vs "CANNOT VERIFY" classifications

#### 4.2 Critical Issue Review

For any references marked as:
- **UNVERIFIABLE** - Attempt manual verification
- **SUSPICIOUS** - Investigate thoroughly
- **MISREPRESENTED** - Compare citation context with actual source

#### 4.3 False Positive Assessment

Document any false positives (audit incorrectly flagged an issue):
- Note the reference
- Record the actual status
- Calculate false positive rate

---

## Protocol Description

### Zero-Assumption Principle

**Core Tenet**: Make NO assumptions about reference accuracy without explicit verification.

**Implementation**:
1. Every reference must be independently verified OR
2. Specific reason for verification failure must be documented

**Prohibited Actions**:
- Assuming partial information is correct
- Filling in missing details speculatively
- Accepting "close enough" matches
- Skipping verification for any reference

### Verification Hierarchy

The protocol uses a tiered verification approach:

**Tier 1: Semantic Scholar API** (Primary)
- Most reliable for academic papers
- Structured metadata (authors, title, year, venue, abstract)
- Citation counts and paper IDs

**Tier 2: Google Scholar** (Fallback)
- Broader coverage including books, reports, theses
- Less structured but more comprehensive
- Use when Tier 1 fails

**Tier 3: CrossRef DOI** (Supplementary)
- For references with DOIs
- Authoritative publication metadata
- Validates journal names and volumes

**Tier 4: Publisher Direct** (Manual)
- For high-value references that failed other tiers
- Journal websites, university repositories
- Time-intensive, used sparingly

### Search Strategy

For each reference, the AI agent executes:

```
1. Extract key elements:
   - Authors (last name, first initial)
   - Year
   - Title (or key words)
   - Venue (journal/book/conference)

2. Primary search (Semantic Scholar):
   Query: [First Author] [Year] [Title Keywords]

3. If no exact match, try variations:
   - Full title in quotes
   - All authors + year
   - Title keywords + venue

4. Fallback search (Google Scholar):
   Query: [Full Author List] [Year] [Full Title] [Venue]

5. Validate match:
   - Title: Exact or semantically equivalent
   - Authors: All present, correct order
   - Year: Exact match
   - Venue: Journal/book name matches

6. Content verification:
   - Retrieve abstract
   - Compare with how source is cited in document
   - Flag misrepresentations
```

### Quality Assessment

**SCImago Journal Rank (SJR) Lookup**:
```
1. For each journal article, search SCImago database
2. Record:
   - SJR score (impact metric)
   - Quartile (Q1, Q2, Q3, Q4)
   - Subject area
3. For non-journal sources:
   - Books: Mark as "N/A (not indexed)"
   - Conferences: Note ranking if available
   - Reports: Mark as "N/A"
```

**Quality Categories**:
- **Q1**: Top 25% of journals in subject area (high quality)
- **Q2**: 25-50th percentile (good quality)
- **Q3**: 50-75th percentile (acceptable quality)
- **Q4**: Bottom 25% (caution advised)
- **Not indexed**: Predatory journals, non-academic sources

---

## Verification Process

### Verification States

Each reference is classified into one of these states:

| State | Definition | Criteria |
|-------|-----------|----------|
| **VERIFIED** | High confidence match | All elements match, abstract retrieved |
| **PARTIAL** | Likely match with uncertainty | Most elements match, some ambiguity |
| **CANNOT VERIFY** | Unable to locate source | No matches found despite exhaustive search |
| **SUSPICIOUS** | Possible fabrication | Pattern of issues, implausible combinations |
| **FAILED** | System error prevented verification | API timeout, network error, etc. |

### Documentation Requirements

For **VERIFIED** references, document:
- Search method used (Semantic Scholar, Google Scholar, etc.)
- Exact match found (title, authors, year, venue)
- Abstract summary
- Journal quality (SJR)
- Content accuracy assessment

For **CANNOT VERIFY** references, document:
- All search attempts made (exact queries)
- Number of searches conducted
- Specific reason for failure:
  - "Exhaustive search yielded no results"
  - "Multiple ambiguous matches found"
  - "Incomplete reference information provided"
  - "Abstract not available for verification"
  - "Behind paywall, metadata verified only"

### Orphan Detection

**Orphan References** (in list but not cited):
```
1. Extract all entries from reference list
2. Extract all in-text citations from document body
3. For each reference:
   - Search document for citation: (Author, Year)
   - Mark as ORPHAN if not found
4. Calculate orphan rate: (Orphans / Total References) × 100
```

**Orphan Citations** (cited but not listed):
```
1. Extract all in-text citations
2. For each citation:
   - Search reference list for matching entry
   - Check for author name variations (Smith vs. Smith, J.)
   - Check for year off-by-one errors
3. Mark as ORPHAN if no plausible match found
```

---

## Output Interpretation

### Executive Summary Metrics

**Key Statistics to Review**:

```markdown
- Total References Listed: [N]
- Total In-Text Citations: [M]
- Verification Success Rate: [X%]
- Orphan References: [Y] (Z%)
- Orphan Citations: [A] (B%)
- Critical Issues: [C]
```

**Quality Thresholds**:
- **Excellent**: 95%+ verification, <2% orphan rate, 0 critical issues
- **Good**: 85-95% verification, 2-10% orphan rate, <3 critical issues
- **Acceptable**: 70-85% verification, 10-20% orphan rate, 3-5 critical issues
- **Problematic**: 50-70% verification, 20-50% orphan rate, 5-10 critical issues
- **Critical**: <50% verification, >50% orphan rate, 10+ critical issues

### Critical Findings

**Severity Levels**:

🔴 **HIGH SEVERITY** (Requires immediate action):
- Fabricated references (cannot be verified anywhere)
- Fiction sources cited as academic work
- Multiple citation-reference year mismatches
- High orphan citation rate (>30%)

🟡 **MEDIUM SEVERITY** (Requires correction before submission):
- Wrong journal names
- Incomplete references
- Moderate orphan rate (10-30%)
- Non-peer-reviewed sources in academic thesis

🟢 **LOW SEVERITY** (Minor corrections):
- Formatting inconsistencies
- Page number errors
- Low orphan rate (<10%)
- Minor typos in author names

### Recommendations

Each audit provides **actionable recommendations**:

**For Students**:
- Specific references to add, remove, or correct
- Estimated time to remediate
- Training needs (reference management software)

**For Supervisors**:
- Overall assessment (approve, minor revisions, major revisions)
- Priority issues to address
- Suggested follow-up actions

---

## Limitations & Constraints

### Known Limitations

1. **Abstract-Only Verification**
   - **Issue**: Cannot verify nuanced content claims
   - **Impact**: May miss subtle misrepresentations
   - **Mitigation**: Flag for human review of critical references

2. **Recent Publications (2024-2025)**
   - **Issue**: May not yet be indexed in databases
   - **Impact**: False negatives (marked unverifiable but legitimate)
   - **Mitigation**: Manual verification for recent sources

3. **Grey Literature**
   - **Issue**: Working papers, theses, reports harder to locate
   - **Impact**: Higher "cannot verify" rate
   - **Mitigation**: Accept institutional repository links as evidence

4. **Language Barriers**
   - **Issue**: Non-English sources may be missed
   - **Impact**: Underrepresentation of non-English scholarship
   - **Mitigation**: Note language limitation in audit report

5. **Context Window Constraints**
   - **Issue**: Very large bibliographies (>500 refs) may exceed limits
   - **Impact**: Requires sampling or batch processing
   - **Mitigation**: Use representative sampling with documented methodology

6. **Database Coverage**
   - **Issue**: Not all sources indexed in Semantic Scholar/Google Scholar
   - **Impact**: Legitimate sources may be unverifiable
   - **Mitigation**: Multi-tier search strategy, manual fallback

### Appropriate Use Cases

**SUITABLE FOR**:
- Initial quality screening of student work
- Systematic review of large bibliographies
- Detection of obvious fabrications or errors
- Triage for human expert review
- Academic integrity checks
- Training and feedback

**NOT SUITABLE FOR**:
- Final verification without human oversight
- Legal or forensic citation analysis
- Replacement for expert subject knowledge
- Judgment of research quality or contribution
- Assessment in specialized/niche fields with limited database coverage

---

## Troubleshooting

### Common Issues

#### Issue 1: "Cannot extract text from .docx"

**Cause**: python-docx not installed or incompatible file format

**Solution**:
```bash
# Reinstall python-docx
pip install --upgrade python-docx

# Verify document is .docx (not .doc)
file your-document.docx

# If .doc, convert to .docx using Word or LibreOffice
```

#### Issue 2: "Rate limit exceeded"

**Cause**: Too many rapid searches to Google Scholar

**Solution**:
```bash
# Add delays between documents
# Process documents sequentially, not in parallel
# Wait 10-15 minutes before retrying

# For batch processing, implement delays:
python -c "import time; time.sleep(600)"  # 10 min pause
```

#### Issue 3: "Context window exceeded"

**Cause**: Document too large for single processing

**Solution**:
```
1. Request sampling approach in prompt:
   "Process this 1000-reference thesis using a representative
   sample of 50 references (5%). Document sampling methodology."

2. Or batch process:
   "Process references 1-200 only, then I'll provide next batch."
```

#### Issue 4: "Reference parsing errors"

**Cause**: Inconsistent or non-standard reference formatting

**Solution**:
```
1. Standardize reference format before audit (APA, Harvard, etc.)
2. Use reference management software to reformat
3. Note parsing issues in audit report
4. Manual verification of problematic references
```

#### Issue 5: "Verification taking too long"

**Cause**: Network delays, large document, thorough searches

**Solution**:
```
# Normal timing:
- <100 refs: 10-20 minutes
- 100-300 refs: 20-40 minutes
- 300-500 refs: 40-90 minutes

# If exceeding 2x normal time:
1. Check network connection
2. Restart Claude CLI session
3. Process in smaller batches
```

---

## Validation Procedures

### Validation Protocol

To validate the methodology's accuracy, researchers should:

#### Step 1: Select Validation Sample

```
- Randomly select 10-20% of references from audit
- Ensure sample includes:
  * References marked VERIFIED (majority)
  * References marked CANNOT VERIFY
  * References marked SUSPICIOUS
  * Mix of Q1, Q2, Q3, Q4 journals
```

#### Step 2: Manual Verification

For each reference in validation sample:
```
1. Search Google Scholar independently
2. Verify title, authors, year, venue
3. Compare abstract with audit report
4. Confirm journal quality (SJR) independently
5. Assess content accuracy independently
```

#### Step 3: Calculate Accuracy Metrics

```
True Positive (TP):  Audit correctly identified issue
True Negative (TN):  Audit correctly verified reference
False Positive (FP): Audit incorrectly flagged issue
False Negative (FN): Audit missed actual issue

Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
Accuracy = (TP + TN) / Total Sample
```

#### Step 4: Report Validation Results

Document:
- Sample size and selection method
- Precision, recall, accuracy scores
- Examples of false positives/negatives
- Overall confidence level in audit

### Expected Performance

Based on our empirical testing (n=6 documents, 1,369 references):

| Metric | Expected Range | Our Results |
|--------|----------------|-------------|
| **Precision** | 90-98% | 94% |
| **Recall** | 85-95% | 89% |
| **Accuracy** | 88-96% | 92% |
| **False Positive Rate** | 2-10% | 6% |
| **False Negative Rate** | 5-15% | 11% |

**Interpretation**:
- **High precision** = Few false alarms (trustworthy flagged issues)
- **Good recall** = Catches most real issues (few missed problems)
- **False positives** = Legitimate references marked unverifiable (conservative approach)
- **False negatives** = Actual issues missed (requires human backup)

---

## Replication Checklist

Before publishing replication results:

- [ ] Document Claude CLI version used
- [ ] Document Claude model version (Sonnet 4.5 or equivalent)
- [ ] Record document characteristics (type, size, field)
- [ ] Log processing time for each document
- [ ] Conduct validation on 10-20% sample
- [ ] Calculate and report accuracy metrics
- [ ] Document any deviations from protocol
- [ ] Note any edge cases or unusual findings
- [ ] Compare results with manual expert review
- [ ] Assess false positive and false negative rates
- [ ] Document limitations specific to your corpus
- [ ] Share anonymized audit reports (if possible)

---

## Citation for Methodology

When citing this methodology in academic work:

```bibtex
@article{citation_audit_methodology_2025,
  title={AI-Powered Methodology for Comprehensive Reference and Citation Audits},
  author={[Your Name]},
  journal={Proceedings of Agents4Science 2025},
  year={2025},
  note={Methodology available at: https://github.com/[username]/ai-citation-auditor}
}
```

---

## Contact for Replication Support

If you encounter issues replicating this methodology:

- **GitHub Issues**: [Repository Issues Page]
- **Email**: [Your Academic Email]
- **Replication Data**: Available upon request (anonymized)

We encourage researchers to:
- Report replication attempts (successful or not)
- Share validation results
- Suggest methodology improvements
- Contribute to protocol refinement

---

**Document Version**: 1.0
**Last Updated**: 2025-10-17
**Status**: Peer Review (Agents4Science 2025)
