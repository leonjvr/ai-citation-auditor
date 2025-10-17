#!/usr/bin/env python3
"""
Batch runner for citation audits on all validation papers.

This script reads all audit input files and generates a comprehensive
processing plan for systematic citation auditing.

Usage:
    python run_all_audits.py

Author: LJ Janse van Rensburg
License: MIT
"""

import json
from pathlib import Path

def main():
    # Directories
    audit_inputs_dir = Path("audit_inputs")
    audit_reports_dir = Path("audit_reports")

    # Load batch manifest
    manifest_file = audit_inputs_dir / "audit_batch_manifest.json"
    with open(manifest_file, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    print("=" * 70)
    print("CITATION AUDIT BATCH PROCESSING PLAN")
    print("=" * 70)
    print(f"\nTotal papers to audit: {manifest['batch_info']['total_papers']}")
    print(f"Total references to verify: {manifest['batch_info']['total_references']:,}")
    print(f"Protocol: {manifest['batch_info']['audit_protocol']}")
    print(f"Methodology: {manifest['batch_info']['methodology']}")

    print("\n" + "=" * 70)
    print("PAPERS TO PROCESS")
    print("=" * 70)

    for i, paper in enumerate(manifest['papers'], 1):
        print(f"\n[{i}/24] {paper['paper']}")
        print(f"  References: {paper['references']}")
        print(f"  Input file: {Path(paper['input_file']).name}")
        print(f"  Expected output: {Path(paper['input_file']).stem.replace('_AuditInput', '_ReferenceAudit.md')}")

    print("\n" + "=" * 70)
    print("PROCESSING STRATEGY")
    print("=" * 70)

    # Group papers by size
    small = [p for p in manifest['papers'] if p['references'] <= 25]
    medium = [p for p in manifest['papers'] if 25 < p['references'] <= 55]
    large = [p for p in manifest['papers'] if p['references'] > 55]

    print(f"\nSmall papers (≤25 refs): {len(small)} papers, {sum(p['references'] for p in small)} refs")
    print(f"Medium papers (26-55 refs): {len(medium)} papers, {sum(p['references'] for p in medium)} refs")
    print(f"Large papers (>55 refs): {len(large)} papers, {sum(p['references'] for p in large)} refs")

    print("\n" + "=" * 70)
    print("RECOMMENDED PROCESSING ORDER")
    print("=" * 70)

    print("\nBatch 1 - Small papers (quick validation):")
    for paper in sorted(small, key=lambda x: x['references'])[:5]:
        print(f"  - {Path(paper['paper']).stem[:60]}: {paper['references']} refs")

    print("\nBatch 2 - Medium papers:")
    for paper in sorted(medium, key=lambda x: x['references'])[:5]:
        print(f"  - {Path(paper['paper']).stem[:60]}: {paper['references']} refs")

    print("\nBatch 3 - Large papers (most time-intensive):")
    for paper in sorted(large, key=lambda x: x['references']):
        print(f"  - {Path(paper['paper']).stem[:60]}: {paper['references']} refs")

    print("\n" + "=" * 70)
    print("IMPLEMENTATION NOTES")
    print("=" * 70)
    print("""
This batch processing plan provides a roadmap for systematic auditing.

For automated processing:
1. Read each audit input file
2. Submit to AI agent with tool access (Semantic Scholar, Google Scholar, SJR)
3. Collect generated audit reports
4. Save to audit_reports/ directory
5. Track progress and errors

For manual processing:
1. Copy audit input file content
2. Paste into Claude/ChatGPT with agentic mode
3. Wait for comprehensive audit report
4. Save generated report to audit_reports/
5. Move to next paper

Estimated time:
- Small papers: ~10-15 min each
- Medium papers: ~15-25 min each
- Large papers: ~30-45 min each
- Total: ~8-12 hours for all 24 papers (manual)
- Total: ~2-4 hours (automated batch processing)
""")

if __name__ == '__main__':
    main()
