# GitHub Repository Setup Guide

## Quick Setup Instructions for Publishing to GitHub

This guide will help you publish the `ai-citation-auditor` repository to GitHub.

---

## Prerequisites

- GitHub account (username: `leonjvr`)
- Git installed locally
- Command line access

---

## Step 1: Initialize Local Git Repository

```bash
cd "C:\Users\leon\Dropbox\UJ\Research\Conferences\Agents4Science 2025\Data\ai-citation-auditor"

# Initialize git repository
git init

# Add all files
git add .

# Check what will be committed (should NOT include .docx files)
git status

# Verify .gitignore is working
git status --ignored
```

**Expected**: You should see `.docx` files and extracted text files listed under "Ignored files".

---

## Step 2: Create Initial Commit

```bash
# Commit all files
git commit -m "Initial commit: AI-Powered Citation Auditor v1.0.0

- Zero-assumption protocol for reference verification
- Comprehensive methodology documentation
- Example audit reports (anonymized)
- Replication instructions
- Claude CLI v2.0.21 implementation
- Tested on 6 documents (1,369 references)
- Developed for Agents4Science 2025 conference"
```

---

## Step 3: Create GitHub Repository

### Option A: Via GitHub Web Interface

1. Go to: https://github.com/new
2. **Repository name**: `ai-citation-auditor`
3. **Description**:
   ```
   AI-powered methodology for comprehensive reference and citation audits
   in academic manuscripts. Zero-assumption protocol using Agentic AI.
   Agents4Science 2025.
   ```
4. **Visibility**: Public
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Option B: Via GitHub CLI (if installed)

```bash
gh repo create ai-citation-auditor --public \
  --description "AI-powered methodology for comprehensive reference and citation audits" \
  --source=. --remote=origin
```

---

## Step 4: Connect Local Repository to GitHub

```bash
# Add GitHub as remote (replace with your actual repo URL)
git remote add origin https://github.com/leonjvr/ai-citation-auditor.git

# Verify remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 5: Verify Upload

1. Visit: https://github.com/leonjvr/ai-citation-auditor
2. Check that all files are present:
   - ✓ README.md
   - ✓ METHODOLOGY.md
   - ✓ CITATION.md
   - ✓ LICENSE
   - ✓ CITATION.cff
   - ✓ .gitignore
   - ✓ protocol/
   - ✓ audit-reports/
3. **Verify NO .docx files were uploaded**
4. Check that README displays correctly

---

## Step 6: Configure Repository Settings

### Add Topics/Tags

Go to: https://github.com/leonjvr/ai-citation-auditor/settings

Add topics:
- `citation-auditing`
- `reference-verification`
- `academic-integrity`
- `agentic-ai`
- `llm-agents`
- `claude-cli`
- `research-tools`
- `agents4science`
- `bibliography-management`
- `scholarly-communication`

### Update Repository Description

```
🤖 AI-powered citation auditor using agentic AI to verify references, detect
fabricated sources, and assess journal quality. Zero-assumption protocol for
academic manuscripts. Agents4Science 2025.
```

### Add Website Link

In "About" section, add:
- **Website**: https://agents4science.stanford.edu

---

## Step 7: Create Release (v1.0.0)

```bash
# Tag the release
git tag -a v1.0.0 -m "Release v1.0.0: Initial public release for Agents4Science 2025

Features:
- Zero-assumption citation verification protocol
- Comprehensive audit report generation
- Support for 19-916 reference documents
- 76.8% average verification rate
- 95%+ time efficiency vs manual review
- Example audits from 6 academic documents
- Full replication methodology

Technical:
- Claude CLI v2.0.21
- Claude Sonnet 4.5
- Python 3.8+ with python-docx
- Cross-platform support
"

# Push tag
git push origin v1.0.0
```

Then on GitHub:
1. Go to: https://github.com/leonjvr/ai-citation-auditor/releases/new
2. Select tag: `v1.0.0`
3. Release title: `v1.0.0 - Initial Public Release`
4. Copy tag message as description
5. Check "Set as the latest release"
6. Click "Publish release"

---

## Step 8: Archive on Zenodo (Optional but Recommended)

For persistent DOI and long-term archiving:

1. Go to: https://zenodo.org/
2. Log in (use ORCID or GitHub)
3. Go to: https://zenodo.org/account/settings/github/
4. Enable repository: `leonjvr/ai-citation-auditor`
5. Create a new release on GitHub (v1.0.0)
6. Zenodo automatically archives and assigns DOI
7. Update CITATION.md and README.md with DOI

---

## Step 9: Update Citation Files with DOI

Once you have the Zenodo DOI:

```bash
# Edit CITATION.md
# Replace: doi = {[Add DOI if archived on Zenodo]}
# With: doi = {10.5281/zenodo.XXXXXX}

# Edit README.md
# Add DOI badge at top:
# [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXX)

