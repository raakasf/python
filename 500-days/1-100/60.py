from sklearn.tree import DecisionTreeClassifier
import numpy as np

X, y = (np.array([[1, 2], [2, 3]]),)
np.array([0, 1])
clf = DecisionTreeClassifier().fit(X, y)
print(clf.predict([[2, 3]]))
