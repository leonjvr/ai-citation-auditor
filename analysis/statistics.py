#!/usr/bin/env python3
"""
AI-Powered Citation Auditor - Aggregate Statistics Analyzer

This script analyzes multiple audit reports and generates aggregate statistics
for research reporting and methodology validation.

Usage:
    python statistics.py --reports-dir ../audit-reports --output summary_stats.md

Author: LJ Janse van Rensburg
License: MIT
"""

import os
import re
import json
import argparse
from typing import Dict, List, Tuple
from pathlib import Path


class AuditStatistics:
    """Analyzes audit reports and generates aggregate statistics."""

    def __init__(self, reports_dir: str):
        """
        Initialize the statistics analyzer.

        Args:
            reports_dir: Path to directory containing audit report markdown files
        """
        self.reports_dir = Path(reports_dir)
        self.reports = []
        self.aggregate_stats = {}

    def load_reports(self) -> None:
        """Load all audit report markdown files from the reports directory."""
        markdown_files = list(self.reports_dir.glob("*_ReferenceAudit.md"))

        for file_path in markdown_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.reports.append({
                    'filename': file_path.name,
                    'content': content
                })

        print(f"Loaded {len(self.reports)} audit reports")

    def extract_metrics(self, report_content: str) -> Dict:
        """
        Extract key metrics from an audit report.

        Args:
            report_content: Raw markdown content of audit report

        Returns:
            Dictionary of extracted metrics
        """
        metrics = {
            'total_references': 0,
            'total_citations': 0,
            'verified_references': 0,
            'unverifiable_references': 0,
            'orphan_references': 0,
            'orphan_citations': 0,
            'citation_mismatches': 0,
            'q1_journals': 0,
            'q2_journals': 0,
            'q3_journals': 0,
            'q4_journals': 0,
            'not_indexed': 0,
            'fabricated_references': 0,
            'verification_rate': 0.0,
            'orphan_reference_rate': 0.0,
            'quality_rating': 'Unknown'
        }

        # Extract total references
        match = re.search(r'\*\*Total References\*\*:\s*(\d+)', report_content)
        if match:
            metrics['total_references'] = int(match.group(1))

        # Extract total citations
        match = re.search(r'\*\*Total Citations\*\*:\s*(\d+)', report_content)
        if match:
            metrics['total_citations'] = int(match.group(1))

        # Extract verification rate
        match = re.search(r'\*\*Verification Success Rate\*\*:\s*(\d+(?:\.\d+)?)%', report_content)
        if match:
            metrics['verification_rate'] = float(match.group(1))

        # Extract unverifiable count
        match = re.search(r'(\d+)\s+unverifiable', report_content, re.IGNORECASE)
        if match:
            metrics['unverifiable_references'] = int(match.group(1))

        # Extract fabricated count
        match = re.search(r'(\d+)\s+(?:fabricated|potentially fabricated)', report_content, re.IGNORECASE)
        if match:
            metrics['fabricated_references'] = int(match.group(1))

        # Extract orphan references
        match = re.search(r'(\d+)\s+orphan references', report_content, re.IGNORECASE)
        if match:
            metrics['orphan_references'] = int(match.group(1))

        # Extract orphan citations
        match = re.search(r'(\d+)\s+orphan citations', report_content, re.IGNORECASE)
        if match:
            metrics['orphan_citations'] = int(match.group(1))

        # Extract quality rating
        if '🟢' in report_content or 'EXCELLENT' in report_content or 'HIGH QUALITY' in report_content:
            metrics['quality_rating'] = 'High'
        elif '🟡' in report_content or 'MODERATE' in report_content or 'ACCEPTABLE' in report_content:
            metrics['quality_rating'] = 'Moderate'
        elif '🔴' in report_content or 'CRITICAL' in report_content or 'MAJOR REVISION' in report_content:
            metrics['quality_rating'] = 'Critical'

        # Calculate orphan rate if we have the data
        if metrics['total_references'] > 0:
            metrics['orphan_reference_rate'] = (metrics['orphan_references'] / metrics['total_references']) * 100

        # Estimate verified references from verification rate
        if metrics['verification_rate'] > 0 and metrics['total_references'] > 0:
            metrics['verified_references'] = int((metrics['verification_rate'] / 100) * metrics['total_references'])

        return metrics

    def calculate_aggregate_stats(self) -> Dict:
        """
        Calculate aggregate statistics across all reports.

        Returns:
            Dictionary of aggregate statistics
        """
        all_metrics = []

        for report in self.reports:
            metrics = self.extract_metrics(report['content'])
            metrics['filename'] = report['filename']
            all_metrics.append(metrics)

        # Calculate totals and averages
        total_refs = sum(m['total_references'] for m in all_metrics)
        total_cites = sum(m['total_citations'] for m in all_metrics)
        total_verified = sum(m['verified_references'] for m in all_metrics)
        total_unverifiable = sum(m['unverifiable_references'] for m in all_metrics)
        total_orphan_refs = sum(m['orphan_references'] for m in all_metrics)
        total_orphan_cites = sum(m['orphan_citations'] for m in all_metrics)
        total_fabricated = sum(m['fabricated_references'] for m in all_metrics)

        avg_verification_rate = sum(m['verification_rate'] for m in all_metrics) / len(all_metrics) if all_metrics else 0
        avg_orphan_rate = sum(m['orphan_reference_rate'] for m in all_metrics) / len(all_metrics) if all_metrics else 0

        quality_distribution = {
            'High': sum(1 for m in all_metrics if m['quality_rating'] == 'High'),
            'Moderate': sum(1 for m in all_metrics if m['quality_rating'] == 'Moderate'),
            'Critical': sum(1 for m in all_metrics if m['quality_rating'] == 'Critical')
        }

        return {
            'total_documents': len(all_metrics),
            'total_references': total_refs,
            'total_citations': total_cites,
            'total_verified': total_verified,
            'total_unverifiable': total_unverifiable,
            'total_orphan_references': total_orphan_refs,
            'total_orphan_citations': total_orphan_cites,
            'total_fabricated': total_fabricated,
            'avg_verification_rate': avg_verification_rate,
            'avg_orphan_rate': avg_orphan_rate,
            'quality_distribution': quality_distribution,
            'individual_metrics': all_metrics
        }

    def generate_markdown_report(self, stats: Dict, output_file: str) -> None:
        """
        Generate a markdown summary report.

        Args:
            stats: Aggregate statistics dictionary
            output_file: Path to output markdown file
        """
        report = f"""# Aggregate Citation Audit Statistics

## Summary

**Total Documents Audited**: {stats['total_documents']}
**Total References Processed**: {stats['total_references']:,}
**Total In-Text Citations**: {stats['total_citations']:,}
**Total Verified References**: {stats['total_verified']:,}
**Total Unverifiable References**: {stats['total_unverifiable']}
**Total Fabricated References**: {stats['total_fabricated']}
**Total Orphan References**: {stats['total_orphan_references']} ({stats['avg_orphan_rate']:.1f}% average)
**Total Orphan Citations**: {stats['total_orphan_citations']}

**Average Verification Rate**: {stats['avg_verification_rate']:.1f}%
**Average Orphan Reference Rate**: {stats['avg_orphan_rate']:.1f}%

---

## Quality Distribution

| Quality Rating | Count | Percentage |
|----------------|-------|------------|
| High Quality | {stats['quality_distribution']['High']} | {stats['quality_distribution']['High']/stats['total_documents']*100:.1f}% |
| Moderate | {stats['quality_distribution']['Moderate']} | {stats['quality_distribution']['Moderate']/stats['total_documents']*100:.1f}% |
| Critical Issues | {stats['quality_distribution']['Critical']} | {stats['quality_distribution']['Critical']/stats['total_documents']*100:.1f}% |

---

## Individual Document Metrics

| Document | Total Refs | Verification Rate | Orphan Refs | Orphan Cites | Unverifiable | Quality |
|----------|-----------|------------------|-------------|--------------|--------------|---------|
"""

        for metrics in stats['individual_metrics']:
            report += f"| {metrics['filename']} | {metrics['total_references']} | {metrics['verification_rate']:.1f}% | {metrics['orphan_references']} ({metrics['orphan_reference_rate']:.1f}%) | {metrics['orphan_citations']} | {metrics['unverifiable_references']} | {metrics['quality_rating']} |\n"

        report += f"""
---

## Detection Performance

### Issues Detected Across All Documents

| Issue Type | Total Count | Average per Document |
|------------|------------|---------------------|
| Unverifiable References | {stats['total_unverifiable']} | {stats['total_unverifiable']/stats['total_documents']:.1f} |
| Fabricated References | {stats['total_fabricated']} | {stats['total_fabricated']/stats['total_documents']:.1f} |
| Orphan References | {stats['total_orphan_references']} | {stats['total_orphan_references']/stats['total_documents']:.1f} |
| Orphan Citations | {stats['total_orphan_citations']} | {stats['total_orphan_citations']/stats['total_documents']:.1f} |

---

## Methodology Insights

### Verification Success
- **Best case**: {max(m['verification_rate'] for m in stats['individual_metrics']):.1f}% verification rate
- **Worst case**: {min(m['verification_rate'] for m in stats['individual_metrics']):.1f}% verification rate
- **Range**: {max(m['verification_rate'] for m in stats['individual_metrics']) - min(m['verification_rate'] for m in stats['individual_metrics']):.1f} percentage points

### Reference Counts
- **Smallest bibliography**: {min(m['total_references'] for m in stats['individual_metrics'])} references
- **Largest bibliography**: {max(m['total_references'] for m in stats['individual_metrics'])} references
- **Average bibliography size**: {stats['total_references']/stats['total_documents']:.1f} references

### Quality Assessment
- **Documents ready for submission**: {stats['quality_distribution']['High']} ({stats['quality_distribution']['High']/stats['total_documents']*100:.1f}%)
- **Documents requiring revision**: {stats['quality_distribution']['Moderate'] + stats['quality_distribution']['Critical']} ({(stats['quality_distribution']['Moderate'] + stats['quality_distribution']['Critical'])/stats['total_documents']*100:.1f}%)

---

## Key Findings

1. **Verification Effectiveness**: The methodology successfully verified {stats['avg_verification_rate']:.1f}% of references on average, demonstrating robust detection capabilities.

2. **Issue Detection**: Detected {stats['total_unverifiable']} unverifiable references across {stats['total_documents']} documents, identifying potential quality issues before submission.

3. **Orphan Reference Problem**: {stats['avg_orphan_rate']:.1f}% orphan reference rate suggests common citation management issues across documents.

4. **Quality Stratification**: Clear differentiation between high-quality ({stats['quality_distribution']['High']} docs) and critical-issue documents ({stats['quality_distribution']['Critical']} docs).

---

**Generated**: {import_date()}
**Methodology**: AI-Powered Citation Audit Protocol v1.0
**Analysis Tool**: statistics.py
"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"Summary report written to: {output_file}")

    def generate_json_export(self, stats: Dict, output_file: str) -> None:
        """
        Export statistics as JSON for further analysis.

        Args:
            stats: Aggregate statistics dictionary
            output_file: Path to output JSON file
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2)

        print(f"JSON data exported to: {output_file}")


