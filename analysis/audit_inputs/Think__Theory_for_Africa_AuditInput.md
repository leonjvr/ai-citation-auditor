# CITATION AUDIT REQUEST

**Document**: Think__Theory_for_Africa.pdf
**Total References**: 16
**Audit Protocol**: CLAUDE.md - AI-Powered Citation Auditor v1.0

---

## TASK: Systematic Reference Verification

Following the **Reference Checking Protocol for Academic Documents** (CLAUDE.md), perform a comprehensive citation audit of this document with **absolute strictness and zero tolerance for assumptions**.

### Complete Reference List

The following references were extracted from the document's reference section:

[1] MarrD,PoggioT.FromUnderstandingComputationtoUnderstandingNeuralCircuitry. Massachusetts InstituteofTechnologyArtificialIntelligenceLaboratory.1976.p.1–22.

[2] FakhouryM.Neuralprosthesesforrestoringfunctionslostafterspinalcordinjury.NeuralRegenRes. 2015;10(10):1594–5.https://doi.org/10.4103/1673-5374.165267PMID:26692853

[3] YanagisawaT,HirataM,SaitohY,KishimaH,MatsushitaK,GotoT,etal.ElectrocorticographicControl ofaProstheticHandinParalyzedPatients.In:GugerC,AllisonB,LeuthardtEC,editors.Brain-Com- puterInterfaceResearch:AState-of-the-ArtSummary-2. Berlin,Heidelberg: SpringerBerlinHeidel- berg;2014.p.95–103.

[4] HassabisD,KumaranD,SummerfieldC,BotvinickM.Neuroscience-InspiredArtificialIntelligence. Neuron.2017;95(2):245–58.https://doi.org/10.1016/j.neuron.2017.06.011PMID:28728020

[5] AmuntsK,EbellC,MullerJ,TelefontM,KnollA,LippertT.TheHumanBrainProject:CreatingaEuro- peanResearchInfrastructuretoDecodetheHumanBrain.Neuron.2016;92(3):574–81.https://doi.org/ 10.1016/j.neuron.2016.10.046PMID:27809997

[6] JabalpurwalaI.BrainCanada:OneBrainOneCommunity.Neuron.2016;92(3):601–6.https://doi.org/ 10.1016/j.neuron.2016.10.049PMID:27810001

[7] MartinCL,ChunM.TheBRAINInitiative:Building,Strengthening,andSustaining.Neuron.2016;92 (3):570–3.https://doi.org/10.1016/j.neuron.2016.10.039PMID:27809996

[8] SunkinSM,NgL,LauC,DolbeareT,GilbertTL,ThompsonCL,etal.AllenBrainAtlas:anintegrated spatio-temporalportalforexploringthecentralnervoussystem.NucleicAcidsRes.2013;41(Database issue):D996–1008.https://doi.org/10.1093/nar/gks1042PMID:23193282

[9] BalogunWG,CobhamAE,AminA.NeuroscienceinNigeria:thepast,thepresentandthefuture. MetabBrainDis.2018;33(2):359–68.https://doi.org/10.1007/s11011-017-0119-9PMID:28993966

[10] MainaMB,GarbaYM,BukarAM,AhmadU,SalihuA,IbrahumH,etal.AfricanNeuroscienceonthe GlobalStage:NigeriaasaModel.AfricArXiv.2018;(July):1–19.

[11] BalogunWG,CobhamAE,AminA,SeeniA.AdvancingNeuroscienceResearchinAfrica:Invertebrate SpeciestotheRescue.Neuroscience.2018;374(15March2018):323–5.https://doi.org/10.1016/j. neuroscience.2018.01.062PMID:29427653

[12] BadenT,JamesB,ZimmermannMJY,BartelP,GrijseelsD,EulerT,etal.Spikeling:Alow-costhard- wareimplementationofaspikingneuronforneuroscienceteachingandoutreach.PLoSBiol.2018;16 (10):e2006760.https://doi.org/10.1371/journal.pbio.2006760PMID:30365493 PLOSComputationalBiology|https://doi.org/10.1371/journal.pcbi.1007049 July11,2019 4/5

[13] BhogalN.TheroleoftheSquareKilometreArrayinSouthAfrica’seconomicdevelopmentstrategy.S AfrJSci.2018;114(3):1–7.

[14] MulderN,AdebamowoCACA,AdebamowoSNSN,AdebayoO,AdeleyeO,AlibiM,etal.Genomic researchdatageneration,analysisandsharing–challengesintheAfricansetting.DataSciJ.2017;16 (0):1–15.

[15] KarikariTK,AleksicJ.Neurogenomics:Anopportunitytointegrateneuroscience,genomicsandbioin- formaticsresearchinAfrica.ApplTranslgenomics.2015;5:3–10.

[16] SivagnanamS,MajumdarA,YoshimotoK,AstakhovV,BandrowskiA,MartoneM,etal.Introducing theneurosciencegateway.CEURWorkshopProc.2013;993. PLOSComputationalBiology|https://doi.org/10.1371/journal.pcbi.1007049 July11,2019 5/5


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
**Methodology**: AI-Powered Citation Auditor for Agents4Science 2025
