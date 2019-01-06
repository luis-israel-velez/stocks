


def test():
	print("Test")



def getStockDataVec(key, ftype):
	vec = []

	lines = open("data/" + key + "." + ftype, "r").read().splitlines()

    
	for line in lines[1:]:
		print("Hello " + line)
		vec.append(float(line.split(",")[4]))

	return vec

