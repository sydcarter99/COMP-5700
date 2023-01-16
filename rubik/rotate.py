import rubik.cubeConstants as cubeConst
import rubik.verify as verify

def _rotate(parms):
    """Return rotated cube""" 
    
    cube = parms.get('cube')
    direction = parms.get('dir')
    
    result = {}
    
    if(verify.isCubeValid(cube)) and (isDirValid(direction)):
        result['cube'] = rotateCube(cube, direction)
        result['status'] = 'ok'
    else:
        if not(verify.isCubeValid(cube)):
            result['status'] = 'error: invalid cube'
        if not(isDirValid(direction)):
            result['status'] = 'error: invalid direction'
    return result
    
def isDirValid(direction):
    validDirs = 'FfBbRrLlUuDd'
    #['F', 'f', 'B', 'b', 'R', 'r', 'L', 'l', 'U', 'u', 'D', 'd', '', None]
    if direction==None or direction=='':
        return True
    if all(ch in validDirs for ch in direction):
        return True
    return False

def rotateCube(cube, direction):
    #rotatedCube = cube
    if direction=='' or direction==None:
        direction = 'F'
    for x in direction:
        if(x=='F'):
            cube = rotateFrontClockwise(cube)
        if(x=='f'):
            cube = rotateFrontCounterClockwise(cube)
        if(x=='R'):
            cube = rotateRightClockwise(cube)
        if(x=='r'):
            cube = rotateRightCounterClockwise(cube)
        if(x=='B'):
            cube = rotateBackClockwise(cube)
        if(x=='b'):
            cube = rotateBackCounterClockwise(cube)
        if(x=='L'):
            cube = rotateLeftClockwise(cube)
        if(x=='l'):
            cube = rotateLeftCounterClockwise(cube)
        if(x=='U'):
            cube = rotateUpClockwise(cube)
        if(x=='u'):
            cube = rotateUpCounterClockwise(cube)
        if(x=='D'):
            cube = rotateDownClockwise(cube)
        if(x=='d'):
            cube = rotateDownCounterClockwise(cube)
    return cube
    
def rotateFrontClockwise(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    # rotate front face
    rotatedCubeList[cubeConst.frontTopRight]     = cubeList[cubeConst.frontTopLeft]
    rotatedCubeList[cubeConst.frontMiddleRight]  = cubeList[cubeConst.frontTopMiddle]
    rotatedCubeList[cubeConst.frontBottomRight]  = cubeList[cubeConst.frontTopRight]
    rotatedCubeList[cubeConst.frontTopMiddle]    = cubeList[cubeConst.frontMiddleLeft]
    rotatedCubeList[cubeConst.frontCenter]       = cubeList[cubeConst.frontCenter]
    rotatedCubeList[cubeConst.frontBottomMiddle] = cubeList[cubeConst.frontMiddleRight]
    rotatedCubeList[cubeConst.frontTopLeft]      = cubeList[cubeConst.frontBottomLeft]
    rotatedCubeList[cubeConst.frontMiddleLeft]   = cubeList[cubeConst.frontBottomMiddle]
    rotatedCubeList[cubeConst.frontBottomLeft]   = cubeList[cubeConst.frontBottomRight]
    
    #rotate top to right
    rotatedCubeList[cubeConst.rightTopLeft]      = cubeList[cubeConst.upperBottomLeft]
    rotatedCubeList[cubeConst.rightMiddleLeft]   = cubeList[cubeConst.upperBottomMiddle]
    rotatedCubeList[cubeConst.rightBottomLeft]   = cubeList[cubeConst.upperBottomRight]
    
    #rotate right to bottom
    rotatedCubeList[cubeConst.downTopRight]      = cubeList[cubeConst.rightTopLeft]
    rotatedCubeList[cubeConst.downTopMiddle]     = cubeList[cubeConst.rightMiddleLeft]
    rotatedCubeList[cubeConst.downTopLeft]       = cubeList[cubeConst.rightBottomLeft]
    
    #rotate bottom to left
    rotatedCubeList[cubeConst.leftTopRight]      = cubeList[cubeConst.downTopLeft]
    rotatedCubeList[cubeConst.leftMiddleRight]   = cubeList[cubeConst.downTopMiddle]
    rotatedCubeList[cubeConst.leftBottomRight]   = cubeList[cubeConst.downTopRight]
    
    #rotate left to top
    rotatedCubeList[cubeConst.upperBottomRight]  = cubeList[cubeConst.leftTopRight]
    rotatedCubeList[cubeConst.upperBottomMiddle] = cubeList[cubeConst.leftMiddleRight]
    rotatedCubeList[cubeConst.upperBottomLeft]   = cubeList[cubeConst.leftBottomRight]

    cube = "".join(rotatedCubeList)                
    return cube

def rotateFrontCounterClockwise(cube):
    for x in range(3):
        cube = rotateFrontClockwise(cube)
              
    return cube
    
def rotateRightClockwise(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    # rotate right face
    rotatedCubeList[cubeConst.rightTopRight]     = cubeList[cubeConst.rightTopLeft]
    rotatedCubeList[cubeConst.rightMiddleRight]  = cubeList[cubeConst.rightTopMiddle]
    rotatedCubeList[cubeConst.rightBottomRight]  = cubeList[cubeConst.rightTopRight]
    rotatedCubeList[cubeConst.rightTopMiddle]    = cubeList[cubeConst.rightMiddleLeft]
    rotatedCubeList[cubeConst.rightCenter]       = cubeList[cubeConst.rightCenter]
    rotatedCubeList[cubeConst.rightBottomMiddle] = cubeList[cubeConst.rightMiddleRight]
    rotatedCubeList[cubeConst.rightTopLeft]      = cubeList[cubeConst.rightBottomLeft]
    rotatedCubeList[cubeConst.rightMiddleLeft]   = cubeList[cubeConst.rightBottomMiddle]
    rotatedCubeList[cubeConst.rightBottomLeft]   = cubeList[cubeConst.rightBottomRight]
    
    # rotate top to right
    rotatedCubeList[cubeConst.backTopLeft]       = cubeList[cubeConst.upperBottomRight]
    rotatedCubeList[cubeConst.backMiddleLeft]    = cubeList[cubeConst.upperMiddleRight]
    rotatedCubeList[cubeConst.backBottomLeft]    = cubeList[cubeConst.upperTopRight]
    
    # rotate right to bottom
    rotatedCubeList[cubeConst.downBottomRight]   = cubeList[cubeConst.backTopLeft]
    rotatedCubeList[cubeConst.downMiddleRight]   = cubeList[cubeConst.backMiddleLeft]
    rotatedCubeList[cubeConst.downTopRight]      = cubeList[cubeConst.backBottomLeft]
    
    # rotate bottom to left
    rotatedCubeList[cubeConst.frontTopRight]     = cubeList[cubeConst.downTopRight]
    rotatedCubeList[cubeConst.frontMiddleRight]  = cubeList[cubeConst.downMiddleRight]
    rotatedCubeList[cubeConst.frontBottomRight]  = cubeList[cubeConst.downBottomRight]
    
    # rotate left to top
    rotatedCubeList[cubeConst.upperTopRight]     = cubeList[cubeConst.frontTopRight]
    rotatedCubeList[cubeConst.upperMiddleRight]  = cubeList[cubeConst.frontMiddleRight]
    rotatedCubeList[cubeConst.upperBottomRight]  = cubeList[cubeConst.frontBottomRight]

    cube = "".join(rotatedCubeList)                  
    return cube
    
def rotateRightCounterClockwise(cube):
    for x in range(3):
        cube = rotateRightClockwise(cube)
              
    return cube                  

def rotateBackClockwise(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    # rotate back face
    rotatedCubeList[cubeConst.backTopRight]      = cubeList[cubeConst.backTopLeft]
    rotatedCubeList[cubeConst.backMiddleRight]   = cubeList[cubeConst.backTopMiddle]
    rotatedCubeList[cubeConst.backBottomRight]   = cubeList[cubeConst.backTopRight]
    rotatedCubeList[cubeConst.backTopMiddle]     = cubeList[cubeConst.backMiddleLeft]
    rotatedCubeList[cubeConst.backCenter]        = cubeList[cubeConst.backCenter]
    rotatedCubeList[cubeConst.backBottomMiddle]  = cubeList[cubeConst.backMiddleRight]
    rotatedCubeList[cubeConst.backTopLeft]       = cubeList[cubeConst.backBottomLeft]
    rotatedCubeList[cubeConst.backMiddleLeft]    = cubeList[cubeConst.backBottomMiddle]
    rotatedCubeList[cubeConst.backBottomLeft]    = cubeList[cubeConst.backBottomRight]
    
    # rotate top to right
    rotatedCubeList[cubeConst.leftTopLeft]       = cubeList[cubeConst.upperTopRight]
    rotatedCubeList[cubeConst.leftMiddleLeft]    = cubeList[cubeConst.upperTopMiddle]
    rotatedCubeList[cubeConst.leftBottomLeft]    = cubeList[cubeConst.upperTopLeft]

    # rotate right to bottom
    rotatedCubeList[cubeConst.downBottomLeft]    = cubeList[cubeConst.leftTopLeft]
    rotatedCubeList[cubeConst.downBottomMiddle]  = cubeList[cubeConst.leftMiddleLeft]
    rotatedCubeList[cubeConst.downBottomRight]   = cubeList[cubeConst.leftBottomLeft]
    
    # rotate bottom to left
    rotatedCubeList[cubeConst.rightTopRight]     = cubeList[cubeConst.downBottomRight]
    rotatedCubeList[cubeConst.rightMiddleRight]  = cubeList[cubeConst.downBottomMiddle]
    rotatedCubeList[cubeConst.rightBottomRight]  = cubeList[cubeConst.downBottomLeft]
    
    # rotate left to top
    rotatedCubeList[cubeConst.upperTopLeft]      = cubeList[cubeConst.rightTopRight]
    rotatedCubeList[cubeConst.upperTopMiddle]    = cubeList[cubeConst.rightMiddleRight]
    rotatedCubeList[cubeConst.upperTopRight]     = cubeList[cubeConst.rightBottomRight]

    cube = "".join(rotatedCubeList)                    
    return cube
    
def rotateBackCounterClockwise(cube):
    for x in range(3):
        cube = rotateBackClockwise(cube)
              
    return cube
    
def rotateLeftClockwise(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    # rotate left face
    rotatedCubeList[cubeConst.leftTopRight]      = cubeList[cubeConst.leftTopLeft]
    rotatedCubeList[cubeConst.leftMiddleRight]   = cubeList[cubeConst.leftTopMiddle]
    rotatedCubeList[cubeConst.leftBottomRight]   = cubeList[cubeConst.leftTopRight]
    rotatedCubeList[cubeConst.leftTopMiddle]     = cubeList[cubeConst.leftMiddleLeft]
    rotatedCubeList[cubeConst.leftCenter]        = cubeList[cubeConst.leftCenter]
    rotatedCubeList[cubeConst.leftBottomMiddle]  = cubeList[cubeConst.leftMiddleRight]
    rotatedCubeList[cubeConst.leftTopLeft]       = cubeList[cubeConst.leftBottomLeft]
    rotatedCubeList[cubeConst.leftMiddleLeft]    = cubeList[cubeConst.leftBottomMiddle]
    rotatedCubeList[cubeConst.leftBottomLeft]    = cubeList[cubeConst.leftBottomRight]
    
    # rotate top to right
    rotatedCubeList[cubeConst.frontTopLeft]      = cubeList[cubeConst.upperTopLeft]
    rotatedCubeList[cubeConst.frontMiddleLeft]   = cubeList[cubeConst.upperMiddleLeft]
    rotatedCubeList[cubeConst.frontBottomLeft]   = cubeList[cubeConst.upperBottomLeft]
    
    # rotate right to bottom
    rotatedCubeList[cubeConst.downTopLeft]       = cubeList[cubeConst.frontTopLeft]
    rotatedCubeList[cubeConst.downMiddleLeft]    = cubeList[cubeConst.frontMiddleLeft]
    rotatedCubeList[cubeConst.downBottomLeft]    = cubeList[cubeConst.frontBottomLeft]
    
    # rotate bottom to left
    rotatedCubeList[cubeConst.backTopRight]      = cubeList[cubeConst.downBottomLeft]
    rotatedCubeList[cubeConst.backMiddleRight]   = cubeList[cubeConst.downMiddleLeft]
    rotatedCubeList[cubeConst.backBottomRight]   = cubeList[cubeConst.downTopLeft]
    
    # rotate left to top
    rotatedCubeList[cubeConst.upperBottomLeft]   = cubeList[cubeConst.backTopRight]
    rotatedCubeList[cubeConst.upperMiddleLeft]   = cubeList[cubeConst.backMiddleRight]
    rotatedCubeList[cubeConst.upperTopLeft]      = cubeList[cubeConst.backBottomRight]
    
    cube = "".join(rotatedCubeList)                   
    return cube
    
def rotateLeftCounterClockwise(cube):
    for x in range(3):
        cube = rotateLeftClockwise(cube)
              
    return cube
    
def rotateUpClockwise(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    # rotate top face
    rotatedCubeList[cubeConst.upperTopRight]     = cubeList[cubeConst.upperTopLeft]
    rotatedCubeList[cubeConst.upperMiddleRight]  = cubeList[cubeConst.upperTopMiddle]
    rotatedCubeList[cubeConst.upperBottomRight]  = cubeList[cubeConst.upperTopRight]
    rotatedCubeList[cubeConst.upperTopMiddle]    = cubeList[cubeConst.upperMiddleLeft]
    rotatedCubeList[cubeConst.upperCenter]       = cubeList[cubeConst.upperCenter]
    rotatedCubeList[cubeConst.upperBottomMiddle] = cubeList[cubeConst.upperMiddleRight]
    rotatedCubeList[cubeConst.upperTopLeft]      = cubeList[cubeConst.upperBottomLeft]
    rotatedCubeList[cubeConst.upperMiddleLeft]   = cubeList[cubeConst.upperBottomMiddle]
    rotatedCubeList[cubeConst.upperBottomLeft]   = cubeList[cubeConst.upperBottomRight]

    # rotate top to right
    rotatedCubeList[cubeConst.rightTopRight]     = cubeList[cubeConst.backTopRight]
    rotatedCubeList[cubeConst.rightTopMiddle]    = cubeList[cubeConst.backTopMiddle]
    rotatedCubeList[cubeConst.rightTopLeft]      = cubeList[cubeConst.backTopLeft]

    # rotate right to bottom
    rotatedCubeList[cubeConst.frontTopLeft]      = cubeList[cubeConst.rightTopLeft]
    rotatedCubeList[cubeConst.frontTopMiddle]    = cubeList[cubeConst.rightTopMiddle]
    rotatedCubeList[cubeConst.frontTopRight]     = cubeList[cubeConst.rightTopRight]
    
    # rotate bottom to left
    rotatedCubeList[cubeConst.leftTopLeft]       = cubeList[cubeConst.frontTopLeft]
    rotatedCubeList[cubeConst.leftTopMiddle]     = cubeList[cubeConst.frontTopMiddle]
    rotatedCubeList[cubeConst.leftTopRight]      = cubeList[cubeConst.frontTopRight]
    
    # rotate left to top
    rotatedCubeList[cubeConst.backTopLeft]       = cubeList[cubeConst.leftTopLeft]
    rotatedCubeList[cubeConst.backTopMiddle]     = cubeList[cubeConst.leftTopMiddle]
    rotatedCubeList[cubeConst.backTopRight]      = cubeList[cubeConst.leftTopRight]
    
    cube = "".join(rotatedCubeList)                  
    return cube
    
def rotateUpCounterClockwise(cube):
    for x in range(3):
        cube = rotateUpClockwise(cube)
              
    return cube
    
def rotateDownClockwise(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    # rotate bottom face
    rotatedCubeList[cubeConst.downTopRight]      = cubeList[cubeConst.downTopLeft]
    rotatedCubeList[cubeConst.downMiddleRight]   = cubeList[cubeConst.downTopMiddle]
    rotatedCubeList[cubeConst.downBottomRight]   = cubeList[cubeConst.downTopRight]
    rotatedCubeList[cubeConst.downTopMiddle]     = cubeList[cubeConst.downMiddleLeft]
    rotatedCubeList[cubeConst.downCenter]        = cubeList[cubeConst.downCenter]
    rotatedCubeList[cubeConst.downBottomMiddle]  = cubeList[cubeConst.downMiddleRight]
    rotatedCubeList[cubeConst.downTopLeft]       = cubeList[cubeConst.downBottomLeft]
    rotatedCubeList[cubeConst.downMiddleLeft]    = cubeList[cubeConst.downBottomMiddle]
    rotatedCubeList[cubeConst.downBottomLeft]    = cubeList[cubeConst.downBottomRight]
    
    # rotate top to right
    rotatedCubeList[cubeConst.rightBottomLeft]   = cubeList[cubeConst.frontBottomLeft]
    rotatedCubeList[cubeConst.rightBottomMiddle] = cubeList[cubeConst.frontBottomMiddle]
    rotatedCubeList[cubeConst.rightBottomRight]  = cubeList[cubeConst.frontBottomRight]
    
    # rotate right to bottom
    rotatedCubeList[cubeConst.backBottomLeft]    = cubeList[cubeConst.rightBottomLeft]
    rotatedCubeList[cubeConst.backBottomMiddle]  = cubeList[cubeConst.rightBottomMiddle]
    rotatedCubeList[cubeConst.backBottomRight]   = cubeList[cubeConst.rightBottomRight]
    
    # rotate bottom to left
    rotatedCubeList[cubeConst.leftBottomLeft]    = cubeList[cubeConst.backBottomLeft]
    rotatedCubeList[cubeConst.leftBottomMiddle]  = cubeList[cubeConst.backBottomMiddle]
    rotatedCubeList[cubeConst.leftBottomRight]   = cubeList[cubeConst.backBottomRight]
    
    # rotate left to top
    rotatedCubeList[cubeConst.frontBottomLeft]   = cubeList[cubeConst.leftBottomLeft]
    rotatedCubeList[cubeConst.frontBottomMiddle] = cubeList[cubeConst.leftBottomMiddle]
    rotatedCubeList[cubeConst.frontBottomRight]  = cubeList[cubeConst.leftBottomRight]
    
    cube = "".join(rotatedCubeList)                   
    return cube
    
def rotateDownCounterClockwise(cube):
    for x in range(3):
        cube = rotateDownClockwise(cube)
              
    return cube



