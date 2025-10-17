# Reference Checking Protocol for Academic Documents

## Objective

Conduct rigorous, systematic reference checking of academic documents with **absolute strictness and zero tolerance for assumptions**. Each reference must be independently verified against authoritative sources. Any inability to verify must be explicitly documented with clear reasoning.

## Core Principles

### 1. Zero Assumptions Policy
- **NEVER** assume a reference is correct without verification
- **NEVER** fill in missing information speculatively
- **NEVER** accept partial matches as verification
- **ALWAYS** document why verification failed or is incomplete

### 2. Verification Sources (In Order of Priority)
1. **Semantic Scholar API** - Primary source for academic papers
2. **Google Scholar** - Secondary source for broader coverage
3. **CrossRef DOI lookup** - For DOI-based verification
4. **Publisher websites** - Direct verification when available

### 3. Verification Requirements
A reference is considered "VERIFIED" only when:
- Title matches exactly (or with minor punctuation differences)
- All authors are confirmed (order and names)
- Publication year matches
- Publication venue (journal/book/conference) matches
- Abstract or key findings can be retrieved

## Reference Checking Process

### Step 1: Extract Complete Reference List
1. Extract ALL references from the document's reference section
2. Create a structured list with each reference as a separate entry
3. Note any formatting inconsistencies or incomplete references
4. Identify the citation style used (APA, Harvard, Chicago, etc.)

### Step 2: Extract All In-Text Citations
1. Scan entire document for in-text citations
2. Document format of citations (author-year, numeric, footnotes)
3. Create comprehensive list of all cited works in the body

### Step 3: Cross-Reference Analysis
1. Match each reference list entry to in-text citations
2. Identify **orphan references** (in list but not cited in text)
3. Identify **orphan citations** (cited in text but not in reference list)
4. Document any discrepancies (year mismatches, author name variations)

### Step 4: Independent Verification
For each reference, perform the following:

#### A. Search Strategy
1. Search Semantic Scholar using exact title
2. If not found, search using author + year + key title words
3. Verify on Google Scholar as backup
4. Check DOI if provided

#### B. Verification Checklist
- [ ] Title confirmed (exact or semantically identical)
- [ ] Authors confirmed (all names, correct order)
- [ ] Year confirmed
- [ ] Publication venue confirmed (journal name, volume, issue, pages)
- [ ] Abstract or summary retrieved
- [ ] Content relevance assessable

#### C. Documentation Requirements
For each reference, document:
- **What was found**: Exact details from verification source
- **What matches**: Specific elements that align with cited reference
- **What differs**: Any discrepancies, even minor ones
- **Confidence level**: HIGH (all elements verified), MEDIUM (minor uncertainty), LOW (significant gaps), FAILED (cannot verify)

### Step 5: Content Verification
When abstract or content is available:
1. Read and summarize the source's key findings/arguments
2. Compare against how the source is cited in the document
3. Assess whether citation accurately represents the source
4. Flag any misrepresentations, oversimplifications, or distortions

### Step 6: Quality Assessment
For each verified journal article:
1. Search SCImago Journal Rank (SJR) database
2. Record SJR score and quartile (Q1, Q2, Q3, Q4)
3. Note journal subject area and category
4. For books, reports, theses: Mark as "N/A (not indexed)"
5. For conference papers: Note conference ranking if available, else "N/A"
6. If SJR not found: Mark as "Not found in SJR database" (NOT "N/A")

## Output Format

### Required Output Structure

Create a markdown file named: `[DocumentName]_ReferenceAudit.md`

#### Section 1: Document Metadata
```markdown
# Reference Audit Report

**Document**: [Full document title]
**Date of Audit**: [ISO 8601 format]
**Total References Listed**: [Number]
**Total In-Text Citations**: [Number]
**Citation Style**: [APA/Harvard/Chicago/etc.]
**Audit Status**: [Complete/Partial/Failed]
```

#### Section 2: Executive Summary
```markdown
## Executive Summary

- **Verified References**: X/Y (Z%)
- **Failed Verifications**: X
- **Orphan References**: X
- **Orphan Citations**: X
- **Misrepresentations Detected**: X
- **Fabricated References (Suspected)**: X
- **Overall Quality Assessment**: [High/Medium/Low/Critical Issues]

### Key Issues
1. [Most critical issue]
2. [Second most critical issue]
...
```

#### Section 3: Detailed Verification Table

```markdown
## Detailed Reference Verification

| Ref # | Reference (Short Form) | Verification Status | Evidence from Scholar | Accurate as Cited? | Notes | Citation Status | Reference Quality (SJR) |
|-------|------------------------|---------------------|----------------------|-------------------|-------|-----------------|------------------------|
| 1 | Author (Year) | VERIFIED/FAILED/PARTIAL | Summary of findings | YES/NO/PARTIAL + explanation | Issues noted | Cited in text: [Yes/No] + locations | Q1 (SJR: X.XX) / N/A / Not found |
```

#### Section 4: Detailed Analysis per Reference

For each reference, provide:

