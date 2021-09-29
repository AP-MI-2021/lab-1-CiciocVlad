import re
from functools import reduce
import operator


def is_prime(n):
	return not re.match(r'^1?$|^(11+?)\1+$', '1' * n)
  
 
def get_product(lst):
	return reduce(operator.mul, lst)

 
def get_cmmdc_v1(x, y):
	r = x % y
	while r > 0:
		x = y
		y = r
		r = x % y
	return y
 
  
def get_cmmdc_v2(x, y):
	while x != y:
		if x > y:
			x -= y
		else:
			y -= x
		return y

  
def main():
	n = int(input('n = '))
	print(is_prime(n))
	n = int(input('n = '))
	arr = []
	for i in range(n):
		arr.append(int(input()))
	print(get_product(arr))
	x = int(input('x = '))
	y = int(input('y = '))
	print(get_cmmdc_v1(x, y))
	print(get_cmmdc_v2(x, y))


if __name__ == '__main__':
	main()