
from sklearn.naive_bayes import GaussianNB
# Implementing Naïve Bayes method using scikit-learn library
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.cross_validation import train_test_split


#Using iris dataset available in the package
irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target

#split the data for training and testing cross validation
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)

Output=GaussianNB()
Output.fit(irisdatasets.data, irisdatasets.target).predict(irisdatasets.data)
#quality of cluster
print(Output.score(x,y))
#cross validation
model = GaussianNB()
model.fit(x, y)
print(model.score(x_train, y_train))
