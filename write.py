# import numpy as np


def verlet_list(mole, num):
    name = 'verlet' + str(num) + '.list1'
    f = open(name, 'w')
    f.write('verlet list\n')
    f.write('mole number %d \n' % num)
    f.write('neighbor number %d \n' % mole.nlist[num - 1])
    f.write('number        x              y              z \n')
    for i in mole.list[num - 1]:
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i, mole.position[0][i - 1, 0], mole.position[0][i - 1, 1], mole.position[0][i-1, 2]))


def force(force):
    name = 'force.txt'
    f = open(name, 'w+')
    f.write('Force(eV/Angstrom)\n')
    f.write('mole number %d \n' % len(force))
    f.write('number        Fx              Fy              Fz \n')
    for i in range(len(force)):
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i + 1, force[i, 0], force[i, 1], force[i, 2]))


def energy(energy):
    name = 'energy.txt'
    f = open(name, 'w+')
    f.write('energy(eV)  ')
    f.write('%.12g' % energy)
