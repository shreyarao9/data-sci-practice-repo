from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris=datasets.load_iris()
#print(iris.DESCR)
features=iris.data
label=iris.target

print(features[0], label[0])

#training the classifier

clf=KNeighborsClassifier()
clf.fit(features,label)

preds=clf.predict([[60,1,1,1]])
print(preds)