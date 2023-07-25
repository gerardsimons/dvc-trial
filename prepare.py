import pandas as pd

if __name__ == '__main__':
	df = pd.read_csv('raw.csv')
	df = df * 10
	df.to_csv('prepared.csv', index=False)