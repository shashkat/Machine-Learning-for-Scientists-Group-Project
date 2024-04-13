# Machine-Learning-for-Scientists-Group-Project
Record of our group project for the course Machine Learning for Scientists (02-620), Spring 2024.

## get and load GSE75688 RNA-seq dataset

Download data:
```
$ python3 src/download_data.py
```

Preprocess data:
```
$ python3 src/data_preprocessing.py
```
Features `X.npy` and labels `y.npy` will be saved to `data/preprocessed/` dir. 

You can load X and y by:
```
X = np.load('../data/processed/X.npy')
y = np.load('../data/processed/y.npy', allow_pickle=True)
```
