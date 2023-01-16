'''
Created on Nov 14, 2022

@author: sydneycarter
'''
import rubik.cubeConstants as cubeConst
import rubik.cube as rubik

def _permutateCorners(cube):
    cornerCount = 0
    if ((cube[cubeConst.frontTopRight] + cube[cubeConst.rightTopLeft]) == (cube[cubeConst.frontCenter] + cube[cubeConst.rightCenter])):
        cornerCount += 1
    if ((cube[cubeConst.rightTopRight] + cube[cubeConst.backTopLeft]) == (cube[cubeConst.rightCenter] + cube[cubeConst.backCenter])):
        cornerCount += 1
    if ((cube[cubeConst.backTopRight] + cube[cubeConst.leftTopLeft]) == (cube[cubeConst.backCenter] + cube[cubeConst.leftCenter])):
        cornerCount += 1
    if ((cube[cubeConst.leftTopRight] + cube[cubeConst.frontTopLeft]) == (cube[cubeConst.leftCenter] + cube[cubeConst.frontCenter])):
        cornerCount += 1
        
    if (cornerCount == 0):
        rotation = solveNoCorners(cube)
    elif (cornerCount == 1):
        rotation = solveOneCorner(cube)
    elif (cornerCount == 2):
        rotation = solveTwoCorners(cube)
    else:
        rotation = ''
    
    cube = rubik.rotateCube(cube, rotation)
    return rotation, cube

def solveNoCorners(cube):
    frontRightTarget = cube[cubeConst.frontCenter] + cube[cubeConst.rightCenter]
    rightBackTarget  = cube[cubeConst.rightCenter] + cube[cubeConst.backCenter]
    backLeftTarget   = cube[cubeConst.backCenter]  + cube[cubeConst.leftCenter]
    leftFrontTarget  = cube[cubeConst.leftCenter]  + cube[cubeConst.frontCenter]
    
    frontRightActual = cube[cubeConst.frontTopRight] + cube[cubeConst.rightTopLeft]
    rightBackActual  = cube[cubeConst.rightTopRight] + cube[cubeConst.backTopLeft]
    backLeftActual   = cube[cubeConst.backTopRight] + cube[cubeConst.leftTopLeft]
    leftFrontActual  = cube[cubeConst.leftTopRight] + cube[cubeConst.frontTopLeft]
    
    if (backLeftActual == leftFrontTarget) and (leftFrontActual == backLeftTarget):
        rotation = 'uFRuruRUrfRUrurFRf'
    elif (backLeftActual == rightBackTarget) and (rightBackActual == backLeftTarget):
        rotation = 'UFRuruRUrfRUrurFRf'
    elif (frontRightActual == backLeftTarget) and (backLeftActual == frontRightTarget):
        rotation = 'UU'
    elif (frontRightActual == leftFrontTarget) and (rightBackActual == frontRightTarget):
        rotation = 'U'
    elif (frontRightActual == rightBackTarget) and (rightBackActual == backLeftTarget):
        rotation = 'u'
    else:
        rotation = 'UU' + solveTwoCorners(rubik.rotateCube(cube, 'UU'))
    return rotation

def solveOneCorner(cube):
    if ((cube[cubeConst.backTopRight] + cube[cubeConst.leftTopLeft]) == (cube[cubeConst.backCenter]  + cube[cubeConst.leftCenter])):
        if ((cube[cubeConst.leftTopRight] + cube[cubeConst.frontTopLeft]) == (cube[cubeConst.rightCenter] + cube[cubeConst.backCenter])):
            rotation = 'UURUrurFRRuruRUrfu'
        else:
            rotation = 'URUrurFRRuruRUrfUU'
    elif ((cube[cubeConst.leftTopRight] + cube[cubeConst.frontTopLeft]) == (cube[cubeConst.leftCenter]  + cube[cubeConst.frontCenter])):
        if ((cube[cubeConst.frontTopRight] + cube[cubeConst.rightTopLeft]) == (cube[cubeConst.backCenter]  + cube[cubeConst.leftCenter])):
            rotation = 'uRUrurFRRuruRUrfUU'
        else:
            rotation = 'uuRUrurFRRuruRUrfU'
    elif ((cube[cubeConst.frontTopRight] + cube[cubeConst.rightTopLeft]) == (cube[cubeConst.frontCenter] + cube[cubeConst.rightCenter])):
        if ((cube[cubeConst.rightTopRight] + cube[cubeConst.backTopLeft]) == (cube[cubeConst.leftCenter]  + cube[cubeConst.frontCenter])):
            rotation = 'RUrurFRRuruRUrfU'
        else:
            rotation = 'uRUrurFRRuruRUrf'
    else:
        if ((cube[cubeConst.backTopRight] + cube[cubeConst.leftTopLeft]) == (cube[cubeConst.frontCenter] + cube[cubeConst.rightCenter])):
            rotation = 'URUrurFRRuruRUrf'
        else:
            rotation = 'RUrurFRRuruRUrfu'
    return rotation

def solveTwoCorners(cube):
    if (cube[cubeConst.rightTopLeft] == cube[cubeConst.rightTopRight]):
        rotation = 'UURUrurFRRuruRUrfUU'
    elif (cube[cubeConst.backTopLeft] == cube[cubeConst.backTopRight]):
        rotation = 'uRUrurFRRuruRUrfU'
    elif (cube[cubeConst.leftTopLeft] == cube[cubeConst.leftTopRight]):
        rotation = 'RUrurFRRuruRUrf'
    elif (cube[cubeConst.frontTopLeft] == cube[cubeConst.frontTopRight]):
        rotation = 'URUrurFRRuruRUrfu'
    elif (cube[cubeConst.frontTopLeft] == cube[cubeConst.frontCenter]):
        rotation = 'FRuruRUrfRUrurFRf'
    else:
        rotation = 'UFRuruRUrfRUrurFRfu'
    return rotation








