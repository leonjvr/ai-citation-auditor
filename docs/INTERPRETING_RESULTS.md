# Interpreting Audit Results

This guide helps you understand and act on the output from AI-Powered Citation Auditor reports.

## Table of Contents

1. [Understanding the Audit Report Structure](#understanding-the-audit-report-structure)
2. [Executive Summary Metrics](#executive-summary-metrics)
3. [Verification Status Codes](#verification-status-codes)
4. [Journal Quality Ratings](#journal-quality-ratings)
5. [Citation Status Categories](#citation-status-categories)
6. [Severity Classifications](#severity-classifications)
7. [Recommended Actions by Severity](#recommended-actions-by-severity)
8. [Common Patterns and What They Mean](#common-patterns-and-what-they-mean)

---

## Understanding the Audit Report Structure

Each audit report contains these sections in order:

### 1. Document Metadata
```markdown
**Document**: [Document Name]
**Audit Date**: 2025-10-17
**Total References**: 196
**Total Citations**: 103
**Citation Style**: APA 7th Edition
```

**What this tells you:**
- Basic document information
- Scale of the bibliography
- Whether citations and references are balanced

**Red flags:**
- Citations >> References (missing reference list entries)
- References >> Citations (orphan references, possible padding)

---

### 2. Executive Summary

```markdown
## Executive Summary

**Verification Success Rate**: 35%
**Critical Issues Detected**: 5 unverifiable references, 47 orphan citations, 163 orphan references
**Overall Assessment**: 🔴 MAJOR REVISION REQUIRED
**Estimated Remediation Time**: 40-60 hours
```

**Interpretation:**

| Metric | Meaning | Benchmark |
|--------|---------|-----------|
| **Verification Rate** | % of references successfully verified | >90% = Excellent, <50% = Critical |
| **Critical Issues** | Unverifiable refs, fabrications, mismatches | 0-2 = Normal, >5 = Concerning |
| **Overall Assessment** | Quality rating | 🟢 Ready, 🟡 Needs work, 🔴 Major issues |
| **Remediation Time** | Estimated hours to fix | <5hrs = Minor, >40hrs = Substantial |

---

### 3. Detailed Verification Table

```markdown
| Reference | Evidence from Google Scholar/Semantic Scholar | Accurate as cited? | Notes | Citation Status | Reference Quality (SJR) |
|-----------|----------------------------------------------|-------------------|-------|-----------------|------------------------|
| Teece et al. (1997) | Dynamic capabilities and strategic management... | ✅ Yes | Highly cited foundational work | ✅ Cited in text (p. 12) | Q1 (SJR: 8.6) |
| Perry Piscione (2025) | ❌ No results found in any database | ❌ Cannot verify | Potential fabrication - SSRN ID not found | ⚠️ Cited in text (p. 45) | Unknown |
```

**How to read each column:**

#### Reference
- Short form citation (Author, Year)
- Use to cross-reference with main document

#### Evidence
- Summary of what was found in academic databases
- Confirms the source exists and what it's about
- Look for: Match with your understanding of the source

#### Accurate as cited?
- ✅ Yes = Content matches how it's used in your document
- ⚠️ Partial = Source exists but minor discrepancies
- ❌ No = Content doesn't match or source not found

#### Notes
- Specific issues identified
- Explanations for verification failures
- Quality observations

#### Citation Status
- ✅ Cited in text = Properly integrated
- ⚠️ Orphan reference = Listed but never cited
- ⚠️ Orphan citation = Cited but not in reference list
- ❌ Mismatch = Citation doesn't match reference

#### Reference Quality (SJR)
- Q1 = Top 25% of journals in field (best)
- Q2 = 25-50th percentile
- Q3 = 50-75th percentile
- Q4 = Bottom 25% of journals
- N/A = Books, reports, not indexed

---

### 4. Orphan Analysis

```markdown
## Orphan References (listed but not cited)
**Count**: 163 out of 196 (83%)

Examples:
1. Porter, M. E. (1985). Competitive advantage...
2. Wernerfelt, B. (1984). A resource-based view...
[...]
```

**What this means:**

| Orphan Rate | Interpretation | Action Needed |
|-------------|----------------|---------------|
| **0-5%** | Normal - background reading | Acceptable as-is |
| **5-15%** | Some uncited sources | Consider citing or removing |
| **15-30%** | Concerning - possible padding | Review necessity of each |
| **30-50%** | Problematic | Remove or integrate most |
| **>50%** | Critical quality failure | Complete rewrite needed |

**Possible explanations:**
- Student read sources but didn't cite them (cite them!)
- Student padded bibliography to meet length requirements (remove them!)
- Student used reference management software incorrectly (clean it up!)

---

### 5. Quality Distribution

```markdown
## Journal Quality Distribution

| Quartile | Count | Percentage |
|----------|-------|------------|
| Q1 | 32 | 70% |
| Q2 | 8 | 17% |
| Q3 | 3 | 7% |
| Q4 | 1 | 2% |
| Not indexed | 2 | 4% |
```

**Interpretation:**

**Excellent Quality** (PhD/Top-tier publication):
- 60%+ Q1 journals
- <10% Q3/Q4 journals
- Mix of foundational classics and recent publications

**Good Quality** (Master's thesis/Journal article):
- 40-60% Q1 journals
- 20-30% Q2 journals
- <20% Q3/Q4 journals

**Acceptable** (Honours/Course paper):
- 20-40% Q1 journals
- Mix of Q1-Q3 acceptable
- Some non-indexed sources OK if appropriate

**Problematic**:
- <20% Q1 journals
- Majority Q3/Q4 or non-indexed
- Heavy reliance on websites, blogs, non-peer-reviewed sources

---

### 6. Critical Findings

```markdown
## Critical Findings

### Unverifiable References (5)
1. **Perry Piscione (2025)** - SSRN ID 9876543 not found in database
   - Exhaustive search yielded no results
   - Potential fabrication
   - **Action**: Request original PDF or remove

### Citation-Reference Mismatches (3)
1. **Chen et al. (2010)** → Should be Chen et al. (2007)
   - Year error (3-year discrepancy)
   - **Action**: Correct year in reference list
```

**Severity levels:**

**🔴 CRITICAL (immediate action required):**
- Fabricated references
- Fiction sources cited as academic
- Content misrepresentation
- Missing foundational citations

**🟡 HIGH PRIORITY:**
- Year mismatches
- Author name errors
- Journal name errors
- Missing key sources

**🟢 LOW PRIORITY:**
- Formatting inconsistencies
- Minor page number discrepancies
- Abbreviation variations

---

## Executive Summary Metrics

### Verification Success Rate

```
Verified references / Total references × 100%
```

**Quality benchmarks:**

| Rate | Interpretation | Typical Action |
|------|----------------|----------------|
| **95-100%** | Exceptional quality | Accept with minor formatting fixes |
| **85-95%** | High quality | Minor revisions (5-10 hours) |
| **70-85%** | Acceptable | Moderate revision (10-20 hours) |
| **50-70%** | Problematic | Substantial revision (20-40 hours) |
| **<50%** | Critical failure | Complete rewrite (40-60+ hours) |

**Factors affecting rate:**
- Document type (PhD expected higher than Honours)
- Field (STEM vs. humanities - different database coverage)
- Recency (2024-2025 publications harder to verify)
- Source types (grey literature reduces rate)

---

### Citation-Reference Balance

```
Citation count vs. Reference count
```

**Healthy patterns:**

**Research paper/thesis:**
- References ≈ Citations (most sources cited once)
- OK if References > Citations by 10-20% (background reading)

**Literature review:**
- Citations > References (sources cited multiple times)
- Normal pattern for review articles

**Red flags:**

**References >> Citations:**
- 50% more references than citations = Concerning
- 2× more references = Bibliography padding
- **Example**: 200 references, 100 citations = Problem

**Citations >> References:**
- More citations than references = Missing reference entries
- **Example**: 100 citations, 80 references = 20 missing entries

---

## Verification Status Codes

### ✅ VERIFIED
```
Evidence: Found in Semantic Scholar. "Dynamic capabilities and strategic
management." Strategic Management Journal, 18(7), 509-533.
Accurate as cited?: ✅ Yes
```

**Meaning:** Reference successfully confirmed in academic databases with matching metadata (title, authors, year, venue).

**Confidence level:** High - can proceed with confidence

---

### ⚠️ VERIFIED WITH DISCREPANCIES
```
Evidence: Found in Google Scholar. Year is 2007, not 2010 as cited.
Accurate as cited?: ⚠️ Partial - Year error
```

**Meaning:** Source exists but has minor errors in citation.

**Action required:** Correct the discrepancy (update year, author name, journal, etc.)

---

### ❌ UNVERIFIABLE - Exhaustive search yielded no results
```
Evidence: Searched Semantic Scholar, Google Scholar, CrossRef. No results found.
Accurate as cited?: ❌ Cannot verify
Notes: Potential fabrication
```

**Meaning:** Source cannot be located in any major academic database.

**Possible reasons:**
1. **Fabricated** - completely made up (most serious)
2. **Not yet published** - accepted but not yet online
3. **Grey literature** - institutional report, thesis, not indexed
4. **Paywalled** - exists but not visible to public search
5. **Error in citation** - so incorrect that search fails

**Action required:**
1. Request original PDF from student
2. Verify existence through other means (author website, institution)
3. If cannot verify → remove or replace

---

### ❌ UNVERIFIABLE - Multiple ambiguous matches found
```
Evidence: Found 5 different papers with similar titles by different authors.
Accurate as cited?: ❌ Cannot determine which is correct
Notes: Insufficient information to verify
```

**Meaning:** Citation information too vague to identify specific source.

**Action required:** Student must provide complete reference details (full title, all authors, volume/issue, DOI).

---

### ⚠️ FOUND BUT RETRACTED
```
Evidence: Found in Semantic Scholar. RETRACTED 2023 for data fabrication.
Accurate as cited?: ❌ No - Retracted publication
Notes: Must be removed immediately
```

**Meaning:** Source exists but has been retracted from literature.

**Action required:** Remove reference and find alternative source.

---

## Journal Quality Ratings

### SCImago Journal Rank (SJR) Interpretation

**Q1 (Top Quartile) - SJR typically 1.0+**
- Top 25% of journals in the field
- Examples: Strategic Management Journal (8.6), Academy of Management Journal (10.5)
- **Interpretation:** High-quality, rigorous peer review
- **Expected:** 40-70% of references in strong academic work

**Q2 (Second Quartile) - SJR 0.5-1.0**
- 25th-50th percentile
- Solid academic journals, good peer review
- **Interpretation:** Acceptable quality, credible sources
- **Expected:** 20-40% of references

**Q3 (Third Quartile) - SJR 0.2-0.5**
- 50th-75th percentile
- Emerging or specialized journals
- **Interpretation:** Use selectively, verify relevance
- **Expected:** <20% of references

**Q4 (Bottom Quartile) - SJR <0.2**
- Bottom 25% of journals
- May include predatory publishers
- **Interpretation:** Requires scrutiny
- **Expected:** <5% of references

**N/A (Not Indexed)**
- Books, conference proceedings, reports, theses
- **Interpretation:** Depends on source type
- Books from academic publishers = Good
- Grey literature, websites = Use sparingly

---

## Citation Status Categories

### ✅ Cited in text (p. 12)
**Meaning:** Reference properly integrated into the document.

**Example:**
> Reference list: Barney, J. B. (1991). Firm resources...
> In-text: "...as proposed by the resource-based view (Barney, 1991)..."

**Status:** ✅ Good - no action needed

---

### ⚠️ Orphan reference - listed but not cited
**Meaning:** Appears in reference list but never mentioned in document.

**Example:**
> Reference list: Porter, M. E. (1985). Competitive advantage...
> In-text: [No mention of Porter 1985 anywhere]

**Action required:**
1. **If relevant:** Add citation to appropriate section
2. **If not relevant:** Remove from reference list
3. **If background reading:** Cite in introduction/literature review

**Red flag:** >30% orphan references suggests padding

---

### ⚠️ Orphan citation - cited but not listed
**Meaning:** Cited in text but no reference list entry.

**Example:**
> In-text: "...as shown by Wernerfelt (1984)..."
> Reference list: [No Wernerfelt 1984 entry]

**Action required:** Add complete reference to reference list

**Common cause:** Reference management software error

---

### ❌ Citation-reference mismatch
**Meaning:** Information in citation doesn't match reference list.

**Example:**
> In-text: "...following Chen et al. (2010)..."
> Reference list: Chen, M. J., Su, K. H., & Tsai, W. (2007)...

**Action required:** Correct either the in-text citation or reference list entry to match.

**Types of mismatches:**
- Year errors (most common)
- Author name variations
- First author vs. et al. confusion

---

## Severity Classifications

### 🟢 EXCELLENT / APPROVE FOR SUBMISSION
**Characteristics:**
- 95-100% verification rate
- 0-2 minor issues (formatting only)
- <5% orphan references
- 60%+ Q1 journals
- 0 unverifiable references

**Example findings:**
> "Document F (Doctoral): 916 references, 100% verified (sample), 0.5% formatting issues only"

**Action:** Accept with cosmetic corrections only (30 minutes work)

---

### 🟢 HIGH QUALITY / ACCEPT WITH MINOR REVISIONS
**Characteristics:**
- 85-95% verification rate
- 2-5 minor issues
- 5-15% orphan references
- 40-60% Q1 journals
- 0-1 unverifiable references

**Example findings:**
> "Document B (Academic Paper): 65 references, 93% verified, 1 journal name error, 50 orphan references"

**Action:** Fix identified errors, consider citing or removing orphan references (2-4 hours work)

---

### 🟡 MODERATE / REQUIRES REVISION
**Characteristics:**
- 70-85% verification rate
- 5-10 moderate issues
- 15-30% orphan references
- 20-40% Q1 journals
- 1-3 unverifiable references

**Example findings:**
> "Document E: 19 references, 84% verified, 37% non-peer-reviewed, 3 unverifiable"

**Action:** Replace low-quality sources, verify unverifiable references, add peer-reviewed sources (10-20 hours work)

---

### 🟡 PROBLEMATIC / MAJOR REVISION
**Characteristics:**
- 50-70% verification rate
- 10-15 issues including serious errors
- 30-50% orphan references
- <20% Q1 journals
- 3-5 unverifiable references

**Example findings:**
> "Document C: 127 references, 60% verified, 1 fiction source, 5 unverifiable 2025 refs, 13 mismatches"

**Action:** Remove inappropriate sources (fiction!), correct all mismatches, verify recent publications (1-2 weeks work)

---

### 🔴 CRITICAL / COMPLETE REWRITE REQUIRED
**Characteristics:**
- <50% verification rate
- >15 critical issues
- >50% orphan references
- Mix of unverifiable and low-quality sources
- >5 potentially fabricated references

**Example findings:**
> "Document A (Masters): 196 references, 35% verified, 47 orphan citations, 163 orphan references (83%), 5 unverifiable"

**Action:** Complete rewrite of reference section required; student needs training in reference management (40-60 hours work)

---

## Recommended Actions by Severity

### For 🟢 EXCELLENT / HIGH QUALITY Documents

**Supervisor actions:**
1. Review flagged issues (usually <5)
2. Spot-check 5-10 randomly selected references manually
3. Approve for submission with minor corrections

**Student actions:**
1. Fix formatting issues
2. Correct identified errors (journal names, years)
3. Decision on orphan references: cite or remove
4. Final proofread

**Timeline:** 2-4 hours

---

### For 🟡 MODERATE Documents

**Supervisor actions:**
1. Review all flagged issues in detail
2. Manually verify unverifiable references
3. Discuss quality expectations with student
4. Schedule follow-up review after revisions

**Student actions:**
1. Correct all citation-reference mismatches
2. Verify or replace all unverifiable references
3. Cite orphan references or remove them
4. Add missing citations for orphan citations
5. Replace low-quality sources with peer-reviewed alternatives
6. Re-run audit after corrections

**Timeline:** 10-20 hours

---

### For 🟡 PROBLEMATIC / 🔴 CRITICAL Documents

**Supervisor actions:**
1. Meet with student to discuss citation practices
2. Provide training on reference management software
3. Review research strategy and literature search methods
4. Set clear quality expectations
5. Require multiple revision rounds with audits

**Student actions:**
1. **PRIORITY**: Remove any fiction sources or clearly fabricated references
2. Provide original PDFs for all unverifiable references
3. Correct ALL citation-reference mismatches
4. Remove or properly cite all orphan references
5. Add complete references for all orphan citations
6. Replace non-peer-reviewed sources with academic sources
7. Improve journal quality distribution (target 40%+ Q1)
8. Consider complete rewrite of literature review if >80% orphan references
9. Learn to use reference management software (Zotero, Mendeley, EndNote)
10. Re-run audit multiple times during revision process

**Timeline:** 1-2 weeks (Problematic) to 40-60 hours (Critical)

---

## Common Patterns and What They Mean

### Pattern 1: High orphan reference rate (>50%)

**What it suggests:**
- Bibliography padding to meet length requirements
- Student read sources but didn't integrate them
- Copy-paste from reference management software without curation

**Actions:**
- Review each orphan reference for relevance
- If relevant → cite in text
- If not relevant → remove
- If >80% orphans → likely needs complete rewrite

---

### Pattern 2: Cluster of unverifiable 2024-2025 references

**What it suggests:**
- Student citing very recent publications not yet indexed
- Potential fabrication (if >5 from same year)
- Pre-prints or working papers

**Actions:**
- Request original PDFs
- Check author websites, institutional repositories
- Verify pre-prints have been published
- If cannot verify → replace with established sources

---

### Pattern 3: Many citation-reference year mismatches

**What it suggests:**
- Manual entry errors
- Reference management software issues
- Student citing from memory, not from original source

**Actions:**
- Correct all year mismatches
- Verify student has original sources
- Train on proper citation practices

---

### Pattern 4: Mix of very old (>20 years) and very new (<2 years) with nothing in between

**What it suggests:**
- Incomplete literature review
- Missing recent developments in field
- Over-reliance on foundational works

**Actions:**
- Add sources from past 5-10 years
- Demonstrate evolution of field
- Balance classic and contemporary sources

---

### Pattern 5: Heavy use of non-peer-reviewed sources (websites, blogs, LinkedIn)

**What it suggests:**
- Insufficient academic literature search
- Misunderstanding of source quality expectations
- Practitioner-focused rather than research-focused

**Actions:**
- Replace with peer-reviewed alternatives
- Use websites only for data, not theory
- Improve database search skills

---

### Pattern 6: Duplicate references with slight variations

**What it suggests:**
- Reference management software imported same source multiple times
- Student didn't notice duplicates

**Actions:**
- Merge duplicate entries
- Keep version with most complete information
- Update all in-text citations to reference single entry

---

## Using Audit Results for Learning

### For Students

**Green/Yellow flags (minor issues):**
- Review errors to understand citation accuracy requirements
- Learn from mistakes (year errors, journal names, author names)
- Improve reference management practices

**Red flags (major issues):**
- Reassess research strategy
- Seek training on literature searches
- Learn to use reference management software
- Understand difference between peer-reviewed and non-peer-reviewed sources

---

### For Supervisors

**Use audit results to:**
- Identify students needing additional support
- Provide objective, evidence-based feedback
- Set clear quality benchmarks
- Track improvement over multiple drafts
- Demonstrate importance of citation accuracy

**Feedback approach:**
- Frame as quality improvement, not punishment
- Focus on learning from errors
- Provide resources (reference management training, database tutorials)
- Set realistic timelines for revision based on severity

---

## Questions to Ask When Interpreting Results

1. **Is the verification rate appropriate for this document type?**
   - PhD/Journal article: Expect 85-95%+
   - Master's: Expect 70-85%
   - Honours: Expect 60-75%

2. **Are unverifiable references truly fabricated or just hard to find?**
   - Check manually before accusing fabrication
   - Provide opportunity for student to provide evidence

3. **Is the orphan rate acceptable given the document type?**
   - Literature review: Higher acceptable
   - Empirical study: Should be low (<10%)

4. **Does journal quality match expectations for this level?**
   - PhD: 60%+ Q1
   - Master's: 40%+ Q1
   - Honours: 20%+ Q1

5. **Are errors systematic (suggesting lack of knowledge) or random (suggesting carelessness)?**
   - Systematic → training needed
   - Random → more careful proofreading needed

---

**Last Updated**: 2025-10-17
**Version**: 1.0.0

**Next Steps:**
- See TROUBLESHOOTING.md for resolving specific issues
- See BEST_PRACTICES.md for improving citation quality
- See example reports in audit-reports/ directory
