import cube

def U():
    cube.up = cube.up[::-1]
    cube.up = cube.up.transpose()
    temporalL = [cube.left[0][0], cube.left[0][1], cube.left[0][2]]
    temporalF = [cube.front[0][0], cube.front[0][1], cube.front[0][2]]
    temporalR = [cube.right[0][0], cube.right[0][1], cube.right[0][2]]
    temporalB = [cube.back[0][0], cube.back[0][1], cube.back[0][2]]

    temporalL, temporalF, temporalR, temporalB = temporalF, temporalR, temporalB, temporalL

    cube.left[0][0], cube.left[0][1], cube.left[0][2] = temporalL[0],temporalL[1],temporalL[2]
    cube.front[0][0], cube.front[0][1],cube.front[0][2] = temporalF[0],temporalF[1],temporalF[2]
    cube.right[0][0], cube.right[0][1], cube.right[0][2] = temporalR[0],temporalR[1],temporalR[2]
    cube.back[0][0], cube.back[0][1], cube.back[0][2] = temporalB[0],temporalB[1],temporalB[2]
    cube.Print()

def D():
    cube.down = cube.down[::-1]
    cube.down = cube.down.transpose()
    temporalF = [cube.front[2][0], cube.front[2][1], cube.front[2][2]]
    temporalR = [cube.right[2][0], cube.right[2][1], cube.right[2][2]]
    temporalB = [cube.back[2][0], cube.back[2][1], cube.back[2][2]]
    temporalL = [cube.left[2][0], cube.left[2][1], cube.left[2][2]]

    temporalF, temporalR, temporalB, temporalL = temporalL, temporalF, temporalR, temporalB

    cube.front[2][0], cube.front[2][1], cube.front[2][2] = temporalF[0], temporalF[1], temporalF[2]
    cube.right[2][0], cube.right[2][1], cube.right[2][2] = temporalR[0], temporalR[1], temporalR[2]
    cube.back[2][0], cube.back[2][1], cube.back[2][2] = temporalB[0], temporalB[1], temporalB[2]
    cube.left[2][0], cube.left[2][1], cube.left[2][2] = temporalL[0], temporalL[1], temporalL[2]
    cube.Print()

def R():
    cube.right = cube.right[::-1]
    cube.right = cube.right.transpose()
    temporalD = [cube.down[0][2],cube.down[1][2],cube.down[2][2]]
    temporalF = [cube.front[0][2],cube.front[1][2],cube.front[2][2]]
    temporalU = [cube.up[2][2],cube.up[1][2],cube.up[0][2]]
    temporalB = [cube.back[2][0],cube.back[1][0],cube.back[0][0]]

    temporalF, temporalU, temporalB, temporalD = temporalD, temporalF, temporalU, temporalB

    cube.down[0][2],cube.down[1][2],cube.down[2][2] = temporalD[0], temporalD[1], temporalD[2]
    cube.front[0][2],cube.front[1][2],cube.front[2][2] = temporalF[0], temporalF[1], temporalF[2]
    cube.up[0][2],cube.up[1][2],cube.up[2][2] = temporalU[0], temporalU[1], temporalU[2]
    cube.back[0][0],cube.back[1][0],cube.back[2][0] = temporalB[0], temporalB[1], temporalB[2]
    cube.Print()

def L():
    cube.left = cube.left[::-1]
    cube.left = cube.left.transpose()
    temporalF = [cube.front[0][0],cube.front[1][0],cube.front[2][0]]
    temporalD = [cube.down[2][0], cube.down[1][0], cube.down[0][0]]
    temporalB = [cube.back[2][2],cube.back[1][2],cube.back[0][2]]
    temporalU = [cube.up[0][0], cube.up[1][0], cube.up[2][0]]

    temporalF, temporalD, temporalB, temporalU = temporalU, temporalF, temporalD, temporalB
    cube.front[0][0],cube.front[1][0],cube.front[2][0] = temporalF[0], temporalF[1], temporalF[2]
    cube.down[0][0], cube.down[1][0],cube.down[2][0] = temporalD[0], temporalD[1], temporalD[2]
    cube.back[0][2],cube.back[1][2],cube.back[2][2] = temporalB[0], temporalB[1], temporalB[2]
    cube.up[0][0], cube.up[1][0],cube.up[2][0] = temporalU[0], temporalU[1], temporalU[2]
    cube.Print()

def F():
    cube.front = cube.front[::-1]
    cube.front = cube.front.transpose()
    temporalU = [cube.up[2][0], cube.up[2][1], cube.up[2][2]]
    temporalR = [cube.right[2][0], cube.right[1][0], cube.right[0][0]]
    temporalD = [cube.down[0][0], cube.down[0][1], cube.down[0][2]]
    temporalL = [cube.left[2][2], cube.left[1][2], cube.left[0][2]]

    temporalU, temporalR, temporalD, temporalL = temporalL, temporalU, temporalR, temporalD

    cube.down[0][0],cube.down[0][1],cube.down[0][2] = temporalD[0], temporalD[1], temporalD[2]
    cube.left[0][2],cube.left[1][2],cube.left[2][2] = temporalL[0], temporalL[1], temporalL[2]
    cube.up[2][0],cube.up[2][1],cube.up[2][2] = temporalU[0], temporalU[1], temporalU[2]
    cube.right[0][0],cube.right[1][0],cube.right[2][0] = temporalR[0], temporalR[1], temporalR[2]
    cube.Print()

def B():
    cube.back = cube.back[::-1]
    cube.back = cube.back.transpose()
    temporalU = [cube.up[0][2],cube.up[0][1],cube.up[0][0]]
    temporalR = [cube.right[0][2],cube.right[1][2],cube.right[2][2]]
    temporalD = [cube.down[2][2], cube.down[2][1], cube.down[2][0]]
    temporalL = [cube.left[0][0], cube.left[1][0], cube.left[2][0]]

    temporalU, temporalR, temporalD, temporalL = temporalR, temporalD, temporalL, temporalU

    cube.up[0][0],cube.up[0][1],cube.up[0][2] = temporalU[0], temporalU[1], temporalU[2]
    cube.right[0][2],cube.right[1][2],cube.right[2][2] = temporalR[0], temporalR[1], temporalR[2]
    cube.down[2][0], cube.down[2][1], cube.down[2][2] = temporalD[0], temporalD[1], temporalD[2]
    cube.left[0][0], cube.left[1][0], cube.left[2][0] = temporalL[0], temporalL[1], temporalL[2]
    cube.Print()

def M():
    temporalU = [cube.up[0][1],cube.up[1][1],cube.up[2][1]]
    temporalF = [cube.front[0][1], cube.front[1][1], cube.front[2][1]]
    temporalD = [cube.down[2][1], cube.down[1][1], cube.down[0][1]]
    temporalB = [cube.back[2][1], cube.back[1][1], cube.back[0][1]]

    temporalU, temporalF, temporalD, temporalB = temporalB, temporalU, temporalF, temporalD
    cube.up[0][1],cube.up[1][1],cube.up[2][1] = temporalU[0], temporalU[1], temporalU[2]
    cube.front[0][1], cube.front[1][1], cube.front[2][1] = temporalF[0], temporalF[1], temporalF[2]
    cube.down[0][1], cube.down[1][1], cube.down[2][1] = temporalD[0], temporalD[1], temporalD[2]
    cube.back[0][1], cube.back[1][1], cube.back[2][1] = temporalB[0], temporalB[1], temporalB[2]
    cube.Print()

def E():
    temporalL = [cube.left[1][0], cube.left[1][1], cube.left[1][2]]
    temporalF = [cube.front[1][0], cube.front[1][1], cube.front[1][2]]
    temporalR = [cube.right[1][0], cube.right[1][1], cube.right[1][2]]
    temporalB = [cube.back[1][0], cube.back[1][1], cube.back[1][2]]

    temporalF, temporalR, temporalB, temporalL = temporalL, temporalF, temporalR, temporalB
    cube.left[1][0], cube.left[1][1], cube.left[1][2] = temporalL[0], temporalL[1], temporalL[2]
    cube.front[1][0], cube.front[1][1], cube.front[1][2] = temporalF[0], temporalF[1], temporalF[2]
    cube.right[1][0], cube.right[1][1], cube.right[1][2] = temporalR[0], temporalR[1], temporalR[2]
    cube.back[1][0], cube.back[1][1], cube.back[1][2] = temporalB[0], temporalB[1], temporalB[2]
    cube.Print()

def S():
    temporalU = [cube.up[1][0], cube.up[1][1], cube.up[1][2]]
    temporalR = [cube.right[2][1], cube.right[1][1], cube.right[0][1]]
    temporalD = [cube.down[1][0], cube.down[1][1], cube.down[1][2]]
    temporalL = [cube.left[2][1], cube.left[1][1], cube.left[0][1]]

    temporalU, temporalR, temporalD, temporalL = temporalL, temporalU, temporalR, temporalD
    cube.up[1][0], cube.up[1][1], cube.up[1][2] = temporalU[0], temporalU[1], temporalU[2]
    cube.right[0][1], cube.right[1][1], cube.right[2][1] = temporalR[0], temporalR[1], temporalR[2]
    cube.down[1][0], cube.down[1][1], cube.down[1][2] = temporalD[0], temporalD[1], temporalD[2]
    cube.left[0][1], cube.left[1][1], cube.left[2][1] = temporalL[0], temporalL[1], temporalL[2]
    cube.Print()

def u():
    for i in range(3):
        U()

def d():
    for i in range(3):
        D()

def f():
    for i in range(3):
        F()

def b():
    for i in range(3):
        B()

def r():
    for i in range(3):
        R()

def l():
    for i in range(3):
        L()

def s():
    for i in range(3):
        S()

def e():
    for i in range(3):
        E()

def m():
    for i in range(3):
        M()

def R2():
    for i in range(2):
        R()

def L2():
    for i in range(2):
        L()

def F2():
    for i in range(2):
        F()

def B2():
    for i in range(2):
        B()

def U2():
    for i in range(2):
        U()

def D2():
    for i in range(2):
        D()

def E2():
    for i in range(2):
        E()

def S2():
    for i in range(2):
        S()

def M2():
    for i in range(2):
        M()

def rotateDownToFront():
    R()
    m()
    l()

def rotateUpToFront():
    r()
    M()
    L()

def rotateRightToFront():
    U()
    e()
    d()

def rotateLeftToFront():
    u()
    E()
    D()