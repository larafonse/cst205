# 
# hw1_task2.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 17 February 2020
# 

import hw1_hist_plotter as hp
import pickle


def task2(my_file):
	"""creates a list containing 3 lists of RGB"""
	list=[]
	redlist=[]
	greenlist=[]
	bluelist=[]
	for x in range(len(my_file)):
		for y in range(len(my_file[x])):
			redlist.append(my_file[x][y][0])
			greenlist.append(my_file[x][y][1])
			bluelist.append(my_file[x][y][2])
	list.append(redlist)
	list.append(greenlist)
	list.append(bluelist)
	return list

with open('image_matrix', 'rb') as pickle_file:
	my_file = pickle.load(pickle_file)

hp.hist_plotter(task2(my_file))
