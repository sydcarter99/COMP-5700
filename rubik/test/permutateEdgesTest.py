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
        
    def test010_solves_three_edge_cycle(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'obooooooobgbbbbbbbrrrrrrrrrgogggggggyyyyyyyyywwwwwwwww'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test020_solves_three_edge_cycle(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ogooooooobobbbbbbbrrrrrrrrrgbgggggggyyyyyyyyywwwwwwwww'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test030_solves_three_edge_cycle(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bgbbbbbbbrrrrrrrrrgogggggggoboooooooyyyyyyyyywwwwwwwww'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test040_solves_three_edge_cycle(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgbgggggggogooooooobobbbbbbbyyyyyyyyywwwwwwwww'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test050_solves_opposite_edge_swap(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'orooooooobgbbbbbbbrorrrrrrrgbgggggggyyyyyyyyywwwwwwwww'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test060_solves_adjacent_edge_swap(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'obooooooobobbbbbbbrgrrrrrrrgrgggggggyyyyyyyyywwwwwwwww'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test070_solves_entire_cube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gbgyorobgrbyygyrrbbwwgrbwgwowyrbobobggrowwoywyoygywrro'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test080_solves_entire_cube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gyywobrgrbbgrgwgyyogwrrbbgybboobogrboyywwyworwwwgyrroo'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test090_solves_entire_cube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ywwboobygrggwgryboywrbrywwrygbrbogyobrrowrobbwgooyywgg'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test100_solves_entire_cube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yyoborbygggwwggwgybryyrwbboryroboggwgboowrbbwrrrwyoywo'
        
        cube = inputDict.get('cube')
        
        expectedResult = (cube[4]*9) + (cube[13]*9) + (cube[22]*9) + (cube[31]*9) + (cube[40]*9) + (cube[49]*9)
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        actualResult = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
        
        
        
        