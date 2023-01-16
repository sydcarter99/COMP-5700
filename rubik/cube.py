import rubik.rotate as rotate

def rotateCube(cube, rotation):
    newCube = {}
    newCube['cube'] = cube
    newCube['dir'] = rotation
    if (rotation != ''):
        cube = rotate._rotate(newCube).get('cube')
    return cube