# Commit and push
git add CITATION.md README.md
git commit -m "Add Zenodo DOI for v1.0.0"
git push
```

---

## Step 10: Share Repository

### Academic Networks

**Twitter/X**:
```
🎉 Introducing the AI-Powered Citation Auditor - an open-source tool for
systematic reference verification using Agentic AI!

✅ Zero-assumption protocol
✅ 95%+ time savings vs manual review
✅ Detects fabricated sources
✅ Tested on 1,369 references

Developed for #Agents4Science2025

📖 https://github.com/leonjvr/ai-citation-auditor

#AcademicIntegrity #AIResearch #OpenScience
```

**LinkedIn**:
```
I'm excited to share the AI-Powered Citation Auditor, an open-source
methodology for comprehensive reference verification in academic work.

This tool uses Agentic AI (Claude CLI) to systematically verify references
against Semantic Scholar and Google Scholar, detect fabricated sources, and
assess journal quality - all in a fraction of the time of manual review.

Key Features:
• Zero-assumption verification protocol
• Comprehensive audit reports
• 76.8% average verification rate across diverse documents
• Scales from 19 to 916 references
• Full methodology for replication

Developed for the Agents4Science 2025 conference, this research demonstrates
how AI agents can assist academic supervision while maintaining critical
oversight and transparency.

Repository: https://github.com/leonjvr/ai-citation-auditor

#OpenScience #AcademicIntegrity #AIResearch #HigherEducation
```

**ResearchGate**:
- Add as "Code" contribution
- Link to GitHub repository
- Tag relevant topics

---

## Maintenance Commands

### Update repository

```bash
# Make changes to files
git add .
git commit -m "Description of changes"
git push
```

### Create new release

```bash
git tag -a v1.1.0 -m "Release notes here"
git push origin v1.1.0
```

### Check repository status

```bash
git status
git log --oneline
```

---

## Security Checklist

Before publishing, verify:

- [ ] NO student documents (.docx files) included
- [ ] NO personal identifying information in audit reports
- [ ] NO email addresses or contact details
- [ ] NO institutional confidential information
- [ ] .gitignore properly excludes sensitive files
- [ ] All example audit reports are anonymized
- [ ] No API keys or credentials in code
- [ ] License file is present and correct

Run final check:
```bash
# Check for any .docx files
find . -name "*.docx" -type f

# Should return nothing (all excluded by .gitignore)
```

---

## Troubleshooting

### Problem: .docx files showing in git status

**Solution**:
```bash
# Verify .gitignore is in place
cat .gitignore | grep docx

# Force git to respect .gitignore
git rm --cached *.docx
git add .gitignore
git commit -m "Fix: Ensure .docx files are ignored"
```

### Problem: Repository too large

**Solution**:
```bash
# Check repository size
du -sh .git

# If >100MB, verify no large files committed
git ls-files --exclude-standard | xargs du -sh | sort -h
```

### Problem: Push rejected

**Solution**:
```bash
# Pull latest changes first
git pull origin main --rebase

# Then push
git push origin main
```

---

## Post-Publication Checklist

After repository is live:

- [ ] Verify README displays correctly on GitHub
- [ ] Check all links work (CLAUDE.md, METHODOLOGY.md, etc.)
- [ ] Confirm audit reports are readable
- [ ] Test clone command works
- [ ] Add repository topics/tags
- [ ] Create v1.0.0 release
- [ ] Archive on Zenodo (optional)
- [ ] Update conference submission with GitHub link
- [ ] Share on academic social media
- [ ] Add to ORCID profile
- [ ] Add to ResearchGate
- [ ] Monitor GitHub issues/discussions

---

## Conference Paper Integration

Include in Agents4Science 2025 submission:

**In Abstract**:
> "Complete methodology and replication materials are available at:
> https://github.com/leonjvr/ai-citation-auditor"

**In Methods Section**:
> "The complete citation audit protocol is publicly available under an open-source
> MIT license (Janse van Rensburg, 2025), enabling full replication by other
> researchers. See: https://github.com/leonjvr/ai-citation-auditor"

**In Data Availability Statement**:
> "Code and methodology: https://github.com/leonjvr/ai-citation-auditor
> Example audit reports (anonymized): Available in repository under audit-reports/
> Original student documents: Not available due to privacy considerations"

**In Acknowledgments**:
> "The AI-Powered Citation Auditor is powered by Anthropic Claude (Sonnet 4.5)
> via Claude CLI v2.0.21."

---

## Support and Community

After publication, monitor:
- GitHub Issues: Questions and bug reports
- GitHub Discussions: Community conversations
- Stars/Forks: Gauge interest and adoption
- Citations: Track academic citations via Google Scholar

Be responsive to:
- Replication questions
- Methodology clarifications
- Bug reports
- Feature requests

---

**Setup Complete!**

Your repository is now ready for publication at:
**https://github.com/leonjvr/ai-citation-auditor**

For questions about this setup, see GitHub documentation:
https://docs.github.com/en/repositories/creating-and-managing-repositories
