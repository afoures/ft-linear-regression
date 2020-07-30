import os

usage = 'usage:	$> python {} dataset.csv'.format(__file__)

def	getPath(file):
	return os.path.join(os.path.dirname(__file__), file)