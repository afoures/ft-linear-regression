from train import getPath, getData
from estimate import getThetas, estimatePrice

def getAccuracy(thetas, mileages, prices):
    price_average = sum(prices) / len(prices)
    ssr = sum(map(lambda mileage, price: pow(
        price - estimatePrice(thetas, mileage, mileages, prices), 2
    ), mileages, prices))
    sst = sum(map(lambda price: pow(price - price_average, 2), prices))
    return (1 - (ssr / sst))

def main():
    thetas = getThetas(getPath('thetas.csv'))
    mileages, prices = getData(getPath('data.csv'))
    accuracy = getAccuracy(thetas, mileages, prices)
    print("ft-linear-regression accuracy is: {}".format(accuracy))

if __name__ == "__main__":
    main()
