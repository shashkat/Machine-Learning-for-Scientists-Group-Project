### 04-20-24

- merging the work done by rohit and ray into the work done by jon and shashank.
- first adding all the work in an organized way in the src/complete_project.ipynb file (some part from code/dimensionality_reduction_updated.ipynb)
    - when I went on to do eigendecomposition for PCA, RAM got full as X has 50000+ features. Hence, need to perform initial feature selection. For this, needed to calculate the variance of all the genes to begin with. However, the data was standardized. So, I modified the standardization that was happening in the initial step, and once the high variance genes were selected, then the data was standardized.
    - done what is written in the prev point and also plotted the original labels in PCA. Also, done k-means and also plotted PCA'ed data with the found clusters. Found that with seed value 13, the clustering was pretty good (quantified by ARI score, used to compare clusterings). 
    - Now am gonna train the logreg model on the clustered data and try to find genes of significance.