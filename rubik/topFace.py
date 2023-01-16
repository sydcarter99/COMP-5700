'''
Created on Oct 30, 2022

@author: sydneycarter
'''
import rubik.cubeConstants as cubeConst
import rubik.cube as rubik

def _topFace(cube):
    center = cube[cubeConst.upperCenter]
    
    cornerCount = 0
    if (center == cube[cubeConst.upperTopLeft]):
        cornerCount += 1
    if (center == cube[cubeConst.upperTopRight]):
        cornerCount += 1
    if (center == cube[cubeConst.upperBottomLeft]):
        cornerCount += 1
    if (center == cube[cubeConst.upperBottomRight]):
        cornerCount += 1
        
    if cornerCount == 0:
        rotation, cube = noCorners(cube, center)
    elif cornerCount == 1:
        rotation, cube = oneCorner(cube, center)
    elif cornerCount == 2:
        rotation, cube = twoCorners(cube, center)
    else:
        rotation = ''
        
    return rotation, cube
        
def noCorners(cube, center):
    if (cube[cubeConst.frontTopLeft] == cube[cubeConst.frontTopRight] == cube[cubeConst.backTopLeft] == cube[cubeConst.backTopRight] == center):
        rotation = 'FRUruRUruRUruf'
    elif (cube[cubeConst.rightTopLeft] == cube[cubeConst.rightTopRight] == cube[cubeConst.leftTopLeft] == cube[cubeConst.leftTopRight] == center):
        rotation = 'UFRUruRUruRUruf'
    else:
        if (cube[cubeConst.leftTopRight] == cube[cubeConst.leftTopLeft] == center):
            rotation = 'RUURRuRRuRRUUR'
        elif (cube[cubeConst.frontTopLeft] == cube[cubeConst.frontTopRight] == center):
            rotation = 'URUURRuRRuRRUUR'
        elif (cube[cubeConst.rightTopLeft] == cube[cubeConst.rightTopRight] == center):
            rotation = 'UURUURRuRRuRRUUR'
        else:
            rotation = 'uRUURRuRRuRRUUR'
    
    cube = rubik.rotateCube(cube, rotation)
    return rotation, cube
    
def oneCorner(cube, center):
    if (center == cube[cubeConst.upperBottomLeft]) and (center == cube[cubeConst.frontTopRight]):
        rotation = 'RUrURUUr'
    elif (center == cube[cubeConst.upperBottomRight]) and (center == cube[cubeConst.rightTopRight]):
        rotation = 'URUrURUUr'
    elif (center == cube[cubeConst.upperTopRight]) and (center == cube[cubeConst.backTopRight]):
        rotation = 'UURUrURUUr'
    elif (center == cube[cubeConst.upperTopLeft]) and (center == cube[cubeConst.leftTopRight]):
        rotation = 'uRUrURUUr'
    elif (center == cube[cubeConst.upperBottomRight]) and (center == cube[cubeConst.frontTopLeft]):
        rotation = 'luLulUUL'
    elif (center == cube[cubeConst.upperTopRight]) and (center == cube[cubeConst.rightTopLeft]):
        rotation = 'UluLulUUL'
    elif (center == cube[cubeConst.upperTopLeft]) and (center == cube[cubeConst.backTopLeft]):
        rotation = 'UUluLulUUL'
    elif (center == cube[cubeConst.upperBottomLeft]) and (center == cube[cubeConst.leftTopLeft]):
        rotation = 'uluLulUUL'
        
    cube = rubik.rotateCube(cube, rotation)
    return rotation, cube
    
def twoCorners(cube, center):
    if (center == cube[cubeConst.frontTopLeft] == cube[cubeConst.frontTopRight]):
        rotation = 'rrDrUURdrUUr'
    elif (center == cube[cubeConst.rightTopLeft] == cube[cubeConst.rightTopRight]):
        rotation = 'UrrDrUURdrUUr'
    elif (center == cube[cubeConst.backTopLeft] == cube[cubeConst.backTopRight]):
        rotation = 'UUrrDrUURdrUUr'
    elif (center == cube[cubeConst.leftTopLeft] == cube[cubeConst.leftTopRight]):
        rotation = 'urrDrUURdrUUr'
    elif (center == cube[cubeConst.leftTopLeft] == cube[cubeConst.rightTopRight]):
        rotation = 'RUUruRurrUURUrUR'
    elif (center == cube[cubeConst.backTopRight] == cube[cubeConst.frontTopLeft]):
        rotation = 'URUUruRurrUURUrUR'
    elif (center == cube[cubeConst.leftTopRight] == cube[cubeConst.rightTopLeft]):
        rotation = 'UURUUruRurrUURUrUR'
    elif (center == cube[cubeConst.frontTopRight] == cube[cubeConst.backTopLeft]):
        rotation = 'uRUUruRurrUURUrUR'
    elif (center == cube[cubeConst.frontTopLeft] == cube[cubeConst.rightTopRight]):
        rotation = 'lRUruLURur'
    elif (center == cube[cubeConst.rightTopLeft] == cube[cubeConst.backTopRight]):
        rotation = 'UlRUruLURur'
    elif (center == cube[cubeConst.backTopLeft] == cube[cubeConst.leftTopRight]):
        rotation = 'UUlRUruLURur'
    else:
        rotation = 'ulRUruLURur'
    
    cube = rubik.rotateCube(cube, rotation)
    return rotation, cube
    
    