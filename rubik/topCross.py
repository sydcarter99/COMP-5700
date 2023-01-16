'''
Created on Oct 30, 2022

@author: sydneycarter
'''
import rubik.cubeConstants as cubeConst
import rubik.cube as rubik

def _topCross(cube):
    center = cube[cubeConst.upperCenter]
    top    = cube[cubeConst.upperTopMiddle]
    left   = cube[cubeConst.upperMiddleLeft]
    right  = cube[cubeConst.upperMiddleRight]
    bottom = cube[cubeConst.upperBottomMiddle]
    
    if (center != top) and (center != left) and (center != right) and (center != bottom):
        rotation = 'FURurURurfUUFURurf'
    elif (center == top) and (center == bottom) and (center != left) and (center != right):
        rotation = 'FURurfUUFURurf'
    elif (center == left) and (center == right) and (center != top) and (center != bottom):
        rotation = 'UFURurfUUFURurf'
    elif (center == left) and (center == top) and (center != right) and (center != bottom):
        rotation = 'FURurf'
    elif (center == top) and (center == right) and (center != bottom) and (center != left):
        rotation = 'uFURurf'
    elif (center == right) and (center == bottom) and (center != left) and (center != top):
        rotation = 'UUFURurf'
    elif (center == bottom) and (center == left) and (center != top) and (center != right):
        rotation = 'UFURurf'
    else:
        rotation = ''
        
    cube = rubik.rotateCube(cube, rotation)
    return rotation, cube
