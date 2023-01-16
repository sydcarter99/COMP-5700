'''
Created on Oct 4, 2022

@author: sydneycarter
'''
import rubik.rotate as rotate
import rubik.cubeConstants as cubeConst
import rubik.cube as rubik

def _middleLayer(cube):
    rotation1, cube = solveFrontRightEdge(cube, cube[cubeConst.frontCenter] + cube[cubeConst.rightCenter])
    rotation2, cube = solveRightBackEdge(cube, cube[cubeConst.rightCenter] + cube[cubeConst.backCenter])
    rotation3, cube = solveBackLeftEdge(cube, cube[cubeConst.backCenter] + cube[cubeConst.leftCenter])
    rotation4, cube = solveLeftFrontEdge(cube, cube[cubeConst.leftCenter] + cube[cubeConst.frontCenter])
    rotations = rotation1 + rotation2 + rotation3 + rotation4
    return rotations, cube

def solveFrontRightEdge(cube, target):
    targetEdge = findEdge(cube, target)
    rotationsList = ['URurufUF', 'uufUFURur', 'UURurufUF', 'ufUFURur', 'uRurufUF', 'fUFURur',
                     'RurufUF', 'UfUFURur', '', 'RurufUFuRurufUF', 'BuburURUfUFURur', 'BuburURRurufUF',
                     'LulubUBuufUFURur', 'LulubUBURurufUF', 'FufulULufUFURur', 'FufulULUURurufUF']
    rotation1 = rotationsList[targetEdge]
    cube = rubik.rotateCube(cube, rotation1)
    return rotation1, cube
    
def solveRightBackEdge(cube, target):
    targetEdge = findEdge(cube, target)
    rotationsList = ['BuburUR', 'UrURUBub', 'UBuburUR', 'uurURUBub', 'UUBuburUR', 'urURUBub',
                     'uBuburUR', 'rURUBub', 'RurufUFurURUBub', 'RurufUFUUBuburUR', '', 'BuburURuBuburUR',
                     'LulubUBUrURUBub', 'LulubUBBuburUR', 'FufulULuurURUBub', 'FufulULUBuburUR']
    rotation2 = rotationsList[targetEdge]
    cube = rubik.rotateCube(cube, rotation2)
    return rotation2, cube
    
def solveBackLeftEdge(cube, target):
    targetEdge = findEdge(cube, target)
    rotationsList = ['uLulubUB', 'bUBULul', 'LulubUB', 'UbUBULul', 'ULulubUB', 'uubUBULul',
                     'UULulubUB', 'ubUBULul', 'RurufUFuubUBULul', 'RurufUFULulubUB', 'BuburURubUBULul',
                     'BuburURUULulubUB', '', 'LulubUBuLulubUB', 'FufulULUbUBULul', 'FufulULLulubUB']
    rotation3 = rotationsList[targetEdge]
    cube = rubik.rotateCube(cube, rotation3)
    return rotation3, cube
    
def solveLeftFrontEdge(cube, target):
    targetEdge = findEdge(cube, target)
    rotationsList = ['UUFufulUL', 'ulULUFuf', 'uFufulUL', 'lULUFuf', 'FufulUL', 'UlULUFuf',
                     'UFufulUL', 'uulULUFuf', 'RurufUFUlULUFuf', 'RurufUFFufulUL', 'BuburURuulULUFuf',
                     'BuburURUFufulUL', 'LulubUBulULUFuf', 'LulubUBUUFufulUL', '', 'FufulULuFufulUL']
    rotation4 = rotationsList[targetEdge]
    cube = rubik.rotateCube(cube, rotation4)
    return rotation4, cube
    
def findEdge(cube, target):
    edgePosition = {}
    # top layer positions
    edgePosition[0]  = cube[cubeConst.frontTopMiddle]    + cube[cubeConst.upperBottomMiddle]
    edgePosition[1]  = cube[cubeConst.upperBottomMiddle] + cube[cubeConst.frontTopMiddle]
    edgePosition[2]  = cube[cubeConst.rightTopMiddle]    + cube[cubeConst.upperMiddleRight]
    edgePosition[3]  = cube[cubeConst.upperMiddleRight]  + cube[cubeConst.rightTopMiddle]
    edgePosition[4]  = cube[cubeConst.backTopMiddle]     + cube[cubeConst.upperTopMiddle]
    edgePosition[5]  = cube[cubeConst.upperTopMiddle]    + cube[cubeConst.backTopMiddle]
    edgePosition[6]  = cube[cubeConst.leftTopMiddle]     + cube[cubeConst.upperMiddleLeft]
    edgePosition[7]  = cube[cubeConst.upperMiddleLeft]   + cube[cubeConst.leftTopMiddle]
    
    # middle layer positions
    edgePosition[8]  = cube[cubeConst.frontMiddleRight]  + cube[cubeConst.rightMiddleLeft]
    edgePosition[9]  = cube[cubeConst.rightMiddleLeft]   + cube[cubeConst.frontMiddleRight]
    edgePosition[10] = cube[cubeConst.rightMiddleRight]  + cube[cubeConst.backMiddleLeft]
    edgePosition[11] = cube[cubeConst.backMiddleLeft]    + cube[cubeConst.rightMiddleRight]
    edgePosition[12] = cube[cubeConst.backMiddleRight]   + cube[cubeConst.leftMiddleLeft]
    edgePosition[13] = cube[cubeConst.leftMiddleLeft]    + cube[cubeConst.backMiddleRight]
    edgePosition[14] = cube[cubeConst.leftMiddleRight]   + cube[cubeConst.frontMiddleLeft]
    edgePosition[15] = cube[cubeConst.frontMiddleLeft]   + cube[cubeConst.leftMiddleRight]
    
    for position in range(len(edgePosition)):
        if (target == edgePosition[position]):
            return position
    
    