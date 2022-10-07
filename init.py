import read
import get
import write

inputfile = 'INPUT'
# 读取命令文件、数据文件
cmd = read.read_cmd(inputfile)
mole = read.read_in(cmd)

# 初始化
if cmd['model'] == 'LJ':
    LJ = read.defineLJ(cmd)