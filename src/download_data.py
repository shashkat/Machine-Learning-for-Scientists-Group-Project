import requests
import os
import gzip
import shutil

def download_file(url, filename):
    """
    Helper function to download a file from a URL and save it locally.
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.raw.read())
    else:
        print(f"Failed to download file: Status code {response.status_code}\nURL: {url}")

def decompress_gz(source_filepath, dest_filepath):
    """
    Decompresses a gzip file to a destination file path.
    """
    with gzip.open(source_filepath, 'rb') as f_in:
        with open(dest_filepath, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def main():
    data_dir = '../data/raw'  # Adjust the path according to your project structure
    os.makedirs(data_dir, exist_ok=True)

    # File URLs and paths
    files = {
        'TPM_matrix': {
            'url': 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE75nnn/GSE75688/suppl/GSE75688_GEO_processed_Breast_Cancer_raw_TPM_matrix.txt.gz',
            'gz_path': 'GSE75688_GEO_processed_Breast_Cancer_raw_TPM_matrix.txt.gz',
            'final_path': 'GSE75688_GEO_processed_Breast_Cancer_raw_TPM_matrix.txt'
        },
        'sample_info': {
            'url': 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE75nnn/GSE75688/suppl/GSE75688_final_sample_information.txt.gz',
            'gz_path': 'GSE75688_final_sample_information.txt.gz',
            'final_path': 'GSE75688_final_sample_information.txt'
        }
    }

    for key, file_info in files.items():
        gz_file_path = os.path.join(data_dir, file_info['gz_path'])
        decompressed_file_path = os.path.join(data_dir, file_info['final_path'])

        # Download the file
        print(f"Downloading {key}...")
        download_file(file_info['url'], gz_file_path)

        # Decompress the file
        print(f"Decompressing {key}...")
        decompress_gz(gz_file_path, decompressed_file_path)

        print(f"{key} downloaded and decompressed successfully.")

if __name__ == '__main__':
    main()

