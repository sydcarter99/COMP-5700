'''
Created on Oct 4, 2022

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
    
    def test010_solves_cube_with_middle_layer_solved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gbgbbbbbboobrrrrrrrgoggggggbrrooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'
        expectedResult['rotations'] = ''
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test020_solves_front_right_edge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ryrbbybbbggobrrrrrbogggggggobbooooooyyyryyyrywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test030_solves_right_back_edge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rgbrrrrrrrgyggyggggoyrooooooyybbbbbbbyobyygoywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test040_solves_back_left_edge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'byyrrrrrrrogggggggoyyooyooooyyrbbbbbbbygybrogwwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test050_solves_left_front_edge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbbbbbbbrryrrrrrrryoggggggyyoooyooogoggyyyoywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test060_solves_entire_middle_layer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yboybybbbbrggrrrrroryygogggrgrbooooogbyoygbyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test070_solves_bottom_two_layers(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ybbygwryborwoowowororbbywgrggobrrgwyygbrybgowboygwrwyg'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test080_solves_bottom_two_layers(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrbwwroyrrbwwrryogbogyybwoyoywoogbggygogbwbbywbgrgyowr'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test090_solves_bottom_two_layers(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'grygrrrrrobbygrgggrgygoyooorbyobybbbgoyyyoobbwwwwwwwww'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test100_solves_bottom_two_layers(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ggrbgbwgowobyoyyrbwrgobrygoyboyrwgrbrbroywwygoobwwgywr'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
    def test110_solves_bottom_two_layers(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bgbogrorrgbbyrgooywyowybbyywyyrwwoggyogwbwrbrwogrogrbw'
        
        expectedResult = {}
        expectedResult['bottom'] = (inputDict.get('cube')[49]) * 9
        expectedResult['front']  = (inputDict.get('cube')[4])  * 6
        expectedResult['right']  = (inputDict.get('cube')[13]) * 6
        expectedResult['back']   = (inputDict.get('cube')[22]) * 6
        expectedResult['left']   = (inputDict.get('cube')[31]) * 6
        
        solvedCube = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = solvedCube.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        actualResult = {}
        actualResult['bottom'] = cube[45:54]
        actualResult['front']  = cube[3:9]
        actualResult['right']  = cube[12:18]
        actualResult['back']   = cube[21:27]
        actualResult['left']   = cube[30:36]
        
        self.assertEqual(expectedResult, actualResult)
        self.assertEqual('ok', solvedCube.get('status'))
        
        