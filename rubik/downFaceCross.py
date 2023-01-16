import rubik.cubeConstants as cubeConst
import rubik.cube as rubik

def _downFaceCross(cube):
    rotation1, cube = solveDownFrontEdge(cube, cube[cubeConst.downCenter]+cube[cubeConst.frontCenter])
    rotation2, cube = solveDownRightEdge(cube, cube[cubeConst.downCenter]+cube[cubeConst.rightCenter])
    rotation3, cube = solveDownBackEdge( cube, cube[cubeConst.downCenter]+cube[cubeConst.backCenter])
    rotation4, cube = solveDownLeftEdge( cube, cube[cubeConst.downCenter]+cube[cubeConst.leftCenter])
    
    rotations = rotation1 + rotation2 + rotation3 + rotation4

    return rotations, cube

def solveDownFrontEdge(cube, target):
    targetEdge = findEdge(cube, target)
    rotationsList = ['fdLD', 'FF',   'Drd',  'F',    'DRdF', '',      'dLD',  'f',      'rFR', 'UFF', 'RRFRR', 'DRd',
                     'RF',   'RDrd', 'UrFR', 'UUFF', 'dlD',  'llfll', 'dRDF', 'ddFddf', 'Lfl', 'uff', 'lf',    'ldLD']
    rotation1 = rotationsList[targetEdge]
    cube = rubik.rotateCube(cube, rotation1)
    return rotation1, cube
        
def solveDownRightEdge(cube, target):
    targetEdge = findEdge(cube, target)
    rotationsList = ['Frf',  'urr', 'r',     'dFD', 'fr' ,   'fdFD', 'ddLdd', 'dfD',  'rdFD', 'rr',   'Dbd',  'R',
                     'RdFD', '',    'UrdFD', 'Urr', 'ddldd', 'DBd',  'BR',    'BDbd', 'uFrf', 'uurr', 'ldfD', 'FbddBf']
    rotation2 = rotationsList[targetEdge]
    cube = rubik.rotateCube(cube, rotation2)
    return rotation2, cube
    
def solveDownBackEdge(cube, target):
    targetEdge = findEdge(cube, target)
    rotationsList = ['UlBL', 'UUBB', 'drD',  'ddFdd', 'FDLd', 'fddFdd', 'DLd',  'ddfdd', 'dRDb', 'drrD', 'b',  'dRD',
                     'rb',   'RdrD', 'bdRD', 'bb',    'Dld',  'B',      'drDb', '',      'DldB', 'Ubb',  'LB', 'lDLd']
    rotation3 = rotationsList[targetEdge]
    cube = rubik.rotateCube(cube, rotation3)
    return rotation3, cube
    
def solveDownLeftEdge(cube, target):
    targetEdge = findEdge(cube, target)
    rotationsList = ['DfdL',   'Ull',    'ddrdd', 'DFd', 'FL', 'fDFd', 'L',  'Dfd',  'UULDfd', 'UULL', 'dbD',  'ddRdd',
                     'rfbDBF', 'RFFLFF', 'UUfLF', 'uLL', 'l',  'dBD',  'bl', 'bdBD', 'LDfd',   'll',   'lDfd', '']
    rotation4 = rotationsList[targetEdge]
    cube = rubik.rotateCube(cube, rotation4)
    return rotation4, cube
    
def findEdge(cube, target):
    edgePos = {}
    edgePos[0]  = cube[cubeConst.frontTopMiddle]    + cube[cubeConst.upperBottomMiddle]
    edgePos[1]  = cube[cubeConst.upperBottomMiddle] + cube[cubeConst.frontTopMiddle]
    edgePos[2]  = cube[cubeConst.frontMiddleRight]  + cube[cubeConst.rightMiddleLeft]
    edgePos[3]  = cube[cubeConst.rightMiddleLeft]   + cube[cubeConst.frontMiddleRight]
    edgePos[4]  = cube[cubeConst.frontBottomMiddle] + cube[cubeConst.downTopMiddle]
    edgePos[5]  = cube[cubeConst.downTopMiddle]     + cube[cubeConst.frontBottomMiddle]
    edgePos[6]  = cube[cubeConst.frontMiddleLeft]   + cube[cubeConst.leftMiddleRight]
    edgePos[7]  = cube[cubeConst.leftMiddleRight]   + cube[cubeConst.frontMiddleLeft]
    edgePos[8]  = cube[cubeConst.rightTopMiddle]    + cube[cubeConst.upperMiddleRight]
    edgePos[9]  = cube[cubeConst.upperMiddleRight]  + cube[cubeConst.rightTopMiddle]
    edgePos[10] = cube[cubeConst.rightMiddleRight]  + cube[cubeConst.backMiddleLeft]
    edgePos[11] = cube[cubeConst.backMiddleLeft]    + cube[cubeConst.rightMiddleRight]
    edgePos[12] = cube[cubeConst.rightBottomMiddle] + cube[cubeConst.downMiddleRight]
    edgePos[13] = cube[cubeConst.downMiddleRight]   + cube[cubeConst.rightBottomMiddle]
    edgePos[14] = cube[cubeConst.backTopMiddle]     + cube[cubeConst.upperTopMiddle]
    edgePos[15] = cube[cubeConst.upperTopMiddle]    + cube[cubeConst.backTopMiddle]
    edgePos[16] = cube[cubeConst.backMiddleRight]   + cube[cubeConst.leftMiddleLeft]
    edgePos[17] = cube[cubeConst.leftMiddleLeft]    + cube[cubeConst.backMiddleRight]
    edgePos[18] = cube[cubeConst.backBottomMiddle]  + cube[cubeConst.downBottomMiddle]
    edgePos[19] = cube[cubeConst.downBottomMiddle]  + cube[cubeConst.backBottomMiddle]
    edgePos[20] = cube[cubeConst.leftTopMiddle]     + cube[cubeConst.upperMiddleLeft]
    edgePos[21] = cube[cubeConst.upperMiddleLeft]   + cube[cubeConst.leftTopMiddle]
    edgePos[22] = cube[cubeConst.leftBottomMiddle]  + cube[cubeConst.downMiddleLeft]
    edgePos[23] = cube[cubeConst.downMiddleLeft]    + cube[cubeConst.leftBottomMiddle]
    
    for position in range(len(edgePos)):
        if (target == edgePos[position]):
            return position


