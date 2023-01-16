import unittest
import rubik.solve as solve
import rubik.rotate as rotate

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test000_solves_fully_solved_cube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'
        expectedResult['rotations'] = ''
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test010_solves_cube_with_bottom_face_solved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yyrbbbbbbgbyrrrrrrggbggggggrybooooooyyoryyooywwwwwwwww'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'
        expectedResult['rotations'] = ''
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test020_solves_front_right_corner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yyoyorooowgobbygbbbgrororrrybgbgggggbryyyorrbwwywwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test030_solves_back_right_corner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ybgbgggggyyoyorooowgobbygbbbgrororrryobryrbyrwwwwwwwwy'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test040_solves_back_left_corner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bgrororrrybgbgggggyyoyorooowgobbygbbbrroyyyrbwwwwwwyww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test050_solves_front_left_corner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wgobbygbbbgrororrrybgbgggggyyoyorooorybryrboyywwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test060_solves_two_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'woorrgwrryyroggggggrbyobooorgbybbybbyyyryorbgowwwwwbww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test070_solves_three_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wgrbrogrbworyggyggbbyyobooogroyboybyorwyygbrgrwrwwwbww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test080_solves_all_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ryybrygrbgooggrrgogryyogyobbggrbowbyrbwoyywborwwwwwowb'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
    
    def test090_solves_entire_bottom_layer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'brwybbywogoywrwgoyrywggrbrgbwryogoobobgrybwbrroygwywgo'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test100_solves_entire_bottom_layer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ggrbgbwgowobyoyyrbwrgobrygoyboyrwgrbrbroywwygoobwwgywr'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 3
        expectedResult['right']  = (inputDict.get('cube')[13]) * 3
        expectedResult['back']   = (inputDict.get('cube')[22]) * 3
        expectedResult['left']   = (inputDict.get('cube')[31]) * 3
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[6:9]
        actualResult['right']  = cube[15:18]
        actualResult['back']   = cube[24:27]
        actualResult['left']   = cube[33:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test900_missing_cube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test910_invalid_cube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbyyyyyyyyyrrrrrrrrr666666666'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))


