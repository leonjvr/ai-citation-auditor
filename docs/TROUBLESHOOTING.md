# Troubleshooting Guide

This guide addresses common issues encountered when using the AI-Powered Citation Auditor methodology.

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [Document Processing Problems](#document-processing-problems)
3. [Verification Failures](#verification-failures)
4. [Performance Issues](#performance-issues)
5. [Output Quality Problems](#output-quality-problems)
6. [API and Rate Limiting](#api-and-rate-limiting)
7. [Edge Cases](#edge-cases)

---

## Installation Issues

### Problem: Claude CLI not found

**Symptom:**
```bash
claude: command not found
```

**Solution:**
```bash
# Install Claude CLI following official instructions
# Visit: https://docs.anthropic.com/claude/docs/claude-cli

# Verify installation
claude --version
```

**Expected output:** `Claude CLI v2.0.21` or later

---

### Problem: python-docx installation fails

**Symptom:**
```bash
ERROR: Could not find a version that satisfies the requirement python-docx
```

**Solution:**
```bash
# Update pip first
pip install --upgrade pip

# Install python-docx
pip install python-docx

# Verify installation
python -c "import docx; print(docx.__version__)"
```

---

### Problem: Permission denied when running Claude CLI

**Symptom:**
```bash
Error: This operation requires dangerous mode. Run with --dangerously-skip-permissions
```

**Solution:**
```bash
# Run Claude with permissions flag
claude --dangerously-skip-permissions

# Or set alias in your shell config
alias claude-audit='claude --dangerously-skip-permissions'
```

**Note:** This flag is required for automated file reading and web searches.

---

## Document Processing Problems

### Problem: Cannot read .docx file

**Symptom:**
```
Error: This tool cannot read binary files. The file appears to be a binary .docx file.
```

**Solution:**

Use the extraction script first:
```bash
python protocol/extract_docx.py path/to/your/document.docx > extracted_text.txt
```

Then process the extracted text.

**Alternative:** Open document in Word, save as "Plain Text (.txt)" format.

---

### Problem: UnicodeEncodeError when extracting text

**Symptom:**
```
UnicodeEncodeError: 'charmap' codec can't encode character '\u2010'
```

**Solution:**

The `extract_docx.py` script already handles this. If you still encounter issues:

```python
# Update script with explicit UTF-8 encoding
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
```

Or redirect output to file with UTF-8 encoding:
```bash
python protocol/extract_docx.py document.docx > output.txt
```

---

### Problem: Extracted text is garbled or incomplete

**Symptom:** Missing sections, corrupted characters, tables not extracted properly.

**Possible causes:**
- Complex document formatting (text boxes, headers/footers)
- Embedded objects (images, charts)
- Track changes or comments enabled

**Solutions:**

1. **Remove formatting complexity:**
   - Accept all track changes
   - Remove comments
   - Convert tables to plain text
   - Remove text boxes and embedded objects

2. **Manual extraction:**
   - Copy reference section to new document
   - Save as simple .docx without formatting
   - Re-run extraction

3. **Alternative format:**
   - Save document as .txt or .rtf
   - Use PDF to text conversion (though less reliable)

---

## Verification Failures

### Problem: Too many "UNVERIFIABLE" results

**Symptom:** >20% of references marked as unverifiable despite being legitimate sources.

**Possible causes:**
1. Incomplete reference information in original document
2. Very recent publications (2024-2025) not yet indexed
3. Grey literature (theses, reports, working papers)
4. Non-English sources
5. Regional journals not in major databases
6. Rate limiting from search APIs

**Solutions:**

1. **For incomplete references:**
   - Provide complete author names (including initials)
   - Include DOI if available
   - Specify full journal name (not abbreviation)

2. **For recent publications:**
   - Check author websites for pre-prints
   - Search institutional repositories
   - Verify against journal's own website
   - Note: May need manual verification

3. **For grey literature:**
   - Provide institutional links
   - Include report numbers or identifiers
   - Specify archive or repository location

4. **For non-English sources:**
   - Include English translation of title in brackets
   - Provide database where available (e.g., CNKI for Chinese sources)

5. **For rate limiting:**
   - Add delays between searches (see Performance Issues)
   - Process documents in smaller batches

---

### Problem: False positives (correct references marked as errors)

**Symptom:** References marked as incorrect despite being accurate.

**Common scenarios:**

**1. Journal name changes:**
- "Academy of Management Executive" → "Academy of Management Perspectives" (2006)
- "British Journal of Industrial Relations" → multiple name changes

**Action:** Check journal history; both names may be correct depending on publication year.

**2. Author name variations:**
- "Smith, J." vs "Smith, John" vs "Smith, J. A."
- Compound surnames: "van der Berg" vs "Van Der Berg" vs "Vandenberg"

**Action:** Verify which form author uses officially (check ORCID, institutional profile).

**3. Volume/issue numbering:**
- Some journals restart issue numbering each volume
- Online-first articles may have different pagination in print

**Action:** Verify against journal's own archive.

---

### Problem: Legitimate sources marked as "fabricated"

**Symptom:** Real publications marked as unverifiable.

**Diagnostic steps:**

1. **Search manually in Google Scholar:**
   ```
   intitle:"exact title" author:"surname"
   ```

2. **Check publisher directly:**
   - Visit journal website
   - Search by DOI (if available)
   - Check table of contents for relevant issue

3. **Verify through institutional access:**
   - Many sources behind paywalls not visible to public search
   - Access through university library

4. **Check pre-print servers:**
   - arXiv.org (computer science, physics)
   - SSRN (social sciences)
   - bioRxiv (biology)

**If found:** Document the source and add to audit report with correction note.

**If not found:** May be legitimately fabricated; request original PDF from student.

---

## Performance Issues

### Problem: Processing takes too long

**Symptom:** Audit of 100+ references takes >30 minutes.

**Solutions:**

1. **Reduce context length:**
   - Process reference list separately from main document
   - Audit in batches of 50 references at a time

2. **Optimize search strategy:**
   - Use DOI lookup first (faster than full search)
   - Skip content verification for clearly identifiable sources
   - Focus deep verification on flagged references only

3. **Parallel processing:**
   - Split reference list into sections
   - Run multiple Claude sessions simultaneously
   - Merge results afterward

---

### Problem: Claude stops processing mid-audit

**Symptom:** Output cuts off before completing all references.

**Cause:** Context window limit reached (especially with 500+ references).

**Solutions:**

1. **Batch processing approach:**
   ```bash
   # Process references 1-100
   "Audit references 1-100 from document.docx"

   # Process references 101-200
   "Audit references 101-200 from document.docx"

   # Merge results
   ```

2. **Sampling strategy (for very large bibliographies):**
   - Randomly sample 20% of references (e.g., every 5th reference)
   - Audit sample comprehensively
   - Extrapolate quality metrics

3. **Focus on high-risk references:**
   - Prioritize 2024-2025 publications
   - Focus on non-Q1 journals
   - Verify references with incomplete information

---

## Output Quality Problems

### Problem: Inconsistent formatting in audit report

**Symptom:** Tables misaligned, missing columns, inconsistent sections.

**Solution:**

Specify output format explicitly in prompt:
```
Generate audit report with:
1. Executive Summary (stats table)
2. Verification Table (Reference | Evidence | Accurate? | Notes | Citation Status | SJR)
3. Detailed Analysis
4. Orphan Analysis
5. Quality Distribution
6. Critical Findings
7. Recommendations
```

---

### Problem: Missing SJR (journal quality) information

**Symptom:** Many "N/A" or "Not found" in SJR column.

**Causes:**
- Journal not indexed in SCImago
- Incorrect journal name preventing lookup
- Book chapters, conference proceedings (not journals)

**Solutions:**

1. **For journals:** Search manually at https://www.scimagojr.com/
2. **For books/conferences:** Mark as "N/A (not indexed)" - this is expected
3. **Alternative metrics:** Use Impact Factor, h-index, or ABDC ranking

---

### Problem: Orphan analysis incomplete

**Symptom:** Orphan references identified but no specific list provided.

**Solution:**

Explicitly request:
```
Provide:
1. List of all orphan references (listed but not cited) with reference numbers
2. List of all orphan citations (cited but not listed) with page numbers
3. Citation-reference mismatches with specific errors
```

---

## API and Rate Limiting

### Problem: "Rate limit exceeded" errors

**Symptom:**
```
Error: Too many requests to Semantic Scholar API
Error: Google Scholar blocking requests
```

**Solutions:**

1. **Add delays between searches:**
   ```
   "Process references with 2-second delay between searches"
   ```

2. **Use multiple search engines:**
   - Alternate between Semantic Scholar, Google Scholar, CrossRef
   - Reduce load on any single service

3. **Batch processing with cooldown:**
   - Process 25 references
   - Wait 5 minutes
   - Process next 25 references

4. **Reduce search frequency:**
   - Use DOI direct lookup when available (no rate limit)
   - Cache results for repeated references
   - Skip re-verification of known correct references

---

### Problem: Google Scholar CAPTCHA

**Symptom:** Searches fail with "Please verify you're not a robot" message.

**Solutions:**

1. **Reduce search frequency** (see above)
2. **Switch to Semantic Scholar** as primary source
3. **Use institutional access** (often bypasses CAPTCHA)
4. **Manual verification** for flagged references

---

## Edge Cases

### Problem: Multiple publications with same title and authors

**Scenario:** Conference paper and journal article with identical titles.

**Solution:**
- Verify publication venue (conference vs. journal)
- Check publication year (conference often 1-2 years earlier)
- Confirm page numbers and volume/issue
- Note both versions in audit report

---

### Problem: Retracted publications

**Scenario:** Reference is found but has been retracted.

**Action:**
1. Mark as "FOUND BUT RETRACTED"
2. Include retraction notice link
3. Flag as critical issue requiring removal
4. Recommend replacement source

---

### Problem: Pre-print vs. published version differences

**Scenario:** arXiv/SSRN version cited but published version differs.

**Solution:**
- Verify which version is cited (check year, page numbers)
- If pre-print: Note published version exists
- If published: Mark citation as outdated
- Recommend updating to published version

---

### Problem: Book edition differences

**Scenario:** Reference cites "2nd edition" but databases show "3rd edition" exists.

**Action:**
- Verify cited edition is correct for publication year
- Note if more recent edition available
- Check if page numbers match (may differ between editions)
- Only flag if edition cited doesn't exist

---

### Problem: Translated works

**Scenario:** Original German/French work cited in English translation.

**Solution:**
- Verify both original and translation
- Confirm translation details (translator, year)
- Check citation format follows style guide (APA 7 format for translations)
- Note if original year differs from translation year

---

## Getting Help

If you encounter issues not covered here:

1. **Check documentation:**
   - METHODOLOGY.md - Detailed protocol steps
   - INTERPRETING_RESULTS.md - Understanding audit output
   - CLAUDE.md - Core protocol file

2. **Review examples:**
   - audit-reports/ - See example outputs
   - examples/ - Sample reference formats

3. **Report issues:**
   - GitHub Issues: https://github.com/leonjvr/ai-citation-auditor/issues
   - Include: error message, document type, reference count
   - Attach: anonymized audit report (if applicable)

4. **Community support:**
   - Search existing GitHub issues
   - Check if others encountered similar problems
   - Share solutions that worked for you

---

## Prevention Best Practices

**For Students:**
- Use reference management software (Zotero, Mendeley, EndNote)
- Cite as you write (don't add references retroactively)
- Verify references before submission
- Run self-audit early in writing process

**For Supervisors:**
- Request audits at proposal stage (not final draft)
- Review high-risk references manually
- Use audits as teaching tools, not punishment
- Maintain realistic expectations (tool is screening, not definitive)

**For Institutions:**
- Provide training on citation management
- Offer workshops on using audit tools
- Set clear quality expectations
- Support students with writing center resources

---

**Last Updated**: 2025-10-17
**Version**: 1.0.0
