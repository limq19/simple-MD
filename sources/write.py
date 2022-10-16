# import numpy as np


def verlet_list(mole, num):
    name = 'verlet' + str(num) + '.list'
    f = open(name, 'w')
    f.write('verlet list(Angstrom)\n')
    f.write('mole number %d \n' % num)
    f.write('neighbor number %d \n' % mole.nlist[num - 1])
    f.write('number        x              y              z \n')
    for i in mole.list[num - 1]:
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i, mole.position[i - 1, 0], mole.position[i - 1, 1], mole.position[i - 1, 2]))
    f.close()


def energy(energy):
    f = open('energy.txt', 'w+')
    f.write('energy(eV)  %.12g' % energy)
    f.close()


def position(mole):
    f = open('position.txt', 'w+')
    f.write('position(Angstrom)\n')
    f.write('mole number %d \n' % mole.num)
    f.write('\n step 0 time(ps) 0 \n')
    f.write('number         x               y               z \n')
    for i in range(mole.num):
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i + 1, mole.position[i, 0], mole.position[i, 1], mole.position[i, 2]))
    f.close()


def addposition(position, step, time):
    f = open('position.txt', 'a+')
    f.write('\n step %d time(ps) %.8g \n' % (step, time))
    f.write('number         x               y               z \n')
    for i in range(len(position)):
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i + 1, position[i, 0], position[i, 1], position[i, 2]))
    f.close()


def velocity(mole):
    f = open('velocity.txt', 'w+')
    f.write('velocity(Angstrom/ps)\n')
    f.write('mole number %d \n' % mole.num)
    f.write('\n step 0 time(ps) 0 \n')
    f.write('number         Vx               Vy               Vz \n')
    for i in range(mole.num):
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i + 1, mole.velocity[i, 0], mole.velocity[i, 1], mole.velocity[i, 2]))
    f.close()


def addvelocity(velocity, step, time):
    f = open('velocity.txt', 'a+')
    f.write('\n step %d time(ps) %.8g \n' % (step, time))
    f.write('number         Vx               Vy               Vz \n')
    for i in range(len(velocity)):
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i + 1, velocity[i, 0], velocity[i, 1], velocity[i, 2]))
    f.close()


def force(force):
    f = open('force.txt', 'w+')
    f.write('Force(eV/Angstrom)\n')
    f.write('mole number %d \n' % len(force))
    f.write('number        Fx              Fy              Fz \n')
    for i in range(len(force)):
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i + 1, force[i, 0], force[i, 1], force[i, 2]))
    f.close()


def addforce(force, step, time):
    f = open('force.txt', 'a+')
    f.write('\n step %d time %.8g \n' % (step, time))
    f.write('number        Fx              Fy              Fz \n')
    for i in range(len(force)):
        f.write('%4d %14.12g %14.12g %14.12g \n' % (i + 1, force[i, 0], force[i, 1], force[i, 2]))
    f.close()


def run(E, u, Kinetic, temp, step, time):
    f = open('run.log', 'w+')
    f.write('n  t(ps)     E(eV)       u(eV)       Kinetic(eV)       temp(K) \n')
    f.write('%d %4.12g %14.12g %14.12g %14.12g %14.12g\n' % (step, time, E, u, Kinetic, temp))
    f.close()


def addrun(E, u, Kinetic, temp, step, time):
    f = open('run.log', 'a+')
    f.write('%d %4.12g %14.12g %14.12g %14.12g %14.12g\n' % (step, time, E, u, Kinetic, temp))
    f.close()
