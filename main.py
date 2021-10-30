import numpy as np

import cube
import movements2 as move
import algorithms as al
import solver
import scrambles as sc

cube.Print()

sc.scramble2()

count = 1

while( not(np.array_equal(cube.initialUp, cube.up)
        and np.array_equal(cube.initialDown, cube.down)
        and np.array_equal(cube.initialLeft, cube.left)
        and np.array_equal(cube.initialRight, cube.right)
        and np.array_equal(cube.initialFront, cube.front)
        and np.array_equal(cube.initialBack, cube.back)
    )):
    count = count + 1
    sc.scramble2()

cube.Print()