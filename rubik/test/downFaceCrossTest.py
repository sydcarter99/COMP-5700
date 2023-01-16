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
        
    def test010_solves_cube_with_cross_solved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gbgbbbbbboobrrrrrrrgoggggggbrrooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'
        expectedResult['rotations'] = ''
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations')) 
        
    def test020_solves_front_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gggbbbbbboororrorrbbbggggggorrooroorwwwyyyyyyyyywwwwww'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test030_solves_right_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ggyobgybwbrwyrybwwbrgbggggyryroobbogwyooybyrrowrwwrowo'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 

    def test040_solves_back_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oyogbrgbybgryryrrgbbyggbwowrbbyorgoogowrywwoyywbwwwogr'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status'))
        
    def test050_solves_left_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oororrorrbbbggggggorrooroorgggbbbbbbyywyywyywywwywwyww'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status'))
        
    def test060_solves_front_and_right_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oyrgbrogowwywrbgyybbwogbggbrrbyoroogbrryybwogwoywwgywr'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test070_solves_front_and_back_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wybobbrrryyworwwrogbyggbggwbrowoygogryrgyrbgoybbwwwooy'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test080_solves_front_and_left_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rbborrgygywowgowggyrwyoyoorbgbgbbwbyoggoybyrorrrywwbww'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test090_solves_right_and_back_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrgbbwbbryrrgrrgyyyooggyogwbbwroogooyybyybbwrwwwwwgoog'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 

    def test100_solves_right_and_left_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gbrgryrrogybggbbbrwooyobgoybrorboogyyyrgyrwoybwwwwwgww'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test110_solves_back_and_left_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ooyrggrggbrbyorrogyggwbbyorwybyrbgwbooorygwyrwwybwwwbo'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test120_solves_front_right_and_back_edges_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ggrbgbwgowobyoyyrbwrgobrygoyboyrwgrbrbroywwygoobwwgywr'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test130_solves_right_back_and_left_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wgyobrbbwgrryryoowywwoggbggobrwobryygobrywgyoowbbwgyrr'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test140_solves_back_left_and_front_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oygrrorroyywggbggwgrwooogyorwywbwbrybyrbyobgrbgybwwwbo'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test150_solves_left_front_and_right_edge_of_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbwggwryoowbooygyrwyyrbrbborrowrobbwgbrgygyoggoyrwgwwy'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test160_solves_a_full_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbworwyoybywrgbggoowgoogyrrryrwbybygwoggyrwwoogrbwrybb'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test170_solves_a_full_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'byggggyogwygwogrorrbbrbywyyoworroowbwrwrygyborbybwwgob'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test180_solves_a_full_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yoyobywwrgyobrbgggbrwwgoowbroggoyybbbgybyrrwoogwrwyrrw'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test185_solves_a_full_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ywygyroyogyrgorwywobbbrorogrwbrgwbwrggwrbooowbgyywbybg'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test190_solves_a_full_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'byowowyrwggrrgboowbrggbgrrgywgywbybwbbwororwrboyyyyogo'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
    def test195_solves_a_full_downface_cross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rooowwbbwrowyryborbwbbgryyygrggbgrryobowyrowwggyyobwgg'
        
        actualResult = solve._solve(inputDict)
        
        rotateCube = {}
        rotateCube['cube'] = inputDict.get('cube')
        rotateCube['dir'] = actualResult.get('rotations')
        cube = rotate._rotate(rotateCube).get('cube')
        
        self.assertEqual(cube[46], cube[49])
        self.assertEqual(cube[48], cube[49])
        self.assertEqual(cube[50], cube[49])
        self.assertEqual(cube[52], cube[49])
        self.assertEqual(cube[4],  cube[7])
        self.assertEqual(cube[13], cube[16])
        self.assertEqual(cube[22], cube[25])
        self.assertEqual(cube[31], cube[34])
        
        self.assertEqual('ok', actualResult.get('status')) 
        
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


