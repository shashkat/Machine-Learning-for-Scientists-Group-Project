### 04-18-24

Earlier polished the code a bit, by making markdown cells in between and dividing into sections, and reorganizing data processing. Next, will have to reorganize the feature selection through logreg part a bit. And also see how to efficiently extend that to the other cancer types.

I was thinking of trying multiple initializations of k-means, but it turns out that with np.random.seed(0), it gives decent good results for all the samples. 

Am gonna try k = 3 also once, as in most samples, can see 3 distinct clusters and the 4th one is usually overkill.

k = 3 looks good initially. Lets see how good are the genes I identify using it. But first, I will clean that part of the code a bit..

was trying to replicate getting the CXorf61 gene as one of the informative genes. Turns out getting it as the informative genes is highly dependent on the clustering we obtain. Hence, it is important to get a good clustering. 
Can spend time in doing multiple initializations of k-means and choosing the best clustering acc to some criterion.