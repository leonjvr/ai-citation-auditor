# Best Practices for Citation Quality and Audit Usage

This guide provides recommendations for supervisors, students, and institutions on achieving high citation quality and effective use of the AI-Powered Citation Auditor.

## Table of Contents

1. [For Students and Researchers](#for-students-and-researchers)
2. [For Supervisors and Educators](#for-supervisors-and-educators)
3. [For Institutions](#for-institutions)
4. [Reference Management Best Practices](#reference-management-best-practices)
5. [Quality Benchmarks by Document Type](#quality-benchmarks-by-document-type)
6. [Integration into Academic Workflow](#integration-into-academic-workflow)

---

## For Students and Researchers

### 1. Cite as You Write

**DON'T:**
```
❌ Write entire document first
❌ Add all references at the end
❌ Bulk import references "just in case"
❌ Cite from memory without checking source
```

**DO:**
```
✅ Add reference to management software when you read it
✅ Cite immediately when using source in writing
✅ Verify citation details before adding to software
✅ Keep notes on why source is relevant
```

**Why this matters:**
- Prevents orphan references (listed but not cited)
- Ensures you have actually read what you cite
- Makes it easier to find sources again if needed
- Reduces errors from memory or rushed work

---

### 2. Use Reference Management Software

**Recommended tools:**
- **Zotero** (free, open source, browser integration)
- **Mendeley** (free, PDF annotation, cloud sync)
- **EndNote** (paid, powerful, institutional licenses common)

**Essential features to use:**
- Browser plugins for one-click citation capture
- PDF import with automatic metadata extraction
- Citation style switching (APA, Harvard, Chicago, etc.)
- Duplicate detection
- Notes and tags for organization

**Common mistakes to avoid:**
```
❌ Importing without checking metadata
❌ Not verifying auto-extracted information
❌ Keeping duplicate entries
❌ Not using consistent citation keys
```

---

### 3. Verify Before You Cite

**When adding a reference, confirm:**

✅ **Author names:**
- Full names with initials
- Check author order (first author matters!)
- Verify spelling (especially non-English names)

✅ **Publication year:**
- Actual publication year, not "online first" year
- For books: edition year, not reprint year

✅ **Title:**
- Exact title (including subtitle)
- Proper capitalization for your citation style

✅ **Venue:**
- Full journal name (not abbreviation, unless style requires)
- Conference proceedings name and location
- Book publisher and place

✅ **DOI or URL:**
- Include if available
- Verify link works

---

### 4. Quality Over Quantity

**Characteristics of strong reference lists:**

| Aspect | Weak Approach | Strong Approach |
|--------|---------------|-----------------|
| **Number** | 200+ references to look thorough | Focused set of most relevant sources |
| **Recency** | All recent (last 2 years) | Mix: foundational classics + recent developments |
| **Integration** | Many listed but not cited | Nearly all cited, some multiple times |
| **Source quality** | Whatever Google search finds first | Deliberate selection of peer-reviewed sources |
| **Diversity** | Single research tradition | Multiple perspectives and methods |

**Aim for:**
- **Honours (15-20 pages)**: 20-40 high-quality references
- **Master's (40-80 pages)**: 50-100 focused references
- **Doctoral (200+ pages)**: 200-500 comprehensive references

**Red flags:**
- Orphan reference rate >15% (cited references / total references)
- <50% Q1/Q2 journals (for empirical work)
- Heavy reliance on websites, blogs, or non-peer-reviewed sources
- Missing key foundational works in your field

---

### 5. Self-Audit Before Submission

**Timeline:**
1. **Draft stage** (before supervisor review): Run initial audit
2. **Revision stage** (after first feedback): Re-audit to verify corrections
3. **Final stage** (before submission): Final quality check

**What to check:**

**Week before supervisor meeting:**
```bash
# Run audit on your draft
claude --dangerously-skip-permissions

# In Claude:
"Run citation audit on my_thesis_draft.docx using CLAUDE.md protocol"
```

**Review results for:**
- Orphan references → Cite in text or remove
- Orphan citations → Add to reference list
- Unverifiable references → Find original PDFs, verify details
- Citation-reference mismatches → Correct errors
- Low journal quality → Consider replacing with stronger sources

**Fix issues and re-audit:**
```bash
# After corrections
"Re-run audit on my_thesis_revised.docx"
```

**Goal:** Achieve >85% verification rate before sending to supervisor

---

### 6. Keep Original PDFs Organized

**Folder structure:**
```
Literature/
├── Core_Theory/
│   ├── Barney_1991_RBV.pdf
│   ├── Freeman_1984_Stakeholder.pdf
│   └── Teece_1997_DynamicCapabilities.pdf
├── Methods/
│   ├── Eisenhardt_2007_CaseStudy.pdf
│   └── Yin_2018_CaseStudyResearch.pdf
├── Empirical_Studies/
│   ├── [Organized by topic]
└── Working_Papers/
    └── [Pre-prints and grey literature]
```

**Naming convention:**
```
FirstAuthor_Year_ShortTitle.pdf

Examples:
✅ Barney_1991_ResourceBasedView.pdf
✅ Teece_1997_DynamicCapabilities.pdf
❌ download_23423.pdf
❌ Untitled_document.pdf
```

**Why this matters:**
- Easy to find sources if questions arise
- Can provide PDFs if verification fails
- Helps you actually read what you cite
- Essential for supervisory review

---

## For Supervisors and Educators

### 1. Run Audits at Proposal Stage, Not Final Submission

**Timeline integration:**

| Milestone | Audit Purpose | Action |
|-----------|---------------|--------|
| **Proposal** | Identify citation practices early | Provide feedback and training if needed |
| **Literature review draft** | Verify quality and comprehensiveness | Guide toward better sources |
| **First full draft** | Comprehensive check | Address systematic issues |
| **Final draft** | Verification only | Quick spot-check of corrections |

**Why early matters:**
- Prevents wasted work on flawed literature foundation
- Identifies students needing additional support
- Correcting errors is easier before everything is written
- Students learn proper practices for future work

---

### 2. Use Audits for Triage, Not Definitive Judgment

**AI audit is excellent for:**
✅ Identifying which references need closer human review
✅ Detecting patterns (orphan refs, low quality sources)
✅ Screening for obvious errors (wrong years, journal names)
✅ Objective initial quality assessment

**AI audit is NOT sufficient for:**
❌ Determining if sources are appropriately used in context
❌ Assessing theoretical coherence of literature review
❌ Verifying nuanced content claims
❌ Final judgment on academic integrity issues

**Workflow:**
```
1. Run AI audit (10 minutes)
2. Review audit report (30 minutes)
3. Prioritize flagged references for manual check
4. Verify high-risk items (unverifiable, fabricated)
5. Discuss findings with student
6. Require corrections and re-audit
```

---

### 3. Frame Feedback as Learning, Not Punishment

**Problematic approach:**
```
❌ "Your reference list is a disaster."
❌ "Did you make these up?"
❌ "This is unacceptable work."
```

**Constructive approach:**
```
✅ "The audit identified 5 references that couldn't be verified. Let's discuss
   how to strengthen these citations."

✅ "I notice 40% of your references aren't cited in the text. This suggests
   we need to work on integrating sources more effectively."

✅ "Several year mismatches were detected. Let me show you how to verify
   citation details using Google Scholar."
```

**Learning-focused feedback template:**
```
Dear [Student],

I ran a citation audit on your draft using an AI-powered verification tool.
Here's what we discovered:

**Strengths:**
- Strong use of Q1 journals (60% of sources)
- Good mix of foundational and recent literature
- Clear theoretical framework

**Areas for improvement:**
- 15 references need verification (details attached)
- 3 year mismatches to correct (highlighted in report)
- 20 orphan references to integrate or remove

**Next steps:**
1. Review attached audit report
2. Provide PDFs for the 15 unverifiable references
3. Correct the year mismatches
4. For orphan references: either cite in text or remove
5. Schedule meeting to discuss any questions

This is a normal part of the revision process. Let's use these findings to
strengthen your work.

Best regards,
[Supervisor]
```

---

### 4. Set Clear Quality Expectations

**Sample rubric for reference quality:**

| Criterion | Excellent (90-100%) | Good (75-89%) | Acceptable (60-74%) | Needs Work (<60%) |
|-----------|--------------------|--------------|--------------------|------------------|
| **Verification rate** | 95-100% | 85-95% | 70-85% | <70% |
| **Orphan references** | <5% | 5-15% | 15-30% | >30% |
| **Journal quality** | 60%+ Q1 | 40-60% Q1 | 20-40% Q1 | <20% Q1 |
| **Source diversity** | Multiple perspectives | Good range | Limited range | Narrow |
| **Citation accuracy** | 0-2 errors | 3-5 errors | 6-10 errors | >10 errors |

**Communicate expectations:**
- Include in supervision handbook/guidelines
- Discuss at first supervisory meeting
- Share example audit reports (anonymized)
- Provide access to audit tool for self-checking

---

### 5. Provide Training and Resources

**Essential training topics:**

**Reference management software (2-hour workshop):**
- Installing and setting up Zotero/Mendeley/EndNote
- Browser plugin for citation capture
- Importing PDFs and extracting metadata
- Organizing references with folders and tags
- Generating bibliographies in Word/Google Docs
- Avoiding common pitfalls

**Database searching (1-hour session):**
- Google Scholar advanced search
- Semantic Scholar for AI-powered recommendations
- Discipline-specific databases (PubMed, EconLit, PsycINFO, etc.)
- Using boolean operators (AND, OR, NOT)
- Citation chaining (forward and backward)

**Citation quality (1-hour session):**
- Understanding journal quality (SJR, impact factor)
- Identifying peer-reviewed vs. non-peer-reviewed sources
- Evaluating source appropriateness
- Balancing foundational and recent literature

**Self-auditing (30-minute demo):**
- How to run AI citation audit
- Interpreting audit reports
- Common errors and how to fix them
- When to seek supervisor help

---

### 6. Build in Multiple Review Points

**Suggested supervision schedule:**

**Month 1-2: Proposal**
```
Student: Submit proposal with initial reference list (20-30 sources)
Supervisor: Run audit, provide feedback on citation practices
Student: Revise and resubmit
```

**Month 3-4: Literature Review Draft**
```
Student: Submit literature chapter (50-80 sources)
Supervisor: Run audit, check for quality and comprehensiveness
Student: Address gaps, improve source quality
```

**Month 5-6: First Full Draft**
```
Student: Submit complete draft with full reference list
Student: Run self-audit before submission
Supervisor: Review audit results, focus on flagged issues only
Student: Corrections
```

**Month 7: Final Draft**
```
Student: Submit final version
Student: Include audit report showing >90% verification
Supervisor: Spot-check only
```

---

## For Institutions

### 1. Integrate into Writing Centers

**Service model:**

**Walk-in consultation:**
- Students bring draft and reference list
- Writing consultant runs audit while student waits (10 min)
- Review results together (20-30 min)
- Provide guidance on corrections
- Schedule follow-up if needed

**Workshop series:**
- "Citation Quality 101" (intro to expectations)
- "Reference Management Tools" (hands-on training)
- "Self-Auditing Your Work" (using AI tools)
- "Advanced Database Searching" (finding quality sources)

**Online resources:**
- Video tutorial on running audits
- Downloadable audit protocol
- Example reports (anonymized)
- FAQ and troubleshooting guide

---

### 2. Require Audits at Key Milestones

**Graduate program policy example:**

```
All thesis and dissertation candidates must submit citation audit reports
at the following milestones:

1. Proposal defense: Audit of proposed reference list (min 20 sources)
2. Ethics review: Audit of literature review chapter
3. Final submission: Comprehensive audit of full reference list

Minimum standards:
- Master's: 75% verification rate, <20% orphan references
- Doctoral: 85% verification rate, <15% orphan references

Students not meeting standards will be required to revise and resubmit.
```

**Benefits:**
- Sets objective quality standards
- Reduces supervisor burden
- Ensures consistency across programs
- Detects issues early

---

### 3. Provide Institutional Access and Training

**Resource allocation:**

**Software:**
- Institutional Claude CLI license
- Reference management software (Zotero, Mendeley, EndNote)
- Access to academic databases

**Training:**
- Faculty training on using audit tools
- TA training on supporting students
- Student orientation workshops
- Online tutorials and guides

**Support:**
- Writing center consultants trained in audit interpretation
- IT support for software installation
- Dedicated email/helpdesk for questions

---

### 4. Develop Academic Integrity Policy

**Policy framework:**

**Detection vs. Education:**
```
The purpose of citation audits is educational, not punitive. Audit reports
serve as formative feedback to improve citation quality.

However, systematic fabrication of references (>5 unverifiable sources with
no evidence of existence) may be referred to academic integrity committee
for investigation.
```

**Graduated response:**
```
First offense (unintentional errors):
- Require corrections
- Provide training on proper citation practices
- Re-audit after corrections

Pattern of issues (multiple documents):
- Mandatory workshop on academic integrity
- Closer supervisory oversight
- May delay graduation pending remediation

Deliberate fabrication (confirmed):
- Academic integrity investigation
- Possible consequences per institutional policy
```

---

## Reference Management Best Practices

### Choosing Reference Management Software

| Feature | Zotero | Mendeley | EndNote |
|---------|--------|----------|---------|
| **Cost** | Free | Free | Paid (~$250) |
| **Platform** | Win/Mac/Linux | Win/Mac | Win/Mac |
| **Storage** | 300MB free | 2GB free | Unlimited |
| **Browser plugin** | ✅ Excellent | ✅ Good | ✅ Good |
| **PDF annotation** | ✅ Basic | ✅ Excellent | ✅ Good |
| **Collaboration** | ✅ Groups | ✅ Shared folders | ✅ Shared libraries |
| **Word plugin** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Open source** | ✅ Yes | ❌ No | ❌ No |
| **Best for** | Academic researchers | Students | Institutional users |

**Recommendation:**
- **Students**: Zotero (free, powerful, won't lose access after graduation)
- **Institutions**: EndNote (support, training, integration)
- **Collaboration**: Mendeley (social features, shared annotations)

---

### Workflow: From Source to Citation

**Step 1: Discovery**
```
Google Scholar search → Find relevant paper → Click browser plugin →
Automatically imports to reference manager with metadata
```

**Step 2: Organization**
```
Review imported metadata → Correct any errors → Add to project folder →
Tag with keywords → Add notes on relevance
```

**Step 3: Reading**
```
Annotate PDF in reference manager → Highlight key quotes →
Note page numbers → Write summary in notes field
```

**Step 4: Writing**
```
Write in Word → Insert citation with Word plugin → Choose source from
reference manager → Citation and reference list generated automatically
```

**Step 5: Verification**
```
Run AI audit on draft → Review flagged references → Correct errors →
Re-audit to verify → Submit with audit report
```

---

### Common Metadata Errors to Fix

**After auto-importing, ALWAYS check:**

✅ **Author names:**
```
❌ "Smith J." → ✅ "Smith, John A."
❌ "van der Berg" → ✅ "Van der Berg, Maria"
```

✅ **Publication year:**
```
❌ "2024" (online first) → ✅ "2023" (actual publication)
❌ "2010" (reprint) → ✅ "1984" (original)
```

✅ **Journal names:**
```
❌ "Acad. Mgmt. J." → ✅ "Academy of Management Journal"
❌ "AMJ" → ✅ "Academy of Management Journal"
```

✅ **Volume and issue:**
```
❌ "18" (volume only) → ✅ "18(7)" (volume and issue)
```

✅ **DOI:**
```
❌ Missing → ✅ Add from article if available
❌ "http://dx.doi.org/10.1234..." → ✅ "https://doi.org/10.1234..."
```

---

## Quality Benchmarks by Document Type

### Honours Project / Undergraduate Thesis

**Reference list characteristics:**
- **Count**: 20-40 references
- **Q1/Q2 journals**: 30-50%
- **Foundational sources**: 5-10 key theoretical works
- **Recent sources** (<5 years): 30-50%
- **Orphan references**: <20%
- **Verification rate**: >70%

**Acceptable source mix:**
- 50-70% peer-reviewed journals
- 20-30% books and book chapters
- 10-20% grey literature (reports, theses)
- <10% websites/blogs (data sources only)

---

### Master's Thesis / Dissertation

**Reference list characteristics:**
- **Count**: 50-120 references (depending on field and type)
- **Q1/Q2 journals**: 50-70%
- **Foundational sources**: 10-20 key works
- **Recent sources** (<5 years): 40-60%
- **Orphan references**: <15%
- **Verification rate**: >80%

**Expected source mix:**
- 70-80% peer-reviewed journals
- 15-25% books and book chapters
- 5-10% grey literature
- <5% websites/practitioner sources

---

### Doctoral Thesis / Dissertation

**Reference list characteristics:**
- **Count**: 200-500 references (comprehensive coverage)
- **Q1/Q2 journals**: 70-85%
- **Foundational sources**: 30-50 key works
- **Recent sources** (<5 years): 40-60%
- **Orphan references**: <10%
- **Verification rate**: >90%

**Expected source mix:**
- 80-90% peer-reviewed journals
- 10-15% books and book chapters
- <5% grey literature (must be justified)
- <2% websites (data sources only)

---

### Journal Article Submission

**Reference list characteristics:**
- **Count**: 30-80 references (depending on journal and article type)
- **Q1/Q2 journals**: 70-90%
- **Foundational sources**: Mix of classics and recent
- **Recent sources** (<5 years): 60-80%
- **Orphan references**: 0% (every reference must be cited)
- **Verification rate**: >95%

**Expected source mix:**
- 90-95% peer-reviewed journals (top-tier preferred)
- 5-10% books (if relevant)
- 0% grey literature, websites (unless data sources)

---

## Integration into Academic Workflow

### Student Self-Check Schedule

**During literature review:**
```
Week 1: Find 10-15 key sources → Add to reference manager
Week 2: Find another 15-20 → Run first audit to verify all are verifiable
Week 3-4: Expand to 40-50 sources → Organize by theme
Week 5: Run second audit → Ensure >80% verification, check for duplicates
```

**During writing:**
```
After each chapter: Review citations → Check for orphan citations/references
Before supervisor meeting: Run full audit → Fix obvious errors
After supervisor feedback: Re-audit → Verify corrections made
```

**Before final submission:**
```
2 weeks before: Final audit → >90% verification target
1 week before: Re-check flagged references → Provide PDFs if needed
3 days before: Final proofread → Verify all corrections made
```

---

### Supervisor Review Schedule

**Proposal stage:**
```
Receive: Proposal + initial reference list
Action: Quick audit (10 min) + review (20 min)
Feedback: Within 3 days
Focus: Citation practices, source quality
```

**Literature review stage:**
```
Receive: Literature chapter + reference list
Action: Comprehensive audit (10 min) + detailed review (60 min)
Feedback: Within 1 week
Focus: Comprehensiveness, theoretical coherence, quality
```

**First full draft:**
```
Receive: Full draft + student self-audit report
Action: Review student audit + spot-check flagged items (30 min)
Feedback: Within 2 weeks
Focus: Corrections of identified issues
```

**Final draft:**
```
Receive: Final version + verification audit report
Action: Quick check of audit report (10 min)
Approval: If >90% verification and no critical issues
```

---

**Last Updated**: 2025-10-17
**Version**: 1.0.0

**See Also:**
- TROUBLESHOOTING.md - Resolving specific issues
- INTERPRETING_RESULTS.md - Understanding audit reports
- METHODOLOGY.md - Detailed protocol and replication guide
