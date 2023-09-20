from geoshit_fun import *

# make grid of elevations (map) form data
grid = BIG_grid('DMV1000')

# grid correction (averages empty elements)
grid = remove_empyt(grid)

# plot part

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

# textbox

fig.subplots_adjust(bottom=0.2)

# The function to be called from txtbox
def update(val):
	pic.set_data(mask(grid, int(val)))
	fig.canvas.draw_idle()

# okno
from matplotlib.widgets import TextBox

axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "nmv")
text_box.on_submit(update)
text_box.set_val(1)

plt.show()

