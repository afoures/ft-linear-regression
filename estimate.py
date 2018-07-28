import math
import csv
import sys
import os
from train import normalizeElem, denormalizeElem, getData

t0 = 0.0
t1 = 0.0

def	estimatePrice(mileage, mileages, prices):
	price = t1 * normalizeElem(mileages, mileage) + t0
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
	global t0, t1
	if (os.path.isfile(thetas)):
		with open(thetas, 'r') as csvfile:
			file = csv.reader(csvfile, delimiter=',')
			for row in file:
				t0 = float(row[0])
				t1 = float(row[1])
				break

def	main():
	getThetas('thetas.csv')
	mileage = getMileage()
	mileages, prices = getData('data.csv')
	price = math.ceil(estimatePrice(mileage, mileages, prices))
	if price < 0:
		price = "0 (Don't buy this shit)"
	print('The price for this mileage is: {}'.format(price))

if __name__ == "__main__":
	main()
