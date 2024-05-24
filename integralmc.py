# Use a python formatted string for the function you want to integrate. Variable must be x

integral = 'math.sin(x)'
#integral = 'pow(x, 3)'
#integral = '3 * math.sin(2*x) + 1'
#integral = '1 / math.sqrt(8*x + 9)'
#integral = 'math.sin(x) - math.cos(x)'

# Do not modify anything under this line

def func(strfunc, x):
    try:
        return eval(strfunc)
    except:
        return None

import random
import matplotlib.pyplot as plt
import math
pt = 0
pcp = 0
pcn = 0
px = []
py = []

def extrema(equ, limi, lims):
    miny = 0
    maxy = 0
    j = limi
    while j <= lims+0.1:
        test = func(equ, j)
        if test == None:
            j = j + 0.1
            continue
        if miny is None:
            miny = test
            maxy = test
        if test < miny:
            miny = test
        if test > maxy:
            maxy = test
        j = j + 0.1
    return math.floor(miny), math.ceil(maxy)

def montecarlo(equ, p, lb, ub):
    try:
        if equ.strip() == '':
            equ = '1'
        miny, maxy = extrema(equ, lb, ub)
        if miny == 0 and maxy == 0:
            return
        if __name__ == '__main__':
            global pt, pcp, pcn, px, py
        else:
            pt = 0
            pcp = 0
            pcn = 0
            px = []
            py = []
        if p > 100000:
            p = 100000
        for i in range(p):
            pt = pt + 1
            x = random.uniform(lb, ub)
            y = random.uniform(miny, maxy)
            if func(equ, x) == None:
                continue
            if func(equ, x) > 0:
                if y > 0 and y <= func(equ, x):
                    pcp = pcp + 1
                    px.append(x)
                    py.append(y)
            else:
                if y < 0 and y >= func(equ, x):
                    pcn = pcn + 1
                    px.append(x)
                    py.append(y)

        area = (ub - lb) * (maxy - miny)
        mp = pcp / pt
        mn = pcn / pt
        res = (area * mp) - (area * mn)
        if __name__ != '__main__':
            return res
        print('\nIntegral of', equ, 'on the interval','[', lb, ',', ub, ']')
        print('Ordinate limits: [', miny, ',', maxy, ']')
        print('Last point: [', x, ',', y, ']')
        print('Total points: ', pt)
        print('Scattered points: ', pcp + pcn)
        print('Result: ', res)
        plt.scatter(px, py)
        plt.show()
        menu(lb, ub)
    except:
        return

def menu(lb, ub):
    while True:
        try:
            n = int(input("\nPoints to scatter (0 to exit): "))
            break
        except ValueError:
            pass
    if n == 0:
        raise SystemExit
    montecarlo(integral, n, lb, ub)

def execute():
    print('Integral of', integral, 'by Monte Carlo method')
    while True:
        try:
            lb = float(input("Lower bound (from): "))
            break
        except ValueError:
            pass
    while True:
        try:
            ub = float(input("Upper bound (to): "))
            if ub > lb:
                break
        except ValueError:
            pass
    menu(lb, ub)

if __name__ == '__main__':
    execute()