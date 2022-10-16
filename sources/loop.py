import sources.get as get
import sources.write as write
import numpy as np
# from numba import jit


# @jit(nopython=True)
def V_verlet(mole, cmd, potential):
    dt = float(cmd['step_length'])
    nstep = int(cmd['nstep'])
    nstep_search = int(cmd['nstep_search'])
    nstep_out = int(cmd['nstep_out'])
    box = [mole.cell[0][0], mole.cell[1][1], mole.cell[2][2]]
    NA = 6.02214086e+23
    e = 1.602176634e-19

    mole = get.verlet_list(cmd, mole)

    # 建立输出文件，并输出初始数据
    [u, force] = get.u_force(mole, potential)
    [Kinetic, temp] = get.K_temp(mole)
    write.position(mole)
    write.velocity(mole)
    write.force(force)
    write.run(u + Kinetic, u, Kinetic, temp, 0, 0)
    for i in range(nstep):
        # 更新近邻表
        if ((i % nstep_search) == 0) and (i != 0):
            mole = get.verlet_list(cmd, mole)

        position = mole.position + dt * mole.velocity + (NA * e / 10) * force * dt * dt / (2 * mole.mass)
        # 周期性边界
        mole.position = position - box * np.floor(position / box)

        [u, force_after] = get.u_force(mole, potential)
        mole.velocity = mole.velocity + (NA * e / 10) * dt * (force + force_after) / (2 * mole.mass)

        # 输出下一时刻数据
        if ((i + 1) % nstep_out) == 0:
            [Kinetic, temp] = get.K_temp(mole)
            write.addposition(mole.position, (i + 1), (i + 1) * dt)
            write.addvelocity(mole.velocity, (i + 1), (i + 1) * dt)
            write.addforce(force_after, (i + 1), (i + 1) * dt)
            write.addrun(u + Kinetic, u, Kinetic, temp, (i + 1), (i + 1) * dt)

        force = force_after

    return 0
