import read
import get
import write

inputfile = 'INPUT'
# 读取命令文件、数据文件
cmd = read.read_cmd(inputfile)
mole = read.read_in(cmd)

# 初始化

mole = get.verlet_list(cmd, mole)
if cmd['model'] == 'LJ':
    potential = read.defineLJ(cmd)

[u, force] = get.u_force(mole, potential)

print(u)
write.energy(u)
write.force(force)
# print(mole.nlist[11])
# print(mole.list[11])
# write.verlet_list(mole, 12)
