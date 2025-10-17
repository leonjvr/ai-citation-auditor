# Example Audit Reports

This directory contains **anonymized, sanitized examples** of comprehensive reference audits conducted using the AI-Powered Citation Auditor methodology.

## Important Privacy Notice

⚠️ **All reports in this directory have been anonymized to protect student privacy:**
- Student names removed or pseudonymized
- Institution identifiers removed
- Supervisor names removed
- Document-specific titles generalized
- Sensitive content redacted

**Original student documents and personally identifiable audit reports are NEVER committed to this repository.**

---

## Available Examples

### 1. MASTER_AUDIT_SUMMARY.md
**Overview of batch processing results**
- Summarizes 6 documents (1,369 total references)
- Demonstrates range from excellent to critical quality
- Provides aggregate statistics and patterns
- **Use for**: Understanding methodology performance across diverse documents

### 2. Example_Excellent_Quality.md
**Best case scenario: Doctoral thesis**
- 916 references audited
- 100% verification success rate (sample)
- Only 0.5% minor formatting issues
- Demonstrates high-quality citation practices
- **Use for**: Setting quality benchmarks, understanding best practices

### 3. Example_High_Quality.md
**Minor corrections needed: Academic paper**
- 65 references audited
- 93% citation matching rate
- Predominantly Q1 journals
- Few easily correctable errors
- **Use for**: Understanding acceptable quality with minor issues

### 4. Example_Critical_Issues.md
**Worst case scenario: MCom dissertation**
- 196 references listed
- 35% citation matching rate
- 83% orphan references
- 5 unverifiable/potentially fabricated sources
- 47 orphan citations
- **Use for**: Identifying severe quality control failures, training examples

---

## Report Structure

Each audit report follows this structure:

### 1. Document Metadata
- Document title (anonymized)
- Audit date
- Total references and citations
- Citation style

### 2. Executive Summary
- Key statistics (verification rate, orphan rate, critical issues)
- Overall quality assessment
- Severity rating

### 3. Detailed Verification Table
- Reference-by-reference verification status
- Evidence from Semantic Scholar/Google Scholar
- Accuracy assessment
- Journal quality (SJR)
- Citation status

### 4. Orphan Analysis
- Orphan references (listed but not cited)
- Orphan citations (cited but not listed)
- Citation-reference mismatches

### 5. Quality Distribution
- Journal quartile breakdown (Q1, Q2, Q3, Q4)
- Average SJR scores
- Non-indexed sources

### 6. Critical Findings
- Fabricated/unverifiable references
- Misrepresented sources
- Low-quality sources
- Formatting errors

### 7. Recommendations
- Specific actions for student
- Guidance for supervisor
- Estimated remediation time
- Training needs

---

## Using These Examples

### For Researchers
- **Understand methodology output** - See what comprehensive audits look like
- **Validate your own results** - Compare your audit outputs with these examples
- **Assess quality range** - Understand spectrum from excellent to critical
- **Benchmark performance** - Use as reference points for your corpus

### For Educators/Supervisors
- **Set expectations** - Show students what quality audits reveal
- **Training materials** - Use as case studies in academic integrity workshops
- **Quality benchmarks** - Establish standards for acceptable citation practices
- **Feedback examples** - Model how to provide constructive citation feedback

### For Students
- **Self-assessment** - Compare your work against quality examples
- **Learning tool** - Understand what constitutes good vs. poor citation practices
- **Error patterns** - Recognize common mistakes to avoid
- **Quality standards** - Internalize expectations for academic citation

---

## Statistics Summary

| Document | Type | Refs | Verification | Orphan Refs | Orphan Cites | Quality |
|----------|------|------|--------------|-------------|--------------|---------|
| **Excellent** | PhD Thesis | 916 | 100% (sample) | Minimal | 0 | 🟢 Q1-heavy |
| **High Quality** | Paper | 65 | 93% | 77% | 7% | 🟢 Q1-heavy |
| **Critical** | MCom | 196 | 35% | 83% | 46% | 🔴 Mixed/Unverifiable |

**Key Insight**: The methodology effectively stratifies document quality, from publication-ready (Excellent) to requiring complete rewrite (Critical).

---

## Ethical Considerations

### Why Anonymization Matters
- Protects student privacy and dignity
- Allows sharing of findings without stigma
- Focuses on methodology, not individual judgment
- Enables reproducibility without compromising confidentiality

### What Was Anonymized
- **Student names** → "Student A", "Author"
- **Supervisor names** → Removed entirely
- **Institution** → Removed or generalized
- **Document titles** → Generic titles (e.g., "MCom Strategic Management")
- **Specific research topics** → Retained only for context
- **Personal identifiers** → Stripped from all text

### Original Purpose
These audits were conducted as formative feedback for students, not as punitive measures. The goal is quality improvement and learning, not exposure of errors.

---

## Interpreting Audit Results

### Verification Success Rate
- **95-100%**: Excellent - minimal issues
- **85-95%**: Good - minor corrections needed
- **70-85%**: Acceptable - moderate revision required
- **50-70%**: Problematic - substantial revision needed
- **<50%**: Critical - major rewrite required

### Orphan Reference Rate
- **<5%**: Excellent management
- **5-15%**: Acceptable (some uncited background reading)
- **15-30%**: Concerning (possible padding)
- **30-50%**: Problematic (clear padding or poor integration)
- **>50%**: Critical (severe quality control failure)

### Critical Issues
- **0 unverifiable**: Clean audit
- **1-2 unverifiable**: Investigate but likely acceptable
- **3-5 unverifiable**: Concerning pattern
- **5+ unverifiable**: Serious integrity concerns requiring investigation

---

## Replication Notes

These examples are provided to support methodology replication. When conducting your own audits:

1. **Follow the protocol strictly** - See `protocol/CLAUDE.md`
2. **Document all search attempts** - Transparency is key
3. **Use zero-assumption approach** - Never guess or assume
4. **Validate with human review** - AI is a screening tool, not final arbiter
5. **Maintain anonymity** - If sharing results, protect identities

---

## Additional Resources

- **Protocol**: See `/protocol/CLAUDE.md` for complete methodology
- **Replication Guide**: See `/METHODOLOGY.md` for step-by-step instructions
- **Citation**: See `/CITATION.md` for how to cite this work
- **Support**: See main README.md for contact and troubleshooting

---

## Contributions

Have you conducted audits using this methodology? Consider contributing anonymized examples:

1. Anonymize thoroughly (remove ALL identifiable information)
2. Verify anonymization with a colleague
3. Submit via pull request with description
4. Include consent if original author approves sharing

**Guidelines for submissions**:
- Must be fully anonymized
- Must follow the standard audit report format
- Should represent interesting cases (not duplicative)
- Include brief context (document type, field, size)

---

**Note**: These examples represent a snapshot of methodology performance as of October 2025. As the protocol evolves, newer examples may be added. Always refer to the latest protocol version in `/protocol/CLAUDE.md`.

**Privacy Commitment**: No original student documents or personally identifiable audit reports are ever committed to this public repository. Only anonymized, educational examples are shared.