```markdown
### Reference [Number]: [Short Form Citation]

**As Listed in Document**:
```
[Exact text from reference list]
```

**Verification Attempt**:
- **Search Method**: [Semantic Scholar/Google Scholar/DOI/etc.]
- **Search Terms Used**: "[exact terms]"
- **Results Found**: [Yes/No/Partial]

**Verification Results**:
- **Title Match**: ✓ CONFIRMED / ✗ MISMATCH / ? UNCERTAIN / ⊗ NOT FOUND
  - Listed: "[title in document]"
  - Found: "[title in database]"

- **Authors Match**: ✓ CONFIRMED / ✗ MISMATCH / ? UNCERTAIN / ⊗ NOT FOUND
  - Listed: [authors in document]
  - Found: [authors in database]

- **Year Match**: ✓ CONFIRMED / ✗ MISMATCH / ? UNCERTAIN / ⊗ NOT FOUND
  - Listed: [year]
  - Found: [year]

- **Venue Match**: ✓ CONFIRMED / ✗ MISMATCH / ? UNCERTAIN / ⊗ NOT FOUND
  - Listed: "[journal/book]"
  - Found: "[journal/book]"

**Abstract/Summary from Source**:
```
[Retrieved abstract or summary, or "NOT AVAILABLE - [reason]"]
```

**Content Verification**:
- **How cited in document**: "[exact citation context from document]"
- **Actual content of source**: "[summary from abstract]"
- **Assessment**: ACCURATE / MISREPRESENTED / OVERSTATED / PARTIAL / CANNOT ASSESS
- **Explanation**: [Detailed reasoning]

**Quality Metrics**:
- **Journal**: [Full journal name]
- **SJR Score**: [X.XXX] or NOT FOUND or N/A (not indexed)
- **Quartile**: Q1/Q2/Q3/Q4 or N/A
- **Subject Area**: [Field]

**In-Text Citation Analysis**:
- **Cited in document**: YES / NO
- **Citation locations**: [List all page numbers or sections]
- **Citation format**: "[example of how it appears]"

**Final Verdict**:
- **Status**: VERIFIED / FAILED / SUSPICIOUS / CANNOT VERIFY
- **Confidence**: HIGH / MEDIUM / LOW / NONE
- **Action Required**: [NONE / STUDENT MUST VERIFY / SUPERVISOR REVIEW / REJECT]

**Detailed Notes**:
[Any additional observations, concerns, or context]

---
```

#### Section 5: Orphan Analysis

```markdown
## Orphan References (Listed but Not Cited)

| Reference | Reason |
|-----------|--------|
| [Short form] | Listed in references but no in-text citation found |

## Orphan Citations (Cited but Not Listed)

| Citation | Location | Reason |
|----------|----------|--------|
| [Short form] | [Page/section] | Cited in text but no corresponding reference list entry |

## Citation-Reference Mismatches

| Citation in Text | Reference in List | Discrepancy |
|------------------|-------------------|-------------|
| Author (2020) | Author (2021) | Year mismatch |
```

#### Section 6: Quality Distribution

```markdown
## Journal Quality Distribution

| Quartile | Count | Percentage |
|----------|-------|------------|
| Q1 | X | XX% |
| Q2 | X | XX% |
| Q3 | X | XX% |
| Q4 | X | XX% |
| Not Indexed | X | XX% |
| Not Found | X | XX% |

**Average SJR Score** (for ranked journals): X.XXX
```

#### Section 7: Critical Findings

```markdown
## Critical Issues Requiring Immediate Attention

### Fabricated References (Suspected)
1. [Reference]: Cannot be located in any database
   - **Search attempts**: [detail all search strategies]
   - **Reason for suspicion**: [specific evidence]

### Misrepresented Sources
1. [Reference]: Source found but content misrepresented
   - **How cited**: [context in document]
   - **Actual content**: [what source actually says]
   - **Severity**: HIGH/MEDIUM/LOW

### Low-Quality Sources
1. [Reference]: Published in Q4 journal or predatory venue
   - **SJR**: X.XXX (Q4)
   - **Concerns**: [specific issues]
```

#### Section 8: Recommendations

```markdown
## Recommendations

### For Student
1. [Specific actionable recommendation]
2. [Next steps required]

### For Supervisor
1. [Review priorities]
2. [Follow-up actions]

### Overall Assessment
[Holistic evaluation of reference quality and academic integrity]
```

## Strict Verification Standards

### When to Mark "CANNOT VERIFY"

Document explicitly when verification is impossible and **state the specific reason**:

1. **Source not found in any database**
   - Reason: "Exhaustive search of Semantic Scholar, Google Scholar, and CrossRef yielded no results"
   - Searches attempted: [list exact search strings used]

2. **Ambiguous match**
   - Reason: "Multiple papers found with similar titles; cannot confirm which is the cited source"
   - Candidates found: [list potential matches]

3. **Incomplete reference information**
   - Reason: "Reference missing [author/title/year/venue]; insufficient information to locate source"
   - Missing elements: [specify]

4. **Access restricted**
   - Reason: "Source identified but abstract/content not available for verification"
   - Found at: [URL or database]

