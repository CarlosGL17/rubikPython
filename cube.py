import numpy as np
from sty import fg, rs, Style, RgbFg

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