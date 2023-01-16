'''
Created on Nov 14, 2022

@author: sydneycarter
'''
import rubik.cubeConstants as cubeConst
import rubik.cube as rubik

def _permutateEdges(cube):
    edgeCount = 0
    if (cube[cubeConst.frontCenter] == cube[cubeConst.frontTopMiddle]):
        edgeCount += 1
    if (cube[cubeConst.rightCenter] == cube[cubeConst.rightTopMiddle]):
        edgeCount += 1
    if (cube[cubeConst.backCenter] == cube[cubeConst.backTopMiddle]):
        edgeCount += 1
    if (cube[cubeConst.leftCenter] == cube[cubeConst.leftTopMiddle]):
        edgeCount += 1
    
    
    if (edgeCount == 0):
        rotation = solveNoEdges(cube)
    elif (edgeCount == 1):
        rotation = solveOneEdge(cube)
    else:
        rotation = ''
        
    cube = rubik.rotateCube(cube, rotation)
    return rotation, cube

def solveNoEdges(cube):
    if (cube[cubeConst.frontTopMiddle] == cube[cubeConst.backCenter]):
        rotation = 'RRURUrururUruRRURUrururUrU'
    elif (cube[cubeConst.frontTopMiddle] == cube[cubeConst.rightCenter]):
        rotation = 'RRURUrururUrUURuRURURuruRRUU'
    else:
        rotation = 'RRURUrururUrURRURUrururUru'
    return rotation

def solveOneEdge(cube):
    if (cube[cubeConst.backCenter] == cube[cubeConst.backTopMiddle]):
        if (cube[cubeConst.rightTopMiddle] == cube[cubeConst.leftCenter]):
            rotation = 'RuRURURuruRR'
        else:
            rotation = 'RRURUrururUr'
    elif (cube[cubeConst.leftCenter] == cube[cubeConst.leftTopMiddle]):
        if (cube[cubeConst.backTopMiddle] == cube[cubeConst.frontCenter]):
            rotation = 'URuRURURuruRRu'
        else:
            rotation = 'URRURUrururUru'
    elif (cube[cubeConst.frontCenter] == cube[cubeConst.frontTopMiddle]):
        if (cube[cubeConst.leftTopMiddle] == cube[cubeConst.rightCenter]):
            rotation = 'UURuRURURuruRRUU'
        else:
            rotation = 'UURRURUrururUrUU'
    else:
        if (cube[cubeConst.frontTopMiddle] == cube[cubeConst.backCenter]):
            rotation = 'uRuRURURuruRRU'
        else:
            rotation = 'uRRURUrururUrU'
            
    return rotation
            
            
        
    