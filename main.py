import read
import get
import loop


inputfile = 'INPUT'
# 读取命令文件、数据文件
cmd = read.read_cmd(inputfile)
mole = read.read_in(cmd)

# 初始化
# 选择势函数
if cmd['model'] == 'LJ':
    potential = read.defineLJ(cmd)
# 设置初速度
if cmd['read_v'] == '0':
    mole = get.vbegin(int(cmd['t_begin']))


loop.V_verlet(mole, cmd, potential)
