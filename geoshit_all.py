from geoshit_fun import *

dir_name = 'DMV1000\\'

names = os.listdir('DMV1000')

def BIG_grid():
	x_min = 373628
	x_max = 625631
	y_min = 28485
	y_max = 196483

	x_size = (x_max-x_min)//100 + 1
	y_size = (y_max-y_min)//100 + 1

	grid = np.empty((y_size, x_size))

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

grid = BIG_grid()

# korekcija

import time

start = time.time()
for i in range(np.shape(grid)[0]):
	for j in range(1, np.shape(grid)[1]-1):
		if grid[i, j] == 0 and (grid[i, j-1] != 0 and grid[i, j+2] != 0):
			grid[i, j] = (grid[i, j-1] + grid[i, j+2]) / 2
			print(True)
print(time.time()-start)

def mask(grid, mask):
	return np.ma.masked_where(grid<mask,grid)

init_mask = 1

fig, ax = plt.subplots()

pic = ax.imshow(mask(grid, init_mask))

# draw border

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

			ax.plot(data_x, data_y, color='red')

		if i == 260:

			# podatki iz vrstic

			data_x = []
			data_y = []
			for clust in row[-1][15:-1].split(','):
				data_x.append(x_to_grid(float(clust.strip().split(' ')[0])))
				data_y.append(y_to_grid(float(clust.strip().split(' ')[1])))

			ax.plot(data_x, data_y, color='red')

		i += 1

# end od drawing border

fig.subplots_adjust(left=0.25)

from matplotlib.widgets import Slider

# Make a vertically oriented slider to control the amplitude
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
	ax=axamp,
	label="Amplitude",
	valmin=1,
	valmax=2900,
	valinit=init_mask,
	orientation="vertical"
)

# The function to be called anytime a slider's value changes
def update(val):
	pic.set_data(mask(grid, amp_slider.val))
	fig.canvas.draw_idle()


# register the update function with each slider
amp_slider.on_changed(update)

plt.show()

