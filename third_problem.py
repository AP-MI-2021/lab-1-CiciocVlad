def cmmdc(a, b):
	r = a % b
	while r > 0:
		a = b
		b = r
		r = a % b
	return b


def cmmdc2(a, b):
	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
	return a

a = int(input('a = '))
b = int(input('b = '))
print(cmmdc(a, b))
print(cmmdc2(a, b))