def import_date():
    """Return current date in ISO format."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Analyze AI-Powered Citation Audit reports and generate aggregate statistics"
    )
    parser.add_argument(
        '--reports-dir',
        type=str,
        default='../audit-reports',
        help='Directory containing audit report markdown files'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='aggregate_statistics.md',
        help='Output file for markdown summary report'
    )
    parser.add_argument(
        '--json',
        type=str,
        help='Optional JSON export file'
    )

    args = parser.parse_args()

    # Initialize analyzer
    analyzer = AuditStatistics(args.reports_dir)

    # Load and analyze reports
    print(f"Loading audit reports from: {args.reports_dir}")
    analyzer.load_reports()

    if not analyzer.reports:
        print("No audit reports found. Ensure directory contains *_ReferenceAudit.md files.")
        return

    print("Calculating aggregate statistics...")
    stats = analyzer.calculate_aggregate_stats()

    # Generate outputs
    print("Generating summary report...")
    analyzer.generate_markdown_report(stats, args.output)

    if args.json:
        print("Exporting JSON data...")
        analyzer.generate_json_export(stats, args.json)

    print("\nAnalysis complete!")
    print(f"  Documents analyzed: {stats['total_documents']}")
    print(f"  Total references: {stats['total_references']:,}")
    print(f"  Average verification rate: {stats['avg_verification_rate']:.1f}%")
    print(f"  Issues detected: {stats['total_unverifiable']} unverifiable, {stats['total_orphan_references']} orphan refs")


if __name__ == '__main__':
    main()
