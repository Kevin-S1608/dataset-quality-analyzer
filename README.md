# Dataset Quality Analyzer

A Python-based data quality analysis tool that evaluates CSV datasets and identifies common data-quality issues.

## Project Overview

The Dataset Quality Analyzer helps users quickly understand the quality of a dataset before using it for further analysis or machine learning.

The system analyzes a CSV file and provides:

- Dataset dimensions
- Missing value detection
- Duplicate row detection
- Potential outlier detection using the IQR method
- Data type profiling
- Dataset quality score
- Quality classification
- Automatic recommendations

## Technologies Used

- Python
- Pandas
- NumPy

## How It Works

The analyzer follows this workflow:

CSV Dataset
↓
Dataset Inspection
↓
Missing Value Detection
↓
Duplicate Detection
↓
Outlier Detection
↓
Data Type Analysis
↓
Quality Score
↓
Recommendations

## Quality Scoring

The project starts with a score of 100.

Penalties are applied based on:

- Missing values
- Duplicate records
- Potential outliers

The final score is classified as:

| Score | Classification |
|---|---|
| 90–100 | Excellent |
| 75–89 | Good |
| 50–74 | Needs Improvement |
| Below 50 | Poor |

## Outlier Detection

Potential outliers are detected using the Interquartile Range (IQR) method.

IQR = Q3 - Q1

Values outside:

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

are flagged as potential outliers.

## Project Structure

```text
dataset-quality-analyzer/
│
├── dataset_quality_analyzer.py
├── sample_dataset.csv
├── test_quality_dataset.csv
├── screenshots/
│   ├── clean_dataset.png
│   └── problematic_dataset.png
└── README.md
