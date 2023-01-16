import rubik.cube as rubik

def _verify(parms):
    """Determines if the provided cube is physically valid. Returns:
       {'status': 'ok'} if valid 
       {'status': 'error: xxx} if invalid"""
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    result['status'] = 'ok'                     
    return result

def isCubeValid(cube):
    validChar = 'wrgoby'
    if (cube==None) or (len(cube) != 54):
        return False
    if all(ch in validChar for ch in cube):
        f, r, b, l, u, d = cube[4], cube[13], cube[22], cube[31], cube[40], cube[49]
        if (f!=r!=b!=l!=u!=d):
            c1, c2, c3, c4, c5, c6 = cube.count('w'), cube.count('r'), cube.count('g'), cube.count('o'), cube.count('b'), cube.count('y')
            if c1==c2==c3==c4==c5==c6==9:
                return True
    return False