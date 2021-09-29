import re

def prim(n):
	return not re.match(r'^1?$|^(11+?)\1+$', '1' * n)

nr = input('n = ')
print(prim(int(nr)))