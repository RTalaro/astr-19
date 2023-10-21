import math as m
import numpy as np
from astropy.table import Table
from astropy.io import ascii

def main():
	x=np.linspace(0,2*m.pi,1000)
	y=m.sin(x)
	data=Table([y,x],names=['sin(x)','x'])
	ascii.write(data,'table.txt',format='commented_header')
	data_in=ascii.read('table.txt')
	print(data_in)

if __name__=='__main__':
	main()