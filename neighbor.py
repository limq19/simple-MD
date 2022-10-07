import numpy as np
import read
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


inputfile = 'INPUT'
# 读取命令文件、数据文件
cmd = read.read_cmd(inputfile)
[cell, mole] = read.read_in(cmd['id'], cmd['geo_dir'])

N = int(cmd['natom'])
rcut = float(cmd['rcut'])
neighbor_r = float(cmd['neighbor_r'])
neighbor_n = int(cmd['neighbor_n'])
r_v = rcut + neighbor_r
box = cell[0][0]

for i in range(N):
    for j in range(i+1, N):
        x = mole[i].position[0] - mole[j].position[0]
        # 加入周期性边界条件
        xr = x - box * np.rint(x / box)
        d = xr[0] * xr[0] + xr[1] * xr[1] + xr[2] * xr[2]
        if d < r_v * r_v:
            mole[i].nlist = mole[i].nlist + 1
            mole[i].list.append(j)
            mole[j].nlist = mole[j].nlist + 1
            mole[j].list.append(i)

print(mole[11].nlist)
print(mole[11].list)


z = mole[11].position[0]
x = np.zeros([mole[11].nlist, 3])
j = 0
for i in mole[11].list:
    # if mole[i].position[0][1] > z[1]:
    x[:][j] = mole[i].position[0]
    j = j+1

y = np.zeros([N, 3])
j = 0
for i in range(N):
    if i in mole[11].list:
        continue
    else:
        # if mole[i].position[0][1] > z[1]:
        y[:][j] = mole[i].position[0]
        j = j+1

fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x1 = z[0] + r_v * np.outer(np.cos(u), np.sin(v))
y1 = z[1] + r_v * np.outer(np.sin(u), np.sin(v))
z1 = z[2] + r_v * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x1, y1, z1, color='b', cmap=cm.coolwarm)
ax.scatter(y[:, 0], y[:, 1], y[:, 2], c='g')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], c='r')
ax.scatter(z[0], z[1], z[2], s=80, c='b', marker='p')
plt.show()
