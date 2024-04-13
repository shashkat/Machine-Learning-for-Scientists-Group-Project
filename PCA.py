import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

import pandas as pd
import numpy as np
# Load the data
file_path = 'code/data/bladder/GSE75688_GEO_processed_Breast_Cancer_raw_TPM_matrix.txt'
df = pd.read_csv(file_path, sep='\t')

# Extract the numerical data
data = df.iloc[:, 3:]

# Transpose the data to have samples in rows
transposed_data = data.T
transposed_data.columns = df['gene_name']

# Create a mapping of sample names to molecular subtypes
subtype_mapping = {
    'BC01': 'ER+', 'BC02': 'ER+',
    'BC03': 'ER+ and HER2+', 'BC03LN': 'Lymph node metastasis of BC03',
    'BC04': 'HER2+', 'BC05': 'HER2+', 'BC06': 'HER2+',
    'BC07': 'TNBC', 'BC08': 'TNBC', 'BC09': 'TNBC', 'BC10': 'TNBC', 'BC11': 'TNBC',
    'BC07LN': 'Lymph node metastasis of BC07'
}

# Extract the sample names from the data
sample_names = transposed_data.index

# Add a new column for molecular subtypes
transposed_data['Molecular Subtype'] = [subtype_mapping.get(name.split('_')[0], 'Unknown') for name in sample_names]

# Perform PCA on the transposed data (without scaling)
pca_transposed = PCA(n_components=3)
principal_components_transposed = pca_transposed.fit_transform(transposed_data.iloc[:, :-1])  # Exclude the 'Molecular Subtype' column

# Create a DataFrame with the principal components of the transposed data
pca_transposed_df = pd.DataFrame(data=principal_components_transposed, columns=['PC1', 'PC2', 'PC3'])

# Add the 'Molecular Subtype' column to the PCA DataFrame
print(transposed_data['Molecular Subtype'])
print(pca_transposed_df.shape, transposed_data.shape)
transposed_data_copy = transposed_data.reset_index(drop=True)
pca_transposed_df['Molecular Subtype'] = transposed_data_copy['Molecular Subtype']


# Plot the first two principal components with colors based on 'Molecular Subtype'
plt.figure(figsize=(10, 8))
subtypes = pca_transposed_df['Molecular Subtype'].unique()
print(subtypes)
for subtype in subtypes:
    subset = pca_transposed_df[pca_transposed_df['Molecular Subtype'] == subtype]
    plt.scatter(subset['PC1'], subset['PC2'], label=subtype, alpha=0.7)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Breast Cancer Data by Molecular Subtype')
plt.legend(title='Molecular Subtype')
plt.grid(True)
plt.show()

# Plot the first and third principal components with colors based on 'Molecular Subtype'
plt.figure(figsize=(10, 8))
subtypes = pca_transposed_df['Molecular Subtype'].unique()
print(subtypes)
for subtype in subtypes:
    subset = pca_transposed_df[pca_transposed_df['Molecular Subtype'] == subtype]
    plt.scatter(subset['PC1'], subset['PC3'], label=subtype, alpha=0.7)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 3')
plt.title('PCA of Breast Cancer Data by Molecular Subtype')
plt.legend(title='Molecular Subtype')
plt.grid(True)
plt.show()

# Print the explained variance ratio
print(pca_transposed.explained_variance_ratio_)