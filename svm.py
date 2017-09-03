from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib

clf = svm.SVC(gamma=0.001, C=100)
X = []
Y = []

clf.fit(X, Y)

clf.predict(X[0:10])

joblib.dump(clf, 'filename.pkl')
clf = joblib.load('filename.pkl')