5. **Language barrier**
   - Reason: "Source located but published in [language]; cannot verify content without translation"

6. **Paywall/subscription required**
   - Reason: "Source identified behind paywall; abstract available but full content verification not possible"

7. **Grey literature**
   - Reason: "Working paper/thesis/report not indexed in standard databases; institutional repository link [available/not available]"

### When to Mark "SUSPICIOUS"

Flag references as suspicious when:

1. **Pattern of issues**: Multiple references from same author/year all fail verification
2. **Unusual venues**: Journal names that don't appear in any database
3. **Impossible combinations**: Author names + venue + year that don't logically fit
4. **Too perfect**: Reference matches document's argument suspiciously well but can't be verified
5. **Predatory indicators**: Venue shows signs of predatory publishing (excessive scope, rapid publication, unclear peer review)

### When to Mark "MISREPRESENTED"

Mark a reference as misrepresented when:

1. **Content contradiction**: Source argues opposite of how it's cited
2. **Scope inflation**: Narrow study cited as broad generalizable finding
3. **Method mischaracterization**: Qualitative study cited as quantitative evidence (or vice versa)
4. **Cherry-picking**: One finding cited while ignoring contradictory findings in same source
5. **Context removal**: Quote or finding cited without critical context that changes meaning

## Error Handling and Documentation

### If API/Search Fails
Document the failure:
```markdown
**Verification Status**: SYSTEM ERROR
**Reason**: [API timeout / Rate limit exceeded / Network error / etc.]
**Attempted**: [timestamp]
**Retry Required**: Yes
```

### If Format is Unrecognizable
```markdown
**Verification Status**: FORMAT ERROR
**Reason**: Reference format does not follow standard citation style
**Listed**: "[exact text]"
**Issue**: [Cannot parse author / Cannot parse year / etc.]
**Recommendation**: Student must reformat according to [style guide]
```

### If Reference is Partially Complete
```markdown
**Verification Status**: INCOMPLETE
**What's Present**: [list available elements]
**What's Missing**: [list missing elements]
**Can Search**: YES/NO
**If No**: Reason - [insufficient information for database search]
```

## Tools and APIs Required

### Semantic Scholar API
- Endpoint: `https://api.semanticscholar.org/graph/v1/paper/search`
- Parameters: query, fields (title, authors, year, abstract, venue, citationCount)
- Rate limit: Respect API limits, implement retry logic

### Google Scholar (via serpapi or similar)
- Use for fallback when Semantic Scholar fails
- Parse results carefully (less structured than API)

### SCImago Journal Rank
- Database: https://www.scimagojr.com/
- Search by journal title
- Record: SJR score, quartile, subject area

### CrossRef
- DOI resolution: `https://api.crossref.org/works/{doi}`
- Metadata verification

## Quality Control

### Self-Check Before Submitting Audit
- [ ] Every reference has a verification attempt documented
- [ ] Every "CANNOT VERIFY" has a specific reason stated
- [ ] No assumptions made about partial information
- [ ] All orphan references identified
- [ ] All orphan citations identified
- [ ] Executive summary accurately reflects detailed findings
- [ ] Recommendations are actionable and specific
- [ ] Critical issues clearly flagged
- [ ] Output file properly named and formatted

## Batch Processing Instructions

When processing multiple documents:

1. Process one document completely before starting the next
2. Create separate output file for each document
3. Maintain a master log: `_BatchAuditLog.md` with:
   - List of all documents processed
   - Processing timestamps
   - High-level summary for each
   - Any cross-document patterns observed

## Ethical Considerations

### Student Privacy
- Focus on reference quality, not student competence
- Language should be objective, not judgmental
- Recommendations should be constructive

### Academic Integrity
- Distinguish between honest errors and potential fabrication
- Provide evidence for serious allegations
- Allow for possibility of legitimate but hard-to-find sources

### Limitations of AI Audit
- Acknowledge when human expert review is needed
- Don't overstate certainty of findings
- Recognize that absence of evidence ≠ evidence of absence

---

## Execution Instructions for AI Agent

When processing a document:

1. **Read the document** completely to understand context
2. **Extract all references** from the reference list section
3. **Extract all in-text citations** from the document body
4. **For each reference**:
   - Search Semantic Scholar API first
   - Fallback to Google Scholar if needed
   - Document every search attempt
   - Record exact results
   - Compare against listed reference
   - Assess content accuracy if available
   - Look up journal quality (SJR)
   - Check if cited in text
5. **Compile comprehensive report** following the output format
6. **Self-check** against quality control checklist
7. **Save output** as `[DocumentName]_ReferenceAudit.md`

### Non-Negotiable Rules

1. **NEVER** claim verification without explicit evidence
2. **NEVER** skip documenting search attempts
3. **NEVER** assume information not explicitly stated
4. **NEVER** copy reference details without verification
5. **ALWAYS** document why verification failed
6. **ALWAYS** distinguish between different types of verification failures
7. **ALWAYS** provide specific, actionable recommendations

---

**Last Updated**: 2025-10-17
**Version**: 1.0
**Purpose**: Rigorous academic reference verification with zero tolerance for assumptions
