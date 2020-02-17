# 
# hw1_task1.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 17 February 2020
# 

import pickle 

def bin_func(data,bin,c):
	"""Assigns pixel inensity to proper bin"""
	for x in range(len(data)):
		for y in range(len(data[x])):
			if data[x][y][c] < 64:
				bin['1']=bi   n['1']+1
			elif data[x][y][c] < 128:
				bin['2']=bin['2']+1
			elif data[x][y][c] < 192:
				bin['3']=bin['3']+1
			else:
				bin['4']=bin['4']+1

with open('image_matrix', 'rb') as pickle_file:
	data = pickle.load(pickle_file)

# dictionay that holds the RBG values
bin_dict={
'red_bin':{'1':0,'2':0,'3':0,'4':0},
'green_bin':{'1':0,'2':0,'3':0,'4':0},
'blue_bin':{'1':0,'2':0,'3':0,'4':0}
}

#calls function
bin_func(data,bin_dict['red_bin'],0)
bin_func(data,bin_dict['green_bin'],1)
bin_func(data,bin_dict['blue_bin'],2)

#final results
print(bin_dict)