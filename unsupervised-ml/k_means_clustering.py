import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#generating synthetic dataset
X, _ =make_blobs(n_samples=300,centers=4,cluster_std=0.60,random_state=0)

#creating KMeans object
kmeans=KMeans(n_clusters=4)

#fitting the KMeans model to the data
kmeans.fit(X)

#getting cluster centers and labels
cluster_centers=kmeans.cluster_centers_
cluster_labels=kmeans.labels_

#visualisation
plt.scatter(X[:,0],X[:,1],c=cluster_labels,cmap='gist_rainbow')
plt.scatter(cluster_centers[:,0],cluster_centers[:,1],marker='x',s=100)
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()