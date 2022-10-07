import numpy as np


# 近邻表
def verlet_list(cmd, mole):
    N = int(cmd['natom'])
    rcut = float(cmd['rcut'])
    neighbor_r = float(cmd['neighbor_r'])
    # neighbor_n = int(cmd['neighbor_n'])
    r_v = rcut + neighbor_r
    # 目前只针对正方体可以用
    box = mole.cell[0][0]
    mole.nlist = np.zeros(N, dtype=int)
    mole.list = [[] for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            x = mole.position[0][i, :] - mole.position[0][j, :]
            # 加入周期性边界条件
            xr = x - box * np.rint(x / box)
            # 计算近邻并储存
            d = xr[0] * xr[0] + xr[1] * xr[1] + xr[2] * xr[2]
            if d < r_v * r_v:
                mole.list[i].append(j + 1)
                mole.nlist[i] = mole.nlist[i] + 1
                mole.list[j].append(i + 1)
                mole.nlist[j] = mole.nlist[j] + 1

    return mole


# 力
def u_force(mole, potential):
    u = 0
    force = np.zeros([mole.num, 3])
    for i in range(mole.num):
        for j in range(i+1, mole.num):
            # 在近邻表中
            if (j+1) in mole.list[i]:
                x = mole.position[0][i, :] - mole.position[0][j, :]
                # 加入周期性边界条件
                xr = x - mole.cell[0][0] * np.rint(x / mole.cell[0][0])
                sqr_r = xr[0] * xr[0] + xr[1] * xr[1] + xr[2] * xr[2]
                # 在截断半径内有值
                if sqr_r < potential.rcut * potential.rcut:
                    [u_e, force_e] = potential.fun(xr, sqr_r)
                    u = u + u_e
                    # 正负号为方向
                    force[i, :] = force[i, :] + force_e
                    force[j, :] = force[j, :] - force_e

    return [u, force]
