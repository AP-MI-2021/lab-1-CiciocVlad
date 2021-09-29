import operator
from functools import reduce

n = int(input('n = '))
arr = []
for i in range(n):
	arr.append(int(input()))
print(reduce(operator.mul, arr))