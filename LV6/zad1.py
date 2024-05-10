from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
from sklearn import metrics
from scipy.spatial.distance import cdist

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X


data=generate_data(500,3)

kmeans = kmeans = KMeans(n_clusters=4,random_state=0, n_init="auto").fit(data)

y_kmeans= kmeans.predict(data)

center=kmeans.cluster_centers_
plt.scatter(data[:,0], data[:,1],c=y_kmeans,s=50, cmap='viridis')
plt.scatter(center[:,0],center[:,1],c='black',s=200,alpha=0.5)
plt.show()


