#!/usr/bin/env python3
"""
Download open access papers from validation dataset.

This script downloads full-text PDFs from the DOI/URL links in validation_dataset.json.
Papers are downloaded to a temporary directory (NOT committed to git).

Usage:
    python download_papers.py --dataset ../datasets/validation_dataset.json --output ../temp_papers

Author: LJ Janse van Rensburg
License: MIT
"""

import os
import json
import time
import argparse
import requests
from pathlib import Path
from urllib.parse import urlparse


class PaperDownloader:
    """Downloads open access papers from DOI/URL links."""

    def __init__(self, output_dir: str):
        """
        Initialize the downloader.

        Args:
            output_dir: Directory to save downloaded PDFs
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AI-Citation-Auditor/1.0 (Research; mailto:research@example.com)'
        })

        self.downloaded = []
        self.failed = []

    def sanitize_filename(self, title: str, max_length: int = 100) -> str:
        """
        Create a safe filename from paper title.

        Args:
            title: Paper title
            max_length: Maximum filename length

        Returns:
            Safe filename string
        """
        # Remove special characters
        safe_title = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in title)

        # Collapse multiple spaces/underscores
        safe_title = ' '.join(safe_title.split())
        safe_title = safe_title.replace(' ', '_')

        # Truncate if too long
        if len(safe_title) > max_length:
            safe_title = safe_title[:max_length]

        return safe_title

    def download_plos_paper(self, paper: dict) -> bool:
        """
        Download a PLOS paper as PDF.

        Args:
            paper: Paper metadata dictionary

        Returns:
            True if successful, False otherwise
        """
        title = paper.get('title', 'unknown')
        doi = paper.get('doi', '')

        print(f"\nDownloading: {title[:60]}...")

        # Extract DOI identifier
        doi_id = doi.replace('https://doi.org/', '')

        # PLOS PDF URL format
        pdf_url = f"https://journals.plos.org/plosone/article/file?id={doi_id}&type=printable"

        # Create filename
        safe_title = self.sanitize_filename(title)
        filename = f"{safe_title}.pdf"
        filepath = self.output_dir / filename

        # Skip if already downloaded
        if filepath.exists():
            print(f"  Already exists: {filename}")
            self.downloaded.append({
                'title': title,
                'doi': doi,
                'filepath': str(filepath),
                'status': 'existing'
            })
            return True

        try:
            # Download PDF
            response = self.session.get(pdf_url, timeout=30)
            response.raise_for_status()

            # Check if we got a PDF
            content_type = response.headers.get('Content-Type', '')
            if 'application/pdf' not in content_type:
                print(f"  Warning: Not a PDF (Content-Type: {content_type})")
                # Try alternative URL
                pdf_url_alt = paper.get('url', '') + '/file?type=printable'
                response = self.session.get(pdf_url_alt, timeout=30)
                response.raise_for_status()

            # Save PDF
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"  Downloaded: {filename} ({len(response.content)} bytes)")

            self.downloaded.append({
                'title': title,
                'doi': doi,
                'filepath': str(filepath),
                'status': 'downloaded'
            })

            return True

        except Exception as e:
            print(f"  Failed: {e}")
            self.failed.append({
                'title': title,
                'doi': doi,
                'error': str(e)
            })
            return False

    def download_from_dataset(self, dataset_file: str, limit: int = None) -> dict:
        """
        Download papers from validation dataset.

        Args:
            dataset_file: Path to validation_dataset.json
            limit: Maximum number of papers to download (None = all)

        Returns:
            Dictionary with download statistics
        """
        print(f"Loading dataset from: {dataset_file}")

        with open(dataset_file, 'r', encoding='utf-8') as f:
            dataset = json.load(f)

        papers = dataset.get('papers', [])
        total = len(papers)

        if limit:
            papers = papers[:limit]
            print(f"Limiting to {limit} papers (out of {total})")

        print(f"Downloading {len(papers)} papers...")
        print("=" * 60)

        for i, paper in enumerate(papers, 1):
            print(f"\n[{i}/{len(papers)}]", end=' ')

            source = paper.get('source', 'unknown')

            if source == 'PLOS':
                success = self.download_plos_paper(paper)
            else:
                print(f"Unsupported source: {source}")
                self.failed.append({
                    'title': paper.get('title', 'unknown'),
                    'doi': paper.get('doi', ''),
                    'error': f'Unsupported source: {source}'
                })
                continue

            # Rate limiting - be respectful
            if i < len(papers):
                time.sleep(2)

        print("\n" + "=" * 60)
        print(f"\nDownload complete!")
        print(f"  Successfully downloaded: {len(self.downloaded)}")
        print(f"  Failed: {len(self.failed)}")

        return {
            'total': len(papers),
            'downloaded': len(self.downloaded),
            'failed': len(self.failed),
            'downloaded_list': self.downloaded,
            'failed_list': self.failed
        }

    def save_download_report(self, stats: dict, output_file: str) -> None:
        """
        Save download report as JSON.

        Args:
            stats: Download statistics dictionary
            output_file: Path to output JSON file
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2)

        print(f"\nDownload report saved to: {output_file}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Download open access papers from validation dataset"
    )
    parser.add_argument(
        '--dataset',
        type=str,
        default='../datasets/validation_dataset.json',
        help='Path to validation dataset JSON file'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='../temp_papers',
        help='Output directory for downloaded PDFs'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of papers to download'
    )
    parser.add_argument(
        '--report',
        type=str,
        default='download_report.json',
        help='Output file for download report'
    )

    args = parser.parse_args()

    # Initialize downloader
    downloader = PaperDownloader(args.output)

    # Download papers
    stats = downloader.download_from_dataset(args.dataset, limit=args.limit)

    # Save report
    report_path = Path(args.output) / args.report
    downloader.save_download_report(stats, str(report_path))

    # Print summary
    print("\n" + "=" * 60)
    print("DOWNLOAD SUMMARY")
    print("=" * 60)
    print(f"Total papers in dataset: {stats['total']}")
    print(f"Successfully downloaded: {stats['downloaded']}")
    print(f"Failed downloads: {stats['failed']}")

    if stats['failed'] > 0:
        print("\nFailed papers:")
        for failed in stats['failed_list']:
            print(f"  - {failed['title'][:50]}... (Error: {failed['error']})")

    print(f"\nPDFs saved to: {args.output}")
    print("\nNext step: Extract references and run audits")


if __name__ == '__main__':
    main()
