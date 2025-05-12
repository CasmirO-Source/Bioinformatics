import numpy as np
import pandas as pd
import os

def make_gene_data(samples=10, genes=100):
    np.random.seed(123)
    data = np.random.uniform(5, 15, (genes, samples))
    gene_names = [f'Gene_{i+1}' for i in range(genes)]
    sample_names = [f'Sample_{i+1}' for i in range(samples)]
    df = pd.DataFrame(data, index=gene_names, columns=sample_names)
    for row in range(genes):
        for col in range(samples):
            if np.random.random() < 0.05:
                df.iloc[row, col] = np.nan
    return df

def make_metabolite_data(samples=10, metabolites=20):
    np.random.seed(456)
    data = np.random.uniform(2, 8, (metabolites, samples))
    metabolite_names = [f'Metabolite_{i+1}' for i in range(metabolites)]
    sample_names = [f'Sample_{i+1}' for i in range(samples)]
    df = pd.DataFrame(data, index=metabolite_names, columns=sample_names)
    for row in range(metabolites):
        for col in range(samples):
            if np.random.random() < 0.05:
                df.iloc[row, col] = np.nan
    return df

def main():
    print("Making fake biological data...")
    gene_df = make_gene_data()
    metabolite_df = make_metabolite_data()
    os.makedirs('data', exist_ok=True)
    gene_df.to_csv('data/transcriptomics_data.csv')
    metabolite_df.to_csv('data/metabolomics_data.csv')
    print("Done! Created:")
    print(f" - Gene data: {gene_df.shape[0]} genes x {gene_df.shape[1]} samples")
    print(f" - Molecule data: {metabolite_df.shape[0]} metabolites x {metabolite_df.shape[1]} samples")
    print("Check the 'data' folder for the CSV files!")

if __name__ == "__main__":
    main()

