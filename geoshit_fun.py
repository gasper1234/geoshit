import numpy as np
import matplotlib.pyplot as plt
import os
import csv
def remove_empyt(grid):
	for i in range(np.shape(grid)[0]):
		for j in range(1, np.shape(grid)[1]-1):
			if grid[i, j] == 0 and (grid[i, j-1] != 0 and grid[i, j+2] != 0):
				grid[i, j] = (grid[i, j-1] + grid[i, j+2]) / 2
	return grid

def BIG_grid(dir_name):

	names = os.listdir(dir_name)

	x_min = 373628
	x_max = 625631
	y_min = 28485
	y_max = 196483

	x_size = (x_max-x_min)//100 + 1
	y_size = (y_max-y_min)//100 + 1

	grid = np.empty((y_size, x_size))

	dir_name = dir_name+'/'
	for name in names:
		with open(dir_name+name) as file:
			xyz = np.loadtxt(file, dtype=float)

		xyz = np.round(xyz)

		XYZ = xyz.astype(int)

		for i in range(np.shape(XYZ)[0]):
			x_ind = (XYZ[i,0]-x_min)//100
			y_ind = (XYZ[i,1]-y_min)//100
			grid[y_size-1-y_ind, x_ind] = XYZ[i,2]

	return grid

def x_to_grid(val):
	off_left = 11
	off_right = 2490
	diff_grid = off_right-off_left
	x_min = 13.37546315674604
	x_max = 16.596696762097793
	diff = x_max-x_min
	return (val-x_min)/diff * diff_grid + off_left

def y_to_grid(val):
	off_up = 26
	off_down = 1651
	diff_grid = off_down - off_up
	y_min = 45.421429998316384
	y_max = 46.876668395213315
	diff = y_max-y_min
	return (y_max-val)/diff * diff_grid + off_up

def make_grid(name):
	with open(name) as file:
		xyz = np.loadtxt(file, dtype=float)

	xyz = np.round(xyz)
	grid_size = len(xyz[:,0])
	##################
	x_len = 0
	y_0 = xyz[0,1]
	for i in range(grid_size):
		if abs(xyz[i,1] - y_0) > 1:
			break
		else:
			x_len += 1
	y_len = grid_size//x_len
	print(y_len, x_len)
	#######################
	grid = np.zeros((x_len, y_len))

	for y in range(y_len):
		for x in range(x_len):
			grid[x_len-1-x, y] = xyz[y*x_len+x, 2]

	return grid