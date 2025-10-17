#!/usr/bin/env python3
"""
Extract reference lists from downloaded papers for citation auditing.

This script extracts the reference section from downloaded PDFs and prepares
them for systematic citation auditing using the CLAUDE.md protocol.

Usage:
    python extract_references.py --papers-dir ../temp_papers --output extracted_refs

Author: LJ Janse van Rensburg
License: MIT
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional


def extract_references_section(text: str) -> Optional[str]:
    """
    Extract the references/bibliography section from paper text.

    Args:
        text: Full text of the paper

    Returns:
        References section text, or None if not found
    """
    # Common reference section headers - use more flexible patterns
    ref_patterns = [
        r'(?:^|\n)References\s*\n',
        r'(?:^|\n)REFERENCES\s*\n',
        r'(?:^|\n)Bibliography\s*\n',
        r'(?:^|\n)BIBLIOGRAPHY\s*\n',
        r'(?:^|\n)Literature Cited\s*\n',
        r'(?:^|\n)Works Cited\s*\n',
    ]

    # Try to find references section
    for pattern in ref_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            # Extract everything after this header
            start_pos = match.end()

            # Look for common end markers (acknowledgments, appendices, etc.)
            end_patterns = [
                r'(?:^|\n)(?:Acknowledgments|Acknowledgements|Appendix|Supporting Information|Author Contributions|Competing interests|Data Availability)',
            ]

            end_pos = len(text)
            for end_pattern in end_patterns:
                end_match = re.search(end_pattern, text[start_pos:], re.IGNORECASE | re.MULTILINE)
                if end_match:
                    end_pos = start_pos + end_match.start()
                    break

            return text[start_pos:end_pos].strip()

    return None


def parse_numbered_references(ref_text: str) -> List[str]:
    """
    Parse numbered reference list (e.g., "1. Author et al...")

    Args:
        ref_text: Raw references section text

    Returns:
        List of individual references
    """
    # Split by numbered patterns like "1.", "2.", etc. at line start
    pattern = r'(?:^|\n)\s*(\d+)\.\s+'
    parts = re.split(pattern, ref_text, flags=re.MULTILINE)

    references = []

    # Parts alternate: ['preamble', '1', 'ref1 text', '2', 'ref2 text', ...]
    for i in range(1, len(parts), 2):
        if i+1 < len(parts):
            ref_num = parts[i]
            ref_text_content = parts[i+1].strip()
            # Clean up the reference text - remove excessive whitespace
            ref_text_content = ' '.join(ref_text_content.split())
            if ref_text_content:  # Only add non-empty references
                references.append(f"[{ref_num}] {ref_text_content}")

    return references


def parse_bracketed_references(ref_text: str) -> List[str]:
    """
    Parse bracketed reference list (e.g., "[1] Author et al...")

    Args:
        ref_text: Raw references section text

    Returns:
        List of individual references
    """
    # Split by bracketed patterns like "[1]", "[2]", etc.
    pattern = r'(?:^|\n)\s*\[(\d+)\]\s+'
    parts = re.split(pattern, ref_text, flags=re.MULTILINE)

    references = []

    for i in range(1, len(parts), 2):
        if i+1 < len(parts):
            ref_num = parts[i]
            ref_text_content = parts[i+1].strip()
            # Clean up the reference text - remove excessive whitespace
            ref_text_content = ' '.join(ref_text_content.split())
            if ref_text_content:  # Only add non-empty references
                references.append(f"[{ref_num}] {ref_text_content}")

    return references


def extract_references_from_pdf(pdf_path: Path) -> Dict:
    """
    Extract references from a PDF file using pdfplumber.

    Args:
        pdf_path: Path to PDF file

    Returns:
        Dictionary with extracted references and metadata
    """
    try:
        # Try using pdfplumber for better text extraction
        import pdfplumber

        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if not text.strip():
            return {
                'filename': pdf_path.name,
                'status': 'no_text_extracted',
                'error': 'Could not extract text from PDF',
                'references': []
            }

        # Extract references section
        ref_section = extract_references_section(text)

        if not ref_section:
            return {
                'filename': pdf_path.name,
                'status': 'no_refs_found',
                'error': 'Could not locate references section',
                'references': [],
                'debug_info': f'Text length: {len(text)}, First 500 chars: {text[:500]}'
            }

        # Try to parse references
        references = []

        # Try bracketed format first [1], [2], etc.
        if re.search(r'(?:^|\n)\s*\[1\]', ref_section, re.MULTILINE):
            references = parse_bracketed_references(ref_section)
        # Try numbered format 1., 2., etc.
        elif re.search(r'(?:^|\n)\s*1\.\s+', ref_section, re.MULTILINE):
            references = parse_numbered_references(ref_section)
        else:
            # Fallback: try to split by patterns that look like reference starts
            # Look for author names followed by year in parentheses
            ref_pattern = r'(?:^|\n)([A-Z][^\n]+?(?:\(\d{4}\)|,\s*\d{4}).*?)(?=\n[A-Z]|\n\n|$)'
            matches = re.findall(ref_pattern, ref_section, re.MULTILINE | re.DOTALL)
            if matches:
                references = [f"[{i+1}] {' '.join(m.split())}" for i, m in enumerate(matches) if m.strip()]
            else:
                # Last resort: split by double newlines
                references = [f"[{i+1}] {' '.join(r.split())}" for i, r in enumerate(ref_section.split('\n\n')) if r.strip()]

        return {
            'filename': pdf_path.name,
            'status': 'success' if references else 'no_refs_parsed',
            'reference_count': len(references),
            'references': references,
            'raw_section_preview': ref_section[:1000] + '...' if len(ref_section) > 1000 else ref_section
        }

    except ImportError:
        return {
            'filename': pdf_path.name,
            'status': 'error',
            'error': 'pdfplumber not installed. Install with: pip install pdfplumber',
            'references': []
        }
    except Exception as e:
        return {
            'filename': pdf_path.name,
            'status': 'error',
            'error': str(e),
            'references': []
        }


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Extract references from downloaded papers"
    )
    parser.add_argument(
        '--papers-dir',
        type=str,
        default='../temp_papers',
        help='Directory containing downloaded PDFs'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='extracted_references',
        help='Output directory for extracted references'
    )
    parser.add_argument(
        '--dataset',
        type=str,
        default='../datasets/validation_dataset.json',
        help='Path to validation dataset for metadata'
    )

    args = parser.parse_args()

    papers_dir = Path(args.papers_dir)
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True, parents=True)

    # Load dataset metadata
    with open(args.dataset, 'r', encoding='utf-8') as f:
        dataset = json.load(f)

    papers = dataset.get('papers', [])

    print(f"Extracting references from PDFs in {papers_dir}...")
    print("=" * 60)

    results = []

    # Process each PDF
    pdf_files = list(papers_dir.glob("*.pdf"))

    if not pdf_files:
        print(f"No PDF files found in {papers_dir}")
        return

    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] Processing: {pdf_path.name[:60]}...")

        result = extract_references_from_pdf(pdf_path)
        results.append(result)

        if result['status'] == 'success':
            print(f"  [OK] Extracted {result['reference_count']} references")

            # Save individual reference file
            ref_file = output_dir / f"{pdf_path.stem}_references.json"
            with open(ref_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
        else:
            print(f"  [FAILED] {result.get('error', 'Unknown error')}")

    # Save summary
    summary = {
        'total_papers': len(results),
        'successful': len([r for r in results if r['status'] == 'success']),
        'failed': len([r for r in results if r['status'] != 'success']),
        'results': results
    }

    summary_file = output_dir / 'extraction_summary.json'
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print("EXTRACTION SUMMARY")
    print("=" * 60)
    print(f"Total papers: {summary['total_papers']}")
    print(f"Successful extractions: {summary['successful']}")
    print(f"Failed extractions: {summary['failed']}")

    if summary['successful'] > 0:
        total_refs = sum(r['reference_count'] for r in results if r['status'] == 'success')
        avg_refs = total_refs / summary['successful']
        print(f"\nTotal references extracted: {total_refs}")
        print(f"Average references per paper: {avg_refs:.1f}")

    print(f"\nReferences saved to: {output_dir}")
    print(f"Summary saved to: {summary_file}")


if __name__ == '__main__':
    main()
