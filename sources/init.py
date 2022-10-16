import read
import get
import loop
import write

inputfile = 'INPUT'

# 读取命令文件、数据文件
cmd = read.read_cmd(inputfile)
mole = read.read_in(cmd)

# 选择势函数
if cmd['model'] == 'LJ':
    potential = read.defineLJ(cmd)

# 设置初速度
if cmd['read_v'] == '0' or mole.velocity == []:
    mole = get.vbegin(int(cmd['t_begin']))

# # 设置算法选项
# if cmd[''] == '':
#     loop.V_verlet(mole, cmd)

# 建立储存文件

mole = get.verlet_list(cmd, mole)
[u, force] = get.u_force(mole, potential)

print(u)
