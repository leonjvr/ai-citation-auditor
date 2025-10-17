# Open Access Paper Dataset for Citation Audit Validation

## Purpose

This dataset contains links and metadata for 24 open access research papers used to validate the AI-Powered Citation Auditor methodology. The papers were selected to provide diverse representation across:

- Multiple academic disciplines (CS, biology, medicine, social sciences, etc.)
- Different publication venues (journals, preprints)
- Various citation practices and reference list sizes
- Recent publications (2020-2025)

## Dataset Structure

The dataset is stored in `dataset.json` with the following structure:

```json
{
  "metadata": {
    "collection_date": "ISO-8601 timestamp",
    "total_papers": 24,
    "methodology": "AI-Powered Citation Auditor v1.0",
    "purpose": "Statistical validation"
  },
  "papers": [
    {
      "source": "PLOS|arXiv|PubMed",
      "title": "Paper title",
      "authors": ["Author 1", "Author 2"],
      "publication_date": "YYYY-MM-DD",
      "doi": "https://doi.org/...",
      "url": "Direct link to paper",
      "article_type": "Research Article|Review|etc.",
      "abstract": "Paper abstract",
      "collected_date": "ISO-8601 timestamp"
    }
  ]
}
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
python collect_papers.py --count 24 --sources plos --output dataset.json
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

- **Total papers**: 24
- **Collection date**: 2025-10-17
- **Sources**: PLOS, arXiv, PubMed Central
- **Fields**: Multi-disciplinary
- **Purpose**: Statistical validation of AI citation auditing methodology

## Ethical Considerations

- Only open access papers included (legal to download and analyze)
- No full-text redistribution (links only)
- Metadata collection complies with API terms of service
- Rate limiting applied to respect API providers

---

**Last Updated**: 2025-10-17
