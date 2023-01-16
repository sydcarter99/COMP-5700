import rubik.rotate as rotate
import rubik.cubeConstants as cubeConst
import rubik.cube as rubik

def _bottomCorners(cube):
    rotation1, cube = solveFrontRightCorner(cube, cube[cubeConst.downCenter] + cube[cubeConst.frontCenter] + cube[cubeConst.rightCenter])
    rotation2, cube = solveBackRightCorner( cube, cube[cubeConst.downCenter] + cube[cubeConst.rightCenter] + cube[cubeConst.backCenter] )
    rotation3, cube = solveBackLeftCorner(  cube, cube[cubeConst.downCenter] + cube[cubeConst.backCenter]  + cube[cubeConst.leftCenter] )
    rotation4, cube = solveFrontLeftCorner( cube, cube[cubeConst.downCenter] + cube[cubeConst.leftCenter]  + cube[cubeConst.frontCenter])
    
    rotations = rotation1 + rotation2 + rotation3 + rotation4
    return rotations, cube

def solveFrontRightCorner(cube, target):
    targetCorner = findCorner(cube, target)
    rotationsList = ['fuF', 'RUr', 'RUUruRUr', 'uRUUr', 'URUr', 'URUUruRUr', 'RUUr', 'UURUr',
                     'UURUUruRUr', 'Rur', 'uRUr', 'uRUUruRUr', 'RurfuF', 'fUFRUr', '', 'rUURRur',
                     'BUbRUr', 'ruRfUUF', 'buBRur', 'LUlURUr', 'buBuRUr', 'luLURur', 'lULuRUr', 'lULRur']
    rotation1 = rotationsList[targetCorner]
    cube = rubik.rotateCube(cube, rotation1)
    return rotation1, cube

def solveBackRightCorner(cube, target):
    targetCorner = findCorner(cube, target)
    rotationsList = ['Bub', 'uBUb', 'uBUUbuBUb', 'ruR', 'BUb', 'BUUbuBUb', 'uBUUb', 'UBUb',
                     'UBUUbuBUb', 'BUUb', 'UUBUb', 'UUBUUbuBUb', 'fuFUBub', 'fUFuBUb', 'fUFBub', 'BubruR',
                     'rURBUb', '', 'bUUBBub', 'LUlBUb', 'buBrUUR', 'luLBub', 'FUfUBUb', 'luLuBUb']
    rotation2 = rotationsList[targetCorner]
    cube = rubik.rotateCube(cube, rotation2)
    return rotation2, cube

def solveBackLeftCorner(cube, target):
    targetCorner = findCorner(cube, target)
    rotationsList = ['LUUl', 'UULUl', 'UULUUluLUl', 'Lul', 'uLUl', 'uLUUluLUl', 'buB', 'LUl',
                     'LUUluLUl', 'uLUUl', 'ULUl', 'ULUUluLUl', 'fuFLul', 'RUrULUl', 'fuFuLUl', 'ruRULul',
                     'rURuLUl', 'rURLul', 'LulbuB', 'bUBLUl', '', 'lUULLul', 'FUfLUl', 'luLbUUB']
    rotation3 = rotationsList[targetCorner]
    cube = rubik.rotateCube(cube, rotation3)
    return rotation3, cube

def solveFrontLeftCorner(cube, target):
    targetCorner = findCorner(cube, target)
    rotationsList = ['uFUUf', 'UFUf', 'UFUUfuFUf', 'FUUf', 'UUFUf', 'UUFUUfuFUf', 'Fuf', 'uFUf',
                     'uFUUfuFUf', 'luL', 'FUf', 'FUUfuFUf', 'fUUFFUf', 'RUrFUf', 'fuFlUUL', 'ruRFuf',
                     'BUbUFUf', 'ruRuFUf', 'buBUFuf', 'bUBuFUf', 'bUBFuf', 'FufluL', 'lULFUf', '']
    rotation4 = rotationsList[targetCorner]
    cube = rubik.rotateCube(cube, rotation4)
    return rotation4, cube

