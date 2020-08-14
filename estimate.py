import math
import csv
import sys
import os
from train import getPath, normalizeElem, denormalizeElem, getData

def	estimatePrice(thetas, mileage, mileages, prices):
	price = thetas[1] * normalizeElem(mileages, mileage) + thetas[0]
	return (denormalizeElem(prices, price))
	
def	getMileage():
	while 1:
		print('Please enter a mileage: ')
		try:
			mileage = input()
		except EOFError:
			sys.exit('EOF on input. Exit..')
		except:
			sys.exit('Error on input. Exit...')
		try:
			mileage = int(mileage)
			if mileage >= 0:
				break
			else:
				print('Not a valid value for the mileage')
		except ValueError:
			print('Not a valid value for the mileage')
	return (mileage)

def	getThetas(thetas):
	t0, t1 = 0, 0
	if (os.path.isfile(thetas)):
		with open(thetas, 'r') as csvfile:
			file = csv.reader(csvfile, delimiter=',')
			for row in file:
				t0 = float(row[0])
				t1 = float(row[1])
				break
	return (t0, t1)

def	main():
	thetas = getThetas(getPath('thetas.csv'))
	mileage = getMileage()
	mileages, prices = getData(getPath('data.csv'))
	price = estimatePrice(thetas, mileage, mileages, prices)
	if price < 0:
		price = "{} (Don't buy this shit)".format(price)
	print('The price for this mileage is: {}'.format(price))

if __name__ == "__main__":
	main()
