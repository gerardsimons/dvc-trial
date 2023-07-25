import pandas as pd

from sklearn.tree import DecisionTreeClassifier
import pickle

if __name__ == '__main__':
	df = pd.read_csv('data/prepared.csv')

	clf = DecisionTreeClassifier()

	# Do some kind of training here ...
	with open('models/tree.pkl', 'wb') as fp:
		fp.write(pickle.dumps(clf))