import sys
class Animal: #creates Animal class
	def print(self):
		print('My favorite animal is the squirrel.')
		print(f'Length of the arms: {self.armlength} cm')
		print(f'Length of the legs: {self.leglength} cm')
		print(f'Number of eyes: {self.neyes} eyes')
		print(f'Tail? {self.tail}')
		print(f'Furry? {self.furry}')

	def __init__(self,armlength,leglength,neyes,tail,furry):
		self.armlength=armlength
		self.leglength=leglength
		self.neyes = neyes
		self.tail=tail
		self.furry=furry

def main():
	armlength=3.5
	leglength=4.5
	neyes=2
	tail=True
	furry=True
	squirrel=Animal(armlength=armlength,leglength=leglength,neyes=neyes,tail=tail,furry=furry)
	squirrel.print()

if __name__=='__main__':
	main()