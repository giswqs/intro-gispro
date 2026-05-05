---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/software/git.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/software/git.ipynb)

# Version Control with Git

## Introduction

### What is Git?

### What is GitHub?

## Learning Objectives

## Setting Up GitHub Account

### Creating Your GitHub Account

## Installing Git

### Installation Instructions

### Verifying Installation

```bash
# Check Git version
git --version

# Check installation location
which git  # macOS/Linux
where git  # Windows
```

## Configuring Git

### Essential Configuration

```bash
# Replace with your actual name and GitHub email
git config --global user.name "Your Full Name"
git config --global user.email "your.github@email.com"
```

### Verification

```bash
# View all global configuration
git config --global --list

# Check specific values
git config --global user.name
git config --global user.email
```

## Understanding Git Concepts

### Core Git Concepts

### The Git Workflow

## Essential Git Commands

### Starting a New Project

```bash
# Navigate to your project folder
cd ~/my-geo-project

# Initialize Git repository
git init

# Check repository status
git status
```

```bash
# Clone a repository from GitHub
git clone https://github.com/<your-username>/intro-gispro.git
```

### Tracking Changes

```bash
# Add specific files
git add analysis.py
```

```bash
# Add all files in current directory
git add .
```

```bash
# See status of all files
git status

# See detailed changes
git diff
```

```bash
# Commit with inline message
git commit -m "Add rainfall analysis function"

# Commit all tracked files (skip staging)
git commit -am "Update visualization parameters"
```

### Writing Good Commit Messages

```bash
git commit -m "Add NDVI calculation for Landsat 8 imagery"
git commit -m "Fix coordinate transformation bug in UTM conversion"
git commit -m "Update flood mapping algorithm to handle edge cases"
```

### Working with GitHub

```bash
# Add remote repository
git remote add origin https://github.com/<your-username>/<repo-name>.git
```

```bash
# Push to GitHub (first time)
git push -u origin main

# Push subsequent changes
git push
```

```bash
# Pull changes from GitHub
git pull
```

### Basic Branching

```bash
# Create new branch for experimental feature
git checkout -b satellite-analysis

# List all branches
git branch

# Switch back to main branch
git checkout main

# Merge feature branch into main
git merge satellite-analysis

# Delete merged branch
git branch -d satellite-analysis
```

### Viewing Project History

```bash
# View commit history
git log

# Compact one-line format
git log --oneline

# View specific file history
git log -- data_processing.py
```

### Undoing Changes

```bash
# Undo last commit but keep changes
git reset --soft HEAD~1
```

## Using GitHub

### Creating Repositories on GitHub

### Basic Collaboration

### Repository Management

## Integration with VS Code

## Best Practices for Geospatial Projects

### Repository Structure

### What to Track vs. Ignore

### Commit Message Conventions

```bash
# Format: <type>: <description>
git commit -m "feat: add NDVI calculation for Sentinel-2"
git commit -m "fix: handle NoData values in elevation processing"
git commit -m "docs: update README with installation instructions"
```

## Key Takeaways

## Exercises

### Exercise 1: Setting Up Git and GitHub

### Exercise 2: Your First Repository

### Exercise 3: Collaboration and Pull Requests
