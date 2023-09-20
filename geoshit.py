from geoshit_fun import *

dir_name = 'DMV1000\\'

names = os.listdir('DMV1000')

A_names = []
i = 0
while names[i][2] == 'A':
	A_names.append(names[i])
	i += 1

'''
grid_0 = make_grid(dir_name+A_names[0])
for i in range(1, 3):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
grid_right = np.copy(grid_0)

grid_0 = make_grid(dir_name+A_names[3])
for i in range(4, 6):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
grid = np.concatenate((grid_0, grid_right), axis=1)
plt.imshow(grid)
plt.show()
'''

# do sem ok

#############################

'''
grid_0 = make_grid(dir_name+A_names[6])
for i in range(7, 8):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
grid_right = np.copy(grid_0)
plt.imshow(grid_0)
plt.show()
'''

# nikjer ne paše

#######################
'''
grid_0 = make_grid(dir_name+A_names[12])
for i in range(13, 18):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
grid_right = np.copy(grid_0)
plt.imshow(grid_0)
plt.show()
'''
############################
grid_0 = make_grid(dir_name+A_names[18])
for i in range(19, 23):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
grid_right = np.copy(grid_0)
plt.imshow(grid_0)
plt.show()



grid_0 = make_grid(dir_name+A_names[23])
for i in range(24, 28):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
#grid_right = np.copy(grid_0)
plt.imshow(grid_0)
plt.show()


grid = np.concatenate((grid_0, grid_right), axis=1)
plt.imshow(np.rot90(np.flip(grid, axis=0)))
plt.show()

# 18-28 ok (25 16-20, 25 26-30)

####################################

'''
grid_0 = make_grid(dir_name+A_names[28])
for i in range(29, 30):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
#grid_right = np.copy(grid_0)
plt.imshow(grid_0)
plt.show()
'''
##############################
'''
grid_0 = make_grid(dir_name+A_names[8])
for i in range(9, 10):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
grid_right = np.copy(grid_0)
plt.imshow(grid_0)
plt.show()

grid_0 = make_grid(dir_name+A_names[10])
for i in range(11, 12):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
plt.imshow(grid_0)
plt.show()

grid = np.concatenate((grid_0, grid_right), axis=1)
plt.imshow(grid)
plt.show()
'''
# 8-11 4 lepo pašejo skupi (39, 40; 49, 50)

############################################

'''
grid_0 = make_grid(dir_name+A_names[8])
for i in range(9, 10):
	grid = make_grid(dir_name+A_names[i])
	grid_0 = np.concatenate((grid, grid_0), axis=0)

print(np.shape(grid_0))
grid = np.concatenate((grid_0, grid_right), axis=1)
plt.imshow(grid)
plt.show()
'''
'''
name = 'DMV1000\\VTA2308D96.XYZ'
name1 = 'DMV1000\\VTA2309D96.XYZ'

grid = make_grid(name)
grid1  = make_grid(name1)
print(np.shape(grid), 'y')
print(np.shape(grid1), 'y')
fig, ax = plt.subplots(2)

ax[1].imshow(grid)
ax[0].imshow(grid1)
plt.show()

'''
