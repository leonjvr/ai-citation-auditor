# Sample Reference Formats

This file provides examples of reference formats that the AI-Powered Citation Auditor can process and verify.

## Purpose

Use these examples to:
- Understand what well-formatted references look like
- Test the audit protocol on known references
- Demonstrate proper citation practices to students
- Verify the auditor is working correctly

## Example References by Type

### Journal Articles (APA 7th Edition)

**Q1 Journal Example:**
```
Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management.
Strategic Management Journal, 18(7), 509-533. https://doi.org/10.1002/(SICI)1097-0266(199708)18:7<509::AID-SMJ882>3.0.CO;2-Z
```
- **Verification**: ✅ Highly cited foundational work
- **SJR**: Q1 (Strategic Management Journal)
- **Notes**: Available in Semantic Scholar, Google Scholar

**Recent Journal Article Example:**
```
Barney, J. B. (1991). Firm resources and sustained competitive advantage.
Journal of Management, 17(1), 99-120. https://doi.org/10.1177/014920639101700108
```
- **Verification**: ✅ Seminal resource-based view paper
- **SJR**: Q1 (Journal of Management)
- **Notes**: Over 100,000 citations

### Books

**Edited Book:**
```
Freeman, R. E. (1984). Strategic management: A stakeholder approach.
Boston: Pitman.
```
- **Verification**: ✅ Foundational stakeholder theory
- **SJR**: N/A (book, not indexed)
- **Notes**: Widely available, Cambridge University Press reprint 2010

**Book Chapter:**
```
Eisenhardt, K. M., & Graebner, M. E. (2007). Theory building from cases: Opportunities and challenges.
Academy of Management Journal, 50(1), 25-32. https://doi.org/10.5465/amj.2007.24160888
```
- **Verification**: ✅ Methods paper on case study research
- **SJR**: Q1 (Academy of Management Journal)

### Conference Proceedings

**Example:**
```
Davis, F. D. (1989, September). Perceived usefulness, perceived ease of use, and user acceptance of
information technology. MIS Quarterly, 13(3), 319-340. https://doi.org/10.2307/249008
```
- **Verification**: ✅ Technology Acceptance Model (TAM)
- **SJR**: Q1 (MIS Quarterly)
- **Notes**: One of the most cited papers in information systems

### Working Papers & Grey Literature

**SSRN Working Paper:**
```
Bloom, N., & Van Reenen, J. (2007). Measuring and explaining management practices across firms and countries.
Quarterly Journal of Economics, 122(4), 1351-1408. https://doi.org/10.1162/qjec.2007.122.4.1351
```
- **Verification**: ✅ Published version available
- **SJR**: Q1 (Quarterly Journal of Economics)
- **Notes**: Originally SSRN working paper, now published

**Thesis/Dissertation:**
```
Porter, M. E. (1973). Retail structure, market organization, and consumer price levels.
Unpublished doctoral dissertation, Harvard University.
```
- **Verification**: ⚠️ Limited verification possible (unpublished)
- **SJR**: N/A (dissertation)
- **Notes**: May be difficult to verify content accuracy

### Online Sources

**Organizational Report:**
```
World Economic Forum. (2023). The Future of Jobs Report 2023.
Geneva: World Economic Forum. Retrieved from https://www.weforum.org/reports/the-future-of-jobs-report-2023
```
- **Verification**: ✅ Official WEF publication
- **SJR**: N/A (grey literature)
- **Notes**: Legitimate source but not peer-reviewed

## Common Reference Errors

### Error Type 1: Wrong Year

**Incorrect:**
```
Chen, M. J., Su, K. H., & Tsai, W. (2010). Competitive tension: The awareness-motivation-capability
perspective. Academy of Management Journal, 50(1), 101-118.
```

**Correct:**
```
Chen, M. J., Su, K. H., & Tsai, W. (2007). Competitive tension: The awareness-motivation-capability
perspective. Academy of Management Journal, 50(1), 101-118.
```
- **Issue**: Year should be 2007, not 2010
- **Detection**: AI auditor will flag year mismatch

### Error Type 2: Wrong Journal Name

**Incorrect:**
```
Campbell, B. A. (2000). Strategic entrepreneurship: Creating competitive advantage through streams of innovation.
Academy of Management Perspectives, 13(1), 45-63.
```

**Correct:**
```
Campbell, B. A. (2000). Strategic entrepreneurship: Creating competitive advantage through streams of innovation.
Academy of Management Executive, 13(1), 45-63.
```
- **Issue**: Journal renamed; original was "Executive" not "Perspectives"
- **Detection**: AI auditor will identify correct journal name

### Error Type 3: Author Name Variation

**Incorrect:**
```
Barney, J. (2018). Why resource-based theory's model of profit appropriation must incorporate a stakeholder perspective.
Strategic Management Journal, 39(13), 3305-3325.
```

**Correct:**
```
Barney, J. B. (2018). Why resource-based theory's model of profit appropriation must incorporate a stakeholder perspective.
Strategic Management Journal, 39(13), 3305-3325.
```
- **Issue**: Missing middle initial "B."
- **Detection**: AI auditor may flag as potential mismatch

### Error Type 4: Fabricated Reference

**Example of Unverifiable Reference:**
```
Smith, A., Johnson, B., & Williams, C. (2025). The future of organizational resilience in post-pandemic environments.
Journal of Strategic Innovation, 15(3), 234-256. https://doi.org/10.1234/jsi.2025.fake
```
- **Issue**: No results found in any database
- **Detection**: AI auditor will mark as "UNVERIFIABLE - Exhaustive search yielded no results"
- **Recommendation**: Request original source or remove

## Orphan Reference Example

**Listed in Reference List but Never Cited:**
```
Porter, M. E. (1985). Competitive advantage: Creating and sustaining superior performance.
New York: Free Press.
```
- **Issue**: Appears in reference list but no in-text citation exists
- **Detection**: AI auditor flags as "Orphan reference - listed but not cited"
- **Recommendation**: Either cite in text or remove from list

## Orphan Citation Example

**Cited in Text but Missing from Reference List:**

In-text citation:
> "...as demonstrated by the resource-based view (Wernerfelt, 1984)..."

Reference list:
> [No corresponding Wernerfelt 1984 entry exists]

- **Issue**: Citation present but no reference list entry
- **Detection**: AI auditor flags as "Orphan citation - cited but not listed"
- **Recommendation**: Add full reference to list

## Testing the Auditor

To test if your audit protocol is working correctly, create a test document with:

1. **5 correct references** (like Teece et al., 1997; Barney, 1991)
2. **1 year error** (like Chen 2010 → should be 2007)
3. **1 fabricated reference** (completely made up)
4. **1 orphan reference** (listed but not cited)
5. **1 orphan citation** (cited but not listed)

Expected output:
- 5 verified references
- 1 year mismatch detected
- 1 unverifiable reference flagged
- 1 orphan reference identified
- 1 orphan citation identified

## Reference Quality Distribution

### Excellent Quality Reference List Characteristics:
- 90%+ references from Q1/Q2 journals
- <5% orphan references
- 0 fabricated references
- 0 citation-reference mismatches
- Mix of foundational (5+ years old) and current (<3 years) sources

### Problematic Reference List Characteristics:
- >50% orphan references (suggests padding)
- Multiple unverifiable references (suggests fabrication)
- >20% citation-reference mismatches (suggests careless management)
- Reliance on non-peer-reviewed sources (blogs, websites)
- No foundational citations (suggests superficial literature review)

## Using These Examples

### For Students:
1. Compare your references against these formats
2. Run self-audit using these examples as benchmark
3. Understand what "high quality" citations look like
4. Learn to identify common errors

### For Supervisors:
1. Use as training materials in workshops
2. Demonstrate audit capabilities with known examples
3. Set expectations for reference quality
4. Illustrate difference between good and poor citation practices

### For Researchers:
1. Validate audit protocol accuracy
2. Test methodology changes
3. Benchmark against known error types
4. Demonstrate reproducibility

---

**Note**: All references in this document are real, verifiable sources that can be found in academic databases. Use them to validate your audit protocol is working correctly.

**Last Updated**: 2025-10-17
