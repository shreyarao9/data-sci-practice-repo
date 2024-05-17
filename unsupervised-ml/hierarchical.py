import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs

#generate sample data
X, _ =make_blobs(n_samples=300,centers=4,cluster_std=0.60,random_state=0)

#hierarchical clustering
#you can adjust params like linkage type and number of clusters
#linkage types: 'ward', 'complete', 'average', 'single'
#number of clusters: can be specified or determined automatically
cluster=AgglomerativeClustering(n_clusters=4,linkage='ward')
cluster.fit_predict(X)

#plotting the clusters
plt.scatter(X[:,0],X[:,1],c=cluster.labels_,cmap='gist_rainbow')
plt.show()