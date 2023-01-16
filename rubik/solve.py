import hashlib
import random
import rubik.verify as verify
import rubik.downFaceCross as dfc
import rubik.bottomCorners as bc
import rubik.middleLayer as ml
import rubik.topCross as tc
import rubik.topFace as tf
import rubik.permutateCorners as pc
import rubik.permutateEdges as pe

def _solve(parms):
    """Return rotates needed to solve input cube"""

    cube = parms.get('cube')
    result = {}
    
    cubeToTokenize = cube
    
    if not(verify.isCubeValid(cube)):
        result['status'] = 'error: invalid cube'
    else:
        dfcRotations, cube = dfc._downFaceCross(cube)
        bcRotations,  cube = bc._bottomCorners(cube)
        mlRotations,  cube = ml._middleLayer(cube)
        tcRotations,  cube = tc._topCross(cube)
        tfRotations,  cube = tf._topFace(cube)
        pcRotations,  cube = pc._permutateCorners(cube)
        peRotations,  cube = pe._permutateEdges(cube)

        result['rotations'] = dfcRotations + bcRotations + mlRotations + tcRotations + tfRotations + pcRotations + peRotations
        result['status'] = 'ok'
        
        itemToTokenize = cubeToTokenize + result['rotations']
        sha256Hash = hashlib.sha256()
        sha256Hash.update(itemToTokenize.encode())
        fullToken = sha256Hash.hexdigest()
        index = random.randint(0, len(fullToken) - 8)
        tokenSubstring = fullToken[index:index+8]
        
        result['token'] = tokenSubstring

    return result






