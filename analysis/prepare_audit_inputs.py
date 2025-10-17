#!/usr/bin/env python3
"""
Prepare extracted references for citation auditing using CLAUDE.md protocol.

This script takes the extracted references from PDFs and formats them into
audit-ready input files that can be systematically processed according to
the AI-Powered Citation Auditor methodology.

Usage:
    python prepare_audit_inputs.py --refs-dir extracted_references --output audit_inputs

Author: LJ Janse van Rensburg
License: MIT
"""

import os
import json
import argparse
from pathlib import Path
from typing import Dict, List


class AuditInputPreparer:
    """Prepares extracted references for systematic citation auditing."""

    def __init__(self, refs_dir: str, output_dir: str):
        """
        Initialize the audit input preparer.

        Args:
            refs_dir: Directory containing extracted reference JSON files
            output_dir: Directory to save audit-ready input files
        """
        self.refs_dir = Path(refs_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)

    def load_extracted_references(self) -> List[Dict]:
        """
        Load all extracted reference JSON files.

        Returns:
            List of paper dictionaries with extracted references
        """
        papers = []

        json_files = list(self.refs_dir.glob("*_references.json"))

        for json_file in json_files:
            if json_file.name == "extraction_summary.json":
                continue

            with open(json_file, 'r', encoding='utf-8') as f:
                paper_data = json.load(f)
                papers.append(paper_data)

        print(f"Loaded {len(papers)} papers with extracted references")
        return papers

    def create_audit_prompt(self, paper_data: Dict) -> str:
        """
        Create the audit prompt for a single paper following CLAUDE.md protocol.

        Args:
            paper_data: Dictionary containing filename, references, and metadata

        Returns:
            Formatted audit prompt string
        """
        filename = paper_data['filename']
        reference_count = paper_data['reference_count']
        references = paper_data['references']

        # Create the audit prompt based on CLAUDE.md protocol
        prompt = f"""# CITATION AUDIT REQUEST

**Document**: {filename}
**Total References**: {reference_count}
**Audit Protocol**: CLAUDE.md - AI-Powered Citation Auditor v1.0

---

## TASK: Systematic Reference Verification

Following the **Reference Checking Protocol for Academic Documents** (CLAUDE.md), perform a comprehensive citation audit of this document with **absolute strictness and zero tolerance for assumptions**.

### Complete Reference List

The following references were extracted from the document's reference section:

"""

        # Add all references
        for ref in references:
            prompt += f"{ref}\n\n"

        prompt += """
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
"""

        return prompt

    def prepare_all_audit_inputs(self) -> Dict:
        """
        Prepare audit input files for all papers.

        Returns:
            Dictionary with preparation statistics
        """
        papers = self.load_extracted_references()

        prepared = []

        print("\nPreparing audit input files...")
        print("=" * 60)

        for i, paper_data in enumerate(papers, 1):
            filename = paper_data['filename']
            print(f"\n[{i}/{len(papers)}] Preparing: {filename[:60]}...")

            # Create audit prompt
            audit_prompt = self.create_audit_prompt(paper_data)

            # Save to file
            base_name = filename.replace('.pdf', '')
            output_file = self.output_dir / f"{base_name}_AuditInput.md"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(audit_prompt)

            prepared.append({
                'paper': filename,
                'references': paper_data['reference_count'],
                'input_file': str(output_file)
            })

            print(f"  Created: {output_file.name}")
            print(f"  References to audit: {paper_data['reference_count']}")

        print("\n" + "=" * 60)
        print(f"Prepared {len(prepared)} audit input files")

        return {
            'total_papers': len(prepared),
            'total_references': sum(p['references'] for p in prepared),
            'papers': prepared
        }

    def create_audit_batch_manifest(self, stats: Dict) -> None:
        """
        Create a manifest file for batch audit processing.

        Args:
            stats: Preparation statistics dictionary
        """
        manifest = {
            'batch_info': {
                'total_papers': stats['total_papers'],
                'total_references': stats['total_references'],
                'audit_protocol': 'CLAUDE.md v1.0',
                'methodology': 'AI-Powered Citation Auditor',
                'purpose': 'Validation for academic research conference paper'
            },
            'papers': stats['papers']
        }

        manifest_file = self.output_dir / 'audit_batch_manifest.json'

        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)

        print(f"\nBatch manifest saved to: {manifest_file}")

    def create_readme(self) -> None:
        """Create README for the audit inputs directory."""
        readme_content = f"""# Citation Audit Input Files

## Purpose

This directory contains prepared input files for systematic citation auditing using the **AI-Powered Citation Auditor** methodology described in the CLAUDE.md protocol.

## Contents

- **24 audit input files** (one per paper in validation dataset)
- **audit_batch_manifest.json** - Batch processing manifest
- **README.md** - This file

## Input File Format

Each `*_AuditInput.md` file contains:

1. **Document metadata** - Paper filename and reference count
2. **Complete reference list** - All extracted references from the paper
3. **Verification requirements** - Detailed checklist following CLAUDE.md protocol
4. **Output format specification** - Required audit report structure
5. **Strict verification standards** - Zero-assumption policy and marking criteria

## How to Use These Files

### Option 1: Manual Audit (Using Claude or ChatGPT with Agentic Mode)

1. Open one `*_AuditInput.md` file
2. Copy the entire content
3. Paste into Claude (Projects mode) or ChatGPT (with web search enabled)
4. The AI agent will systematically audit all references
5. Save the generated `*_ReferenceAudit.md` report

### Option 2: Batch Processing (Programmatic)

1. Load `audit_batch_manifest.json`
2. Iterate through each paper's input file
3. Submit to AI agent API with tool access (Semantic Scholar, Google Scholar, CrossRef)
4. Collect generated audit reports
5. Run aggregate statistics analysis

## Expected Output

For each input file, the audit process should generate:

- `[PaperName]_ReferenceAudit.md` - Comprehensive citation audit report
- Verification status for all references
- Quality metrics (SJR scores, quartiles)
- Critical findings (fabricated refs, misrepresentations)
- Recommendations for authors and supervisors

## Validation Metrics to Track

When running audits, track:

- **Verification rate**: % of references successfully verified
- **Time per paper**: How long each audit takes
- **Issue detection rate**: % of papers with critical issues
- **Fabricated reference detection**: Count of suspected fabrications
- **Quality distribution**: Q1/Q2/Q3/Q4 journal breakdown

## Next Steps

1. Run audits on all 24 papers
2. Collect audit reports in `../audit_reports/` directory
3. Run `statistics.py` to generate aggregate statistics
4. Analyze results for academic research paper

---

**Protocol**: CLAUDE.md v1.0
**Methodology**: AI-Powered Citation Auditor
**Purpose**: Statistical validation for conference publication
"""

        readme_file = self.output_dir / 'README.md'

        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"README saved to: {readme_file}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Prepare extracted references for citation auditing"
    )
    parser.add_argument(
        '--refs-dir',
        type=str,
        default='extracted_references',
        help='Directory containing extracted reference JSON files'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='audit_inputs',
        help='Output directory for audit input files'
    )

    args = parser.parse_args()

    # Initialize preparer
    preparer = AuditInputPreparer(args.refs_dir, args.output)

    # Prepare all audit inputs
    stats = preparer.prepare_all_audit_inputs()

    # Create batch manifest
    preparer.create_audit_batch_manifest(stats)

    # Create README
    preparer.create_readme()

    # Print summary
    print("\n" + "=" * 60)
    print("PREPARATION SUMMARY")
    print("=" * 60)
    print(f"Total papers prepared: {stats['total_papers']}")
    print(f"Total references to audit: {stats['total_references']:,}")
    print(f"Average references per paper: {stats['total_references']/stats['total_papers']:.1f}")

    print(f"\nAudit input files saved to: {args.output}")
    print("\nNext step: Run citation audits using CLAUDE.md protocol")
    print("  Option 1: Manual audit using Claude/ChatGPT (copy-paste input files)")
    print("  Option 2: Batch processing using API (requires implementation)")


if __name__ == '__main__':
    main()
