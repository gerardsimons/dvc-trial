#!/

import pandas as pd

if __name__ == '__main__':
	df = pd.read_csv('data/raw.csv')
	df = df * 10
	df.to_csv('data/prepared.csv', index=False)