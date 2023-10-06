def summ():
	a = 5.0
	b = 6.0
	c = b+a
	print(c)
	print(type(c))
	#adding floats and printing the type of the sum

def difference():
	d = 10
	e = 5
	print(d-e)
	print(type(d-e))

def product():
	b = 6.0
	e = 5
	print(b*e)
	print(type(b*e))

def main():
	summ()
	difference()
	product()
	#calls all three functions

if __name__ == "__main__":
	main()