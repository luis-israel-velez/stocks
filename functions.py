import numpy as np
import math


def test():
	print("Test")

def formatPrice(n):
	return ("-$" if n < 0 else "$") + "{0:.2f}".format(abs(n))

def getStockDataVec(key, ftype):
	vec = []

	lines = open("data/" + key + "." + ftype, "r").read().splitlines()

    
	for line in lines[1:]:
		vec.append(float(line.split(",")[4]))

	return vec

# returns the sigmoid
def sigmoid(x):
	return 1 / (1 + math.exp(-x))

def getState(data, t, n):
	d = t - n + 1

	block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] #pad with t0
	res = []

	for i in range(n - 1):
		res.append(sigmoid(block[i + 1] - block[i]))

	return np.array([res])