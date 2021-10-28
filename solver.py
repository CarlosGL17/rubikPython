import cube

def obtainCenters():
    centerF, centerB, centerU, centerD, centerL, centerR = cube.front[1][1], cube.back[1][1], cube.up[1][1], cube.down[1][1], cube.left[1][1], cube.right[1][1]
    print(centerF, centerB, centerU, centerD, centerL, centerR)

def ObtainCorners():
    cornerUp1 = [cube.up[0][0], cube.left[0][0], cube.back[0][2]]
    cornerUp2 = [cube.up[0][2], cube.right[0][2], cube.back[0][0]]
    cornerUp3 = [cube.up[2][0], cube.left[0][2], cube.front[0][0]]
    cornerUp4 = [cube.up[2][2], cube.right[0][0], cube.front[0][2]]
    print(cornerUp1, cornerUp2, cornerUp3, cornerUp4)

    cornerDown1 = [cube.down[0][0], cube.left[2][2], cube.front[2][0]]
    cornerDown2 = [cube.down[0][2], cube.right[2][0], cube.front[2][2]]
    cornerDown3 = [cube.down[2][0], cube.left[2][0], cube.back[2][2]]
    cornerDown4 = [cube.down[2][2], cube.right[2][2], cube.back[2][0]]
    print(cornerDown1, cornerDown2, cornerDown3, cornerDown4)

def obtainAristas():
    arista1 = [cube.up[0][1], cube.back[0][1]]
    arista2 = [cube.up[1][0], cube.left[0][1]]
    arista3 = [cube.up[1][2], cube.right[0][1]]
    arista4 = [cube.up[2][1], cube.front[0][1]]
    print(arista1, arista2, arista3, arista4)

    arista5 = [cube.front[1][0], cube.left[1][2]]
    arista6 = [cube.front[1][2], cube.right[1][0]]
    arista7 = [cube.back[1][0], cube.right[1][2]]
    arista8 = [cube.back[1][2], cube.left[1][0]]
    print(arista5, arista6, arista7, arista8)

    arista9 = [cube.down[0][1], cube.front[2][1]]
    arista10 = [cube.down[1][0], cube.left[2][1]]
    arista11 = [cube.down[1][2], cube.right[2][1]]
    arista12 = [cube.down[2][1], cube.back[2][1]]
    print(arista9, arista10, arista11, arista12)