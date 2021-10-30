import numpy as np
from sty import fg, Style, RgbFg

initialUp = [
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y']
]

initialUp = np.array(initialUp)

initialLeft = [
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B']
]

initialLeft = np.array(initialLeft)

initialFront = [
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R']
]

initialFront = np.array(initialFront)

initialRight = [
    ['G', 'G', 'G'],
    ['G', 'G', 'G'],
    ['G', 'G', 'G']
]

initialRight = np.array(initialRight)

initialBack = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]

initialBack = np.array(initialBack)

initialDown = [
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W']
]

initialDown = np.array(initialDown)

up = [
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y']
]
up = np.array(up)

left = [
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B']
]

left = np.array(left)

front = [  
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R']
]

front = np.array(front)

right = [
    ['G', 'G', 'G'],
    ['G', 'G', 'G'],
    ['G', 'G', 'G']
]

right = np.array(right)

back = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]

back = np.array(back)

down = [
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W']
]

down = np.array(down)

space = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

space = np.array(space)
fg.orange = Style(RgbFg(255, 150, 50))

def Print():
    cubeT = np.concatenate((space, up, space, space), axis=1)
    cubeM = np.concatenate((left, front, right, back), axis=1)
    cubeB = np.concatenate((space, down, space, space), axis=1)
    cubeMap = np.concatenate((cubeT, cubeM, cubeB), axis=0)

    for i in range(9):
        for j in range(12):
            if (cubeMap[i][j] == 'R'):
                print(fg.red + cubeMap[i][j], end='   ' + fg.rs)
            if(cubeMap[i][j] == 'G'):
                print(fg.green + cubeMap[i][j], end='   ' + fg.rs)
            if(cubeMap[i][j] == 'Y'):
                print(fg.yellow + cubeMap[i][j], end='   ' + fg.rs)
            if(cubeMap[i][j] == 'B'):
                print(fg.blue + cubeMap[i][j], end='   ' + fg.rs)
            if(cubeMap[i][j] == 'W'):
                print(fg.white + cubeMap[i][j], end='   ' + fg.rs)
            if(cubeMap[i][j] == 'O'):
                print(fg.orange  + cubeMap[i][j], end='   ' + fg.rs)
            if(cubeMap[i][j] == ' '):
                print(cubeMap[i][j], end='   ')
        print('')

def obtainEdges():
    edges = ([front[0][1], up[2][1]], [front[1][0], left[1][2]], [front[1][2], right[1][0]], [front[2][1], down[0][1]])
    print(edges)