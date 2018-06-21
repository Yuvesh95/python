import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
# here we take the value from the csv file
variables = pandas.read_csv('sample_stocks.csv')
#as the csv has 2 variables which are taken into x and y variables
Y = variables[['returns']]
X = variables[['dividendyield']]

Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]

score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
#part 1 of question where we calculate the number of clusters
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()


#to make the resultant clusters into a set and ploting into clusters
pca = PCA(n_components=1).fit(Y)
pca_d = pca.transform(Y)
pca_c = pca.transform(X)
kmeans=KMeans(n_clusters=3)
kmeansoutput=kmeans.fit(Y)

#the 2d graph is converted into 3d
pl.figure('3 Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('3 Cluster K-Means')
pl.show()
