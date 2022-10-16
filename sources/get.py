import numpy as np


# 近邻表
def verlet_list(cmd, mole):
    N = int(cmd['natom'])
    rcut = float(cmd['rcut'])
    neighbor_r = float(cmd['neighbor_r'])
    # neighbor_n = int(cmd['neighbor_n'])
    r_v = rcut + neighbor_r
    # 目前只针对正交cell可以用
    box = [mole.cell[0][0], mole.cell[1][1], mole.cell[2][2]]
    mole.nlist = np.zeros(N, dtype=int)
    mole.list = [[] for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            x = mole.position[i, :] - mole.position[j, :]
            # 加入周期性边界条件
            xr = x - box * np.rint(x / box)
            # 计算近邻并储存
            if abs(xr[0]) > r_v:
                continue
            elif abs(xr[1]) > r_v:
                continue
            elif abs(xr[2]) > r_v:
                continue
            else:
                d = xr[0] * xr[0] + xr[1] * xr[1] + xr[2] * xr[2]
                if d < r_v * r_v:
                    mole.list[i].append(j + 1)
                    mole.nlist[i] = mole.nlist[i] + 1
                    mole.list[j].append(i + 1)
                    mole.nlist[j] = mole.nlist[j] + 1

    return mole


# 总势能和力
def u_force(mole, potential):
    u = 0
    force = np.zeros([mole.num, 3])
    for i in range(mole.num):
        for j in mole.list[i]:
            # 在近邻表中
            if j > i:
                x = mole.position[i, :] - mole.position[j - 1, :]
                # 加入周期性边界条件
                xr = x - mole.cell[0][0] * np.rint(x / mole.cell[0][0])

                [u_e, force_e] = potential.fun(xr)
                u = u + u_e
                # 正负号为方向
                force[i, :] = force[i, :] + force_e
                force[j - 1, :] = force[j - 1, :] - force_e

    return [u, force]


# 计算温度、总动能
def K_temp(mole):
    k = 1.38064852e-23
    NA = 6.02214086e+23
    e = 1.602176634e-19
    Kinetic = 0
    for i in range(mole.num):
        Kinetic = Kinetic + (mole.mass / 2) * (mole.velocity[i, 0] * mole.velocity[i, 0]
                                               + mole.velocity[i, 1] * mole.velocity[i, 1]
                                               + mole.velocity[i, 2] * mole.velocity[i, 2])
    # 动能单位eV、温度单位K
    Kinetic = Kinetic / (NA * e / 10)
    temp = (2 * Kinetic * e)/(3 * mole.num * k)
    return [Kinetic, temp]


# 设置随机初始速度
def vbegin(mole, tbegin):

    mole.velocity = []

    return mole
