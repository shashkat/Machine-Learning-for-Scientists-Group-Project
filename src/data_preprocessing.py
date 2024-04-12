import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

def load_data(tpm_path, sample_info_path):
    """Load TPM matrix and sample information."""
    tpm_matrix = pd.read_csv(tpm_path, sep='\t', index_col=0)
    sample_info = pd.read_csv(sample_info_path, sep='\t', index_col=0)
    return tpm_matrix, sample_info

def preprocess_tpm_matrix(tpm_matrix):
    """Transpose TPM matrix and drop unnecessary initial rows."""
    tpm_transposed = tpm_matrix.T
    # Remove the first two rows which contain 'gene_name' and 'gene_type'
    tpm_transposed = tpm_transposed[2:] 
    return tpm_transposed

def map_subtypes(tpm_transposed):
    """Map samples to their subtypes."""
    subtype_mapping = {
        'BC01': 'ER+', 'BC02': 'ER+', 'BC03': 'ER+HER2+',
        'BC03LN': 'ER+HER2+ LN metastasis', 'BC04': 'HER2+',
        'BC05': 'HER2+', 'BC06': 'HER2+', 'BC07': 'TNBC',
        'BC07LN': 'TNBC LN metastasis', 'BC08': 'TNBC',
        'BC09': 'TNBC', 'BC10': 'TNBC', 'BC11': 'TNBC',
    }
    sample_subtypes = {sample: subtype_mapping[sample.split('_')[0]] for sample in tpm_transposed.index}
    tpm_transposed['subtype'] = pd.Series(sample_subtypes)
    return tpm_transposed

def prepare_data(tpm_transposed):
    """Prepare data for training."""
    X = tpm_transposed.drop('subtype', axis=1)
    y = tpm_transposed['subtype']
    
    # Scaling features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y

def main():
    # File paths
    tpm_path = '../data/raw/GSE75688_GEO_processed_Breast_Cancer_raw_TPM_matrix.txt'
    sample_info_path = '../data/raw/GSE75688_final_sample_information.txt'
    
    # Load data
    tpm_matrix, sample_info = load_data(tpm_path, sample_info_path)
    tpm_transposed = preprocess_tpm_matrix(tpm_matrix)
    tpm_transposed = map_subtypes(tpm_transposed)
    
    # Prepare data
    X, y = prepare_data(tpm_transposed)

    # Create processed data directory
    processed_data_dir = '../data/processed'
    os.makedirs(processed_data_dir, exist_ok=True)  
    
    # Save processed data
    np.save(os.path.join(processed_data_dir, 'X.npy'), X)
    np.save(os.path.join(processed_data_dir, 'y.npy'), y)

    
if __name__ == '__main__':
    main()
