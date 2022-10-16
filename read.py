import numpy as np


class mol():                        # 分子类
    def __init__(self):
        self.id = ''                # 分子id
        self.num = 0                # 分子数
        self.mass = 0               # 分子质量
        self.cell = []              # Cell
        self.position = []          # 分子坐标
        self.velocity = []          # 分子速度
        self.acceleration = []      # 分子加速度
        self.nlist = []             # 近邻分子数
        self.list = []              # 近邻分子序号


class LJ():                         # LJ势
    def __init__(self):
        self.sigma = 0.0            # sigma
        self.epsilon = 0.0          # epsilon
        self.u_rcut = 0.0           # 截断半径势能
        self.rcut = 0.0             # 截断半径

    def fun(self, x):                   # 势函数
        if abs(x[0]) > self.rcut:
            u = 0
            force = np.array([0, 0, 0])
        elif abs(x[1]) > self.rcut:
            u = 0
            force = np.array([0, 0, 0])
        elif abs(x[2]) > self.rcut:
            u = 0
            force = np.array([0, 0, 0])
        else:
            r_2 = x[0] * x[0] + x[1] * x[1] + x[2] * x[2]
            if (r_2 <= self.rcut * self.rcut):
                B = pow(self.sigma, 6) / pow(r_2, 3)
                A = B * B
                u = 4 * self.epsilon * (A - B) - self.u_rcut
                force = (4 * self.epsilon * (12 * A - 6 * B) / r_2) * x
            else:
                u = 0
                force = np.array([0, 0, 0])

        return [u, force]


# 读取命令文件
def read_cmd(inputfile):
    f = open(inputfile, 'r')
    # 读取文件并去除空隙
    file = [line.strip() for line in f.readlines() if line.strip()]
    f.close()
    # 建立命令字典
    cmd = {}
    for line in file:
        info = line.split()
        cmd[info[0]] = info[1]

    return cmd


# 读取输入CELL_PARAMETER、位置、速度
def read_in(cmd):
    f = open(cmd['geo_dir'], 'r')
    # 读取文件并去除空隙
    flist = np.array([line.strip() for line in f.readlines() if line.strip()])
    f.close()

    mole = mol()
    mole.id = cmd['id']
    N = int(cmd['natom'])
    mole.num = N
    mole.mass = float(cmd['molar_mass'])

    # CELL_PARAMETER
    cell = np.array(np.char.split(flist[1:4]).tolist())[:, :].astype(float)
    mole.cell = cell

    # 读取id分子的坐标
    strlist = flist[np.char.find(flist, cmd['id'])+1 > 0]
    position = np.array(np.char.split(strlist).tolist())[:N, 1:].astype(float)
    mole.position = position
    # 读取id分子的速度
    if cmd['read_v'] == '1':
        velocity = np.array(np.char.split(strlist).tolist())[N:, 1:].astype(float)
        mole.velocity = velocity

    return mole


# 建立LJ势函数的类
def defineLJ(cmd):
    potential = LJ()
    potential.epsilon = float(cmd['epsilon'])
    potential.sigma = float(cmd['sigma'])
    potential.rcut = float(cmd['rcut'])
    # 计算截断半径处的势能
    [u, f] = potential.fun(np.array([potential.rcut, 0, 0]))
    potential.u_rcut = u

    return potential
