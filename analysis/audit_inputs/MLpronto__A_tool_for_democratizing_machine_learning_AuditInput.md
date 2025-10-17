# CITATION AUDIT REQUEST

**Document**: MLpronto__A_tool_for_democratizing_machine_learning.pdf
**Total References**: 21
**Audit Protocol**: CLAUDE.md - AI-Powered Citation Auditor v1.0

---

## TASK: Systematic Reference Verification

Following the **Reference Checking Protocol for Academic Documents** (CLAUDE.md), perform a comprehensive citation audit of this document with **absolute strictness and zero tolerance for assumptions**.

### Complete Reference List

The following references were extracted from the document's reference section:

[1] JordanM.I.andMitchellT.M.,Machinelearning:Trends,perspectives,andprospects.Science,2015. 349(6245):p.255–60.https://doi.org/10.1126/science.aaa8415PMID:26185243

[2] NguyenN.andNadiS..AnempiricalevaluationofGitHubcopilot’scodesuggestions.inProceedingsof the19thInternationalConferenceonMiningSoftwareRepositories.2022.

[3] Stokel-WalkerC.andVanNoordenR.,ThepromiseandperilofgenerativeAI.Nature,2023. 614:p. 214–216. PLOSONE|https://doi.org/10.1371/journal.pone.0294924 November30,2023 11/12 PLOS ONE MLpronto:Atoolfordemocratizingmachinelearning

[4] VanschorenJ.,etal.,OpenML:networkedscienceinmachinelearning.ACMSIGKDDExplorations Newsletter,2014. 15(2):p.49–60.

[5] Kaggle.Availablefrom:https://www.kaggle.com/.

[6] HeX.,ZhaoK.,andChuX.,AutoML:asurveyofthestate-of-the-art.Knowledge-BasedSystems,

[2021] 212:p.106622.

[7] AgarwalN.andDasS..Interpretablemachinelearningtools:asurvey.in2020IEEESymposiumSeries onComputationalIntelligence(SSCI).2020.IEEE.

[8] MehrabiN.,etal.,Asurveyonbiasandfairnessinmachinelearning.ACMComputingSurveys,2021. 54(6):p.1–35.

[9] RossM.S.,Towardsaninclusiveandequitablefuture:theimperativetobroadenparticipationincom- puting.2022.p.15–30.

[10] PedregosaF.,etal.,Scikit-learn:machinelearninginpython.JournalofMachineLearningResearch,

[2011] 12:p.2825–2830.

[11] OlsonR.S.,etal.,PMLB:alargebenchmarksuiteformachinelearningevaulationandcomparison.Bio- DataMining,2017. 10:p.1–13.

[12] RomanoJ.D.,etal.,PMLBv1.0:anopen-sourcedatasetcollectionforbenchmarkingmachinelearning methods.Bioinformatics,2022. 38(3):p.878–880.https://doi.org/10.1093/bioinformatics/btab727 PMID:34677586

[13] FrankE.,HallM.A.,andWittenI.H.,DataMining:PracticalMachineLearningToolsandTechniques,in TheWEKAWorkbench,FourthEdition.2016,MorganKaufmann.

[14] PaszkeA.,etal.,Pytorch:Animperativestyle,high-performancedeeplearninglibrary.Advancesin neuralinformationprocessingsystems(NIPS),2019. 32.

[15] KotthoffL.,etal.,Auto-WEKA:AutomaticmodelselectionandhyperparameteroptimizationinWEKA. Automatedmachinelearning:methods,systems,challenges,2019:p.81–95.

[16] ZimmerL.,LindauerM.,andHutterF.,Auto-pytorch:Multi-fidelitymetalearningforefficientandrobust autoDL.IEEETransactionsonPatternAnalysisandMachineIntelligence,2021. 43(9):p.3079–3090. https://doi.org/10.1109/TPAMI.2021.3067763PMID:33750687

[17] FeurerM.,etal.Efficientandrobustautomatedmachinelearning.inAdvancesinNeuralInformation ProcessingSystems 28(NIPS2015).2015.

[18] FeurerM.,etal.,Auto-Sklearn2.0:hands-freeAutoMLviameta-learning.JournalofMachineLearning Research,2022. 23:p.1–61.

[19] SnoekJ.,LarochelleH.,andAdamsR.P..Practicalbayesianoptimizationofmachinelearningalgo- rithms.inAdvancesinneuralinformationprocessingsystems 25(NIPS2012).2012. PLOSONE|https://doi.org/10.1371/journal.pone.0294924 November30,2023 12/12


---

## VERIFICATION REQUIREMENTS

For EACH reference above, you must:

### 1. Independent Verification
- Search **Semantic Scholar** API first (primary source)
- Fallback to **Google Scholar** if Semantic Scholar fails
- Verify **DOI** using CrossRef if provided
- Check publisher websites when available

### 2. Verification Checklist
For each reference, confirm:
- [ ] **Title** matches exactly (or semantically identical)
- [ ] **Authors** confirmed (all names, correct order)
- [ ] **Year** confirmed
- [ ] **Publication venue** confirmed (journal/book/conference name, volume, issue, pages)
- [ ] **Abstract or summary** retrieved
- [ ] **Content relevance** assessable

### 3. Quality Assessment
For each verified journal article:
- Search **SCImago Journal Rank (SJR)** database
- Record SJR score and quartile (Q1, Q2, Q3, Q4)
- Note journal subject area and category
- For books/reports/theses: Mark as "N/A (not indexed)"
- For conference papers: Note conference ranking if available, else "N/A"
- If SJR not found: Mark as "Not found in SJR database" (NOT "N/A")

### 4. Documentation Requirements
For EACH reference, document:
- **What was found**: Exact details from verification source
- **What matches**: Specific elements that align with cited reference
- **What differs**: Any discrepancies, even minor ones
- **Confidence level**: HIGH/MEDIUM/LOW/FAILED

---

## OUTPUT FORMAT REQUIRED

Create a markdown file named: `{filename.replace('.pdf', '')}_ReferenceAudit.md`

The report MUST include:

1. **Document Metadata Section**
   - Document title
   - Date of audit (ISO 8601 format)
   - Total references listed
   - Citation style
   - Audit status

2. **Executive Summary**
   - Verified references: X/Y (Z%)
   - Failed verifications
   - Orphan references
   - Misrepresentations detected
   - Fabricated references (suspected)
   - Overall quality assessment

3. **Detailed Verification Table**
   | Ref # | Reference (Short Form) | Verification Status | Evidence from Scholar | Accurate as Cited? | Notes | Reference Quality (SJR) |
   |-------|------------------------|---------------------|----------------------|-------------------|-------|------------------------|

4. **Detailed Analysis per Reference**
   For each reference, provide comprehensive analysis following CLAUDE.md Section 4 format.

5. **Quality Distribution**
   - Q1 journals: X (XX%)
   - Q2 journals: X (XX%)
   - Q3 journals: X (XX%)
   - Q4 journals: X (XX%)
   - Not indexed: X (XX%)
   - Average SJR score

6. **Critical Findings**
   - Fabricated references (suspected)
   - Misrepresented sources
   - Low-quality sources

7. **Recommendations**
   - For student
   - For supervisor
   - Overall assessment

---

## STRICT VERIFICATION STANDARDS

### Zero Assumptions Policy
- **NEVER** assume a reference is correct without verification
- **NEVER** fill in missing information speculatively
- **NEVER** accept partial matches as verification
- **ALWAYS** document why verification failed or is incomplete

### When to Mark "CANNOT VERIFY"
Document explicitly when verification is impossible and state the specific reason:
- Source not found in any database → "Exhaustive search yielded no results"
- Ambiguous match → "Multiple similar papers found; cannot confirm which is cited"
- Incomplete reference → "Missing [elements]; insufficient information to locate"
- Access restricted → "Source identified but abstract not available"
- Language barrier → "Source in [language]; cannot verify content"
- Paywall → "Behind paywall; abstract available but full content unverified"
- Grey literature → "Not indexed; institutional repository link [status]"

### When to Mark "SUSPICIOUS"
- Pattern of issues: Multiple references from same author/year fail verification
- Unusual venues: Journal names not in any database
- Impossible combinations: Author + venue + year don't logically fit
- Predatory indicators: Signs of predatory publishing

### When to Mark "MISREPRESENTED"
- Content contradiction: Source argues opposite of citation
- Scope inflation: Narrow study cited as broad finding
- Method mischaracterization: Qualitative cited as quantitative
- Cherry-picking: One finding cited, contradictory findings ignored
- Context removal: Quote cited without critical context

---

## IMPORTANT NOTES

**Note 1**: This is a validation dataset audit. The purpose is to test the AI-Powered Citation Auditor methodology's accuracy and reliability.

**Note 2**: Document EVERY search attempt, EVERY verification result, and EVERY reason for failure. This data is critical for methodology validation.

**Note 3**: Do NOT skip any references. All {reference_count} references must be audited.

**Note 4**: Use actual API searches - do NOT rely on LLM training data knowledge. Fresh verification only.

---

**Protocol Version**: CLAUDE.md v1.0 (2025-10-17)
**Methodology**: AI-Powered Citation Auditor for academic research
