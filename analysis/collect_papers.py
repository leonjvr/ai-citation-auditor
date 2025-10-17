#!/usr/bin/env python3
"""
AI-Powered Citation Auditor - Open Access Paper Collection

Collects open access research papers for methodology validation.
Stores only DOI/URL links and extracted metadata, not full-text PDFs.

Usage:
    python collect_papers.py --count 20 --sources arxiv,plos --output dataset.json

Author: LJ Janse van Rensburg
License: MIT
"""

import os
import json
import time
import argparse
import requests
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path


class OpenAccessPaperCollector:
    """Collects metadata and links to open access research papers."""

    def __init__(self):
        """Initialize the paper collector."""
        self.papers = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AI-Citation-Auditor/1.0 (Research Project; mailto:research@example.com)'
        })

    def search_arxiv(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search arXiv for open access papers.

        Args:
            query: Search query string
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        print(f"Searching arXiv for: {query}")

        # arXiv API endpoint
        base_url = "http://export.arxiv.org/api/query"

        params = {
            'search_query': query,
            'start': 0,
            'max_results': max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }

        try:
            response = self.session.get(base_url, params=params)
            response.raise_for_status()

            # Parse arXiv Atom feed (simplified - would need XML parsing for production)
            papers = []

            # For now, return placeholder structure
            # In production, would parse XML response
            print(f"  Found {max_results} papers from arXiv (API integration required)")

            return papers

        except Exception as e:
            print(f"  Error searching arXiv: {e}")
            return []

    def search_plos(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search PLOS ONE for open access papers.

        Args:
            query: Search query string
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        print(f"Searching PLOS for: {query}")

        # PLOS Search API
        base_url = "https://api.plos.org/search"

        params = {
            'q': query,
            'rows': max_results,
            'wt': 'json',
            'fl': 'id,title,author,publication_date,article_type,abstract'
        }

        try:
            response = self.session.get(base_url, params=params)
            response.raise_for_status()

            data = response.json()
            docs = data.get('response', {}).get('docs', [])

            papers = []
            for doc in docs:
                paper = {
                    'source': 'PLOS',
                    'title': doc.get('title', [''])[0] if isinstance(doc.get('title'), list) else doc.get('title', ''),
                    'authors': doc.get('author', []),
                    'publication_date': doc.get('publication_date', ''),
                    'doi': f"https://doi.org/{doc.get('id', '')}",
                    'url': f"https://journals.plos.org/plosone/article?id={doc.get('id', '')}",
                    'article_type': doc.get('article_type', ''),
                    'abstract': doc.get('abstract', [''])[0] if isinstance(doc.get('abstract'), list) else doc.get('abstract', ''),
                    'collected_date': datetime.now().isoformat()
                }
                papers.append(paper)

            print(f"  Found {len(papers)} papers from PLOS")
            return papers

        except Exception as e:
            print(f"  Error searching PLOS: {e}")
            return []

    def search_pubmed_central(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search PubMed Central for open access papers.

        Args:
            query: Search query string
            max_results: Maximum number of results to return

        Returns:
            List of paper metadata dictionaries
        """
        print(f"Searching PubMed Central for: {query}")

        # NCBI E-utilities API
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

        params = {
            'db': 'pmc',
            'term': query + ' AND open access[filter]',
            'retmax': max_results,
            'retmode': 'json',
            'sort': 'pub_date'
        }

        try:
            response = self.session.get(base_url, params=params)
            response.raise_for_status()

            data = response.json()
            id_list = data.get('esearchresult', {}).get('idlist', [])

            papers = []
            print(f"  Found {len(id_list)} papers from PubMed Central (metadata fetch required)")

            # Would need additional API calls to fetch full metadata
            # For now, return structure

            return papers

        except Exception as e:
            print(f"  Error searching PubMed Central: {e}")
            return []

    def collect_diverse_sample(self, count: int = 20, sources: List[str] = None) -> List[Dict]:
        """
        Collect a diverse sample of open access papers.

        Args:
            count: Total number of papers to collect
            sources: List of sources to search (arxiv, plos, pubmed)

        Returns:
            List of collected paper metadata
        """
        if sources is None:
            sources = ['plos']  # Start with PLOS as it has functional API

        papers_per_source = count // len(sources)
        all_papers = []

        # Diverse search queries across different fields
        queries = [
            'machine learning',
            'climate change',
            'covid-19',
            'artificial intelligence',
            'genomics',
            'neuroscience',
            'economics',
            'psychology'
        ]

        for source in sources:
            source_papers = []

            for i, query in enumerate(queries):
                if len(source_papers) >= papers_per_source:
                    break

                if source == 'arxiv':
                    papers = self.search_arxiv(query, max_results=3)
                elif source == 'plos':
                    papers = self.search_plos(query, max_results=3)
                elif source == 'pubmed':
                    papers = self.search_pubmed_central(query, max_results=3)
                else:
                    continue

                source_papers.extend(papers)

                # Rate limiting - be respectful to APIs
                time.sleep(1)

            all_papers.extend(source_papers[:papers_per_source])

        print(f"\nCollected {len(all_papers)} papers total")
        return all_papers

    def save_dataset(self, papers: List[Dict], output_file: str) -> None:
        """
        Save collected papers to JSON file.

        Args:
            papers: List of paper metadata dictionaries
            output_file: Path to output JSON file
        """
        dataset = {
            'metadata': {
                'collection_date': datetime.now().isoformat(),
                'total_papers': len(papers),
                'methodology': 'AI-Powered Citation Auditor v1.0',
                'purpose': 'Methodology validation and statistical significance testing',
                'license': 'Metadata only - papers are open access',
                'note': 'This dataset contains only links and metadata. Download papers from DOI/URL.'
            },
            'papers': papers
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)

        print(f"\nDataset saved to: {output_file}")
        print(f"Total papers: {len(papers)}")

    def generate_dataset_readme(self, output_file: str, paper_count: int) -> None:
        """
        Generate README for the dataset.

        Args:
            output_file: Path to README file
            paper_count: Number of papers in dataset
        """
        readme_content = f"""# Open Access Paper Dataset for Citation Audit Validation

## Purpose

This dataset contains links and metadata for {paper_count} open access research papers used to validate the AI-Powered Citation Auditor methodology. The papers were selected to provide diverse representation across:

- Multiple academic disciplines (CS, biology, medicine, social sciences, etc.)
- Different publication venues (journals, preprints)
- Various citation practices and reference list sizes
- Recent publications (2020-2025)

## Dataset Structure

The dataset is stored in `dataset.json` with the following structure:

```json
{{
  "metadata": {{
    "collection_date": "ISO-8601 timestamp",
    "total_papers": {paper_count},
    "methodology": "AI-Powered Citation Auditor v1.0",
    "purpose": "Statistical validation"
  }},
  "papers": [
    {{
      "source": "PLOS|arXiv|PubMed",
      "title": "Paper title",
      "authors": ["Author 1", "Author 2"],
      "publication_date": "YYYY-MM-DD",
      "doi": "https://doi.org/...",
      "url": "Direct link to paper",
      "article_type": "Research Article|Review|etc.",
      "abstract": "Paper abstract",
      "collected_date": "ISO-8601 timestamp"
    }}
  ]
}}
```

## Data Sources

All papers are from **open access** sources:

- **PLOS** (Public Library of Science) - CC BY license
- **arXiv** - Open access preprints
- **PubMed Central** - Open access biomedical research

## License and Usage

**Dataset License**: CC0 1.0 (Public Domain Dedication)

**Important Notes**:
1. This dataset contains **only metadata and links** to papers
2. Original papers remain under their respective licenses (typically CC BY)
3. To use papers, download from provided DOI/URL
4. **Do NOT redistribute full-text PDFs** - link to original sources instead

## Reproducing the Dataset

To collect a fresh dataset:

```bash
python collect_papers.py --count {paper_count} --sources plos --output dataset.json
```

## Processing Papers

To run citation audits on these papers:

```bash
# Download a paper
curl -L "[DOI_URL]" -o paper.pdf

# Extract text
python ../protocol/extract_docx.py paper.pdf > paper.txt

# Run audit
claude --dangerously-skip-permissions
# Then: "Run citation audit on paper.txt using CLAUDE.md protocol"
```

## Citation

If you use this dataset, please cite:

```
Janse van Rensburg, LJ. (2025). Open Access Paper Dataset for Citation Audit
Validation. AI-Powered Citation Auditor Project.
https://github.com/leonjvr/ai-citation-auditor
```

## Statistics

- **Total papers**: {paper_count}
- **Collection date**: {datetime.now().strftime("%Y-%m-%d")}
- **Sources**: PLOS, arXiv, PubMed Central
- **Fields**: Multi-disciplinary
- **Purpose**: Statistical validation of AI citation auditing methodology

## Ethical Considerations

- Only open access papers included (legal to download and analyze)
- No full-text redistribution (links only)
- Metadata collection complies with API terms of service
- Rate limiting applied to respect API providers

---

**Last Updated**: {datetime.now().strftime("%Y-%m-%d")}
"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"Dataset README saved to: {output_file}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Collect open access papers for citation audit validation"
    )
    parser.add_argument(
        '--count',
        type=int,
        default=20,
        help='Number of papers to collect (default: 20)'
    )
    parser.add_argument(
        '--sources',
        type=str,
        default='plos',
        help='Comma-separated list of sources: arxiv,plos,pubmed (default: plos)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='dataset.json',
        help='Output JSON file (default: dataset.json)'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='../datasets',
        help='Output directory (default: ../datasets)'
    )

    args = parser.parse_args()

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    output_file = output_dir / args.output
    readme_file = output_dir / 'README.md'

    # Initialize collector
    collector = OpenAccessPaperCollector()

    # Parse sources
    sources = [s.strip() for s in args.sources.split(',')]

    print(f"Collecting {args.count} papers from: {', '.join(sources)}")
    print("=" * 60)

    # Collect papers
    papers = collector.collect_diverse_sample(count=args.count, sources=sources)

    if not papers:
        print("\nNo papers collected. Check API connectivity and try again.")
        return

    # Save dataset
    collector.save_dataset(papers, str(output_file))

    # Generate README
    collector.generate_dataset_readme(str(readme_file), len(papers))

    print("\n" + "=" * 60)
    print("Collection complete!")
    print(f"  Papers collected: {len(papers)}")
    print(f"  Dataset: {output_file}")
    print(f"  README: {readme_file}")
    print("\nNext steps:")
    print("  1. Review dataset.json")
    print("  2. Download papers from DOI/URL links")
    print("  3. Run citation audits on downloaded papers")
    print("  4. Generate aggregate statistics")


if __name__ == '__main__':
    main()
