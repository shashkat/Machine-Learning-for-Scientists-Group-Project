### 04-17-24

### pwd: code/dimensionality_reduction_updated.ipynb

Gonna perform differential gene identification. For this, will use logistic regression with some regularization to perform feature elimination.

Remember that we have done all the analysis so far with just the top 1000 genes.

Have made the logreg model and am also able to assign priority values to the different genes. However, the genes identified aren't necessariily related to cancer/breast cancer. Since they are differentiating between different subtypes of breast cancer, I expected them to have some record of cancer-relation. 

Next steps to get better results would include- first performing normalization for each datapoint before standardization of genes. 

Also, increasing the number of clusters may help.

I think some help was obtained by selecting the high variance genes and increase num clusters (k) to 4.

Next, I need to show graphically how the selected genes are helping in distinguishing the subtypes for the different cancer subtypes.