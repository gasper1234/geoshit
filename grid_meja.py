import numpy as np

data_x = np.load('unordered_x.npy')
data_y = np.load('unordered_y.npy')

data_x_min = np.min(data_x)
data_x_max = np.max(data_x)
data_y_min = np.min(data_y)
data_y_max = np.max(data_y)
print(data_x_min)
print(data_x_max)
print(data_y_min)
print(data_y_max)
def x_to_grid(val):
	off_left = 11
	off_right = 2504
	diff_grid = off_right-off_left
	x_min = 13.37546315674604
	x_max = 16.596696762097793
	diff = x_max-x_min
	return (val-x_min)/diff * diff_grid + off_left

def y_to_grid(val):
	off_up = 14
	off_down = 1651
	diff_grid = off_down - off_up
	y_min = 45.421429998316384
	y_max = 46.876668395213315
	diff = y_max-y_min
	return (x_max-val)/diff * diff_grid + off_up

x_min = 373628
x_max = 625631
y_min = 28485
y_max = 196483

x_size = (x_max-x_min)//100 + 1
y_size = (y_max-y_min)//100 + 1

grid = np.empty((y_size, x_size))