def findCorner(cube, target):
    cornerPos = {}
    # top front right orientations
    cornerPos[0]  = cube[cubeConst.frontTopRight]    + cube[cubeConst.upperBottomRight] + cube[cubeConst.rightTopLeft]
    cornerPos[1]  = cube[cubeConst.rightTopLeft]     + cube[cubeConst.frontTopRight]    + cube[cubeConst.upperBottomRight]
    cornerPos[2]  = cube[cubeConst.upperBottomRight] + cube[cubeConst.rightTopLeft]     + cube[cubeConst.frontTopRight]
    # top back right orientations
    cornerPos[3]  = cube[cubeConst.rightTopRight]    + cube[cubeConst.upperTopRight]    + cube[cubeConst.backTopLeft]
    cornerPos[4]  = cube[cubeConst.backTopLeft]      + cube[cubeConst.rightTopRight]    + cube[cubeConst.upperTopRight]
    cornerPos[5]  = cube[cubeConst.upperTopRight]    + cube[cubeConst.backTopLeft]      + cube[cubeConst.rightTopRight]
    # top back left orientations
    cornerPos[6]  = cube[cubeConst.backTopRight]     + cube[cubeConst.upperTopLeft]     + cube[cubeConst.leftTopLeft]
    cornerPos[7]  = cube[cubeConst.leftTopLeft]      + cube[cubeConst.backTopRight]     + cube[cubeConst.upperTopLeft]
    cornerPos[8]  = cube[cubeConst.upperTopLeft]     + cube[cubeConst.leftTopLeft]      + cube[cubeConst.backTopRight]
    # top front left orientations
    cornerPos[9]  = cube[cubeConst.leftTopRight]     + cube[cubeConst.upperBottomLeft]  + cube[cubeConst.frontTopLeft]
    cornerPos[10] = cube[cubeConst.frontTopLeft]     + cube[cubeConst.leftTopRight]     + cube[cubeConst.upperBottomLeft]
    cornerPos[11] = cube[cubeConst.upperBottomLeft]  + cube[cubeConst.frontTopLeft]     + cube[cubeConst.leftTopRight]
    
    # bottom front right orientations
    cornerPos[12] = cube[cubeConst.frontBottomRight] + cube[cubeConst.rightBottomLeft]  + cube[cubeConst.downTopRight]
    cornerPos[13] = cube[cubeConst.rightBottomLeft]  + cube[cubeConst.downTopRight]     + cube[cubeConst.frontBottomRight]
    cornerPos[14] = cube[cubeConst.downTopRight]     + cube[cubeConst.frontBottomRight] + cube[cubeConst.rightBottomLeft]
    # bottom back right orientations
    cornerPos[15] = cube[cubeConst.rightBottomRight] + cube[cubeConst.backBottomLeft]   + cube[cubeConst.downBottomRight]
    cornerPos[16] = cube[cubeConst.backBottomLeft]   + cube[cubeConst.downBottomRight]  + cube[cubeConst.rightBottomRight]
    cornerPos[17] = cube[cubeConst.downBottomRight]  + cube[cubeConst.rightBottomRight] + cube[cubeConst.backBottomLeft]
    # bottom back left orientations
    cornerPos[18] = cube[cubeConst.backBottomRight]  + cube[cubeConst.leftBottomLeft]   + cube[cubeConst.downBottomLeft]
    cornerPos[19] = cube[cubeConst.leftBottomLeft]   + cube[cubeConst.downBottomLeft]   + cube[cubeConst.backBottomRight]
    cornerPos[20] = cube[cubeConst.downBottomLeft]   + cube[cubeConst.backBottomRight]  + cube[cubeConst.leftBottomLeft]
    # bottom front left orientations
    cornerPos[21] = cube[cubeConst.leftBottomRight]  + cube[cubeConst.frontBottomLeft]  + cube[cubeConst.downTopLeft]
    cornerPos[22] = cube[cubeConst.frontBottomLeft]  + cube[cubeConst.downTopLeft]      + cube[cubeConst.leftBottomRight]
    cornerPos[23] = cube[cubeConst.downTopLeft]      + cube[cubeConst.leftBottomRight]  + cube[cubeConst.frontBottomLeft]
    
    for position in range(len(cornerPos)):
        if (target == cornerPos[position]):
            return position


