import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

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
	return (y_max-val)/diff * diff_grid + off_up

csv.field_size_limit(10**7)

glob_data_x = np.zeros(54557)
glob_data_y = np.zeros(54557)
glob_i = 0

with open('SLO_meja.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	i=0
	for row in csv_reader:
		if i < 260 and i > 0:
			print(i)
			# podatki iz vrstic

			data_x = []
			data_y = []
			for clust in row[-1][14:-1].split(','):
				data_x.append(x_to_grid(float(clust.strip().split(' ')[0])))
				data_y.append(y_to_grid(float(clust.strip().split(' ')[1])))

			plt.plot(data_x, data_y)

		if i == 260:

			# podatki iz vrstic

			data_x = []
			data_y = []
			for clust in row[-1][15:-1].split(','):
				data_x.append(x_to_grid(float(clust.strip().split(' ')[0])))
				data_y.append(y_to_grid(float(clust.strip().split(' ')[1])))

			plt.plot(data_x, data_y)

		i += 1
plt.show()