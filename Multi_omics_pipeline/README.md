# Multi-Omics Analysis Pipeline

This pipeline showcases the integration and analysis of transcriptomics and metabolomics data using Python. It generates synthetic data for our transcriptomics and metabolomics and runs it in our analysis pipeline to produces a graph that cleans and combines the data whilst combining the samples to plot a graph to visualise what we are seeing.

## Features

- Data loading and preprocessing for transcriptomics and metabolomics data
- Data integration across omics layers
- Visualization of results using matplotlib 

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main pipeline:
```bash
python multi_omics_pipeline.py
```

## Project Structure

- `multi_omics_pipeline.py`: Main pipeline script
- `data/`: Directory containing sample data
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation

## Data Format

The pipeline expects the following data formats:
- Transcriptomics data: CSV file with genes as rows and samples as columns
- Metabolomics data: CSV file with metabolites as rows and samples as columns

Both datasets should have matching sample IDs for integration. 