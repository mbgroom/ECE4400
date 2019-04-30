import numpy as np
import sys
import random


def generate_numbers(_range, filename, tn):

	''' Parameters:

	_range		: list(starting, ending)
	filename 	: Name of the file
	tn		: total numbers to be generated'''

	f = open(filename, "wb")
	for i in range(tn): 
		f.write((random.randint(_range[0],_range[1])).to_bytes(1,"big"))

def generate_exp(filename, _range, pr, tn, hn):
	
	''' Parameters:
	
	filename 	: Name of the file
	_range 		: list(starting, ending)
	pr 		: range of priority is a list
	tn 		: total numbers
	hn 		: number of high priority numbers '''

	f = open(filename,"wb")
	x = list()
	for i in range(tn):
		if(i < hn):
			x.append(random.randint(pr[0],pr[1]))
		else:
			x.append(random.randint(_range[0],_range[1]))
	
	np.random.shuffle(np.array(x))

	for i in x:
		f.write(i.to_bytes(1,"big")) 
