'''
Created on Nov 14, 2022

@author: sydneycarter
'''
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
        
    def test010_solves_diagonal_corner_swap(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'obroooooogrbbbbbbbrgorrrrrrbogggggggyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test020_solves_adjacent_corner_swap(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'brrbbbbbbgbbrrrrrrrggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test030_solves_double_diagonal_corner_swap(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ororrrrrrbbbggggggrgroooooogogbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test040_solves_double_adjacent_corner_swap(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'grboooooorbobbbbbbbggrrrrrroorggggggyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test050_solves_three_wrong_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bggggggggooboooooorbrbbbbbbgrorrrrrryyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test060_solves_three_wrong_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bggbbbbbboobrrrrrrrbrgggggggroooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test070_solves_full_cube_up_to_top_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rybwoogrrorygbobwygygbrybgbwwyogrrbrobogybggwwyywwowro'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test080_solves_full_cube_up_to_top_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ryrworgbyywyggbooborgwrywrgwbwgbowyyoybowgbobrrgbygrwo'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test090_solves_full_cube_up_to_top_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oobwogoggwbbrbyrwwooogryroygygbgrrobwwwryrybrywygwbbyg'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test100_solves_full_cube_up_to_top_corners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wgroorywwywoygooyygywwrrbbyryrwbboorbgwowggrbgbbgybgro'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 8
        expectedResult['right']  = (inputDict.get('cube')[13]) * 8
        expectedResult['back']   = (inputDict.get('cube')[22]) * 8
        expectedResult['left']   = (inputDict.get('cube')[31]) * 8
        expectedResult['top']    = (inputDict.get('cube')[40]) * 9
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[0]  + cube[2]  + cube[3:9]
        actualResult['right']  = cube[9]  + cube[11] + cube[12:18]
        actualResult['back']   = cube[18] + cube[20] + cube[21:27]
        actualResult['left']   = cube[27] + cube[29] + cube[30:36]
        actualResult['top']    = cube[36:45]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
        
        
        
        