# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 19:29:04 2021

@author: win 10
"""
#Loading dataset from UCI
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


iris = datasets.load_iris()

print(iris.DESCR)

#Printing features and labels
features = iris.data
labels = iris.target
print(features[0], labels[0])


#Training the classifier

classifier = KNeighborsClassifier()
classifier.fit(features, labels)

prdicts = classifier.predict([[31, 1, 1, 1]])
print(prdicts)
