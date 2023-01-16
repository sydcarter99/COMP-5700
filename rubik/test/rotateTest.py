
import unittest
import rubik.rotate as rotate

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


# Analysis:
#
#    inputs:
#        params:    dict: mandatory, arrives validated
#        params['op']:    string; 'rotate', manditory, arrives validated
#        params['cube']:    string; len: 54, [brgoyw], 9 occurrences of each char, mandatory, arrives unvalidated
#        params['dir']:    string; len >= 0, [Ff,Rr,Bb,Ll,Uu,Dd], optional, defaults to F if missing, arrives unvalidated
#
#    outputs:
#        side effects:    no state changes; no external effects
#        returns: dict
#        nominal:
#            dict['cube']:    string, valid cube
#            dict['status']:    'ok'
#        abnormal:
#            dict['status']:    'error: xxx'
#
#    happy path:
#        test 010: nominal valid cube with F rotation
#        test 020: nominal valid cube with f rotation
#        test 030: nominal valid cube with R rotation
#        test 040: nominal valid cube with r rotation
#        test 050: nominal valid cube with B rotation
#        test 060: nominal valid cube with b rotation
#        test 070: nominal valid cube with L rotation
#        test 080: nominal valid cube with l rotation
#        test 090: nominal valid cube with U rotation
#        test 100: nominal valid cube with u rotation
#        test 110: nominal valid cube with D rotation
#        test 120: nominal valid cube with d rotation
#
#    sad path:
#        test 910: invalid cube with valid rotation
#        test 920: valid cube with invalid rotation

    def test010_rotate_F_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wgyowoywyorbbybowroogggryrbobbybwgggbywrrgrogrywyobrww'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['cube'] = 'yowwwgyoyrrboybgwroogggryrbobrybyggwbywrrggwboboyobrww'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 

    def test020_rotate_f_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rgrbrbrowbwowoygwrwyywwybbbwgyogrobygryrygoyogrbgbowog'
        inputDict['dir'] = 'f'
        
        expectedResult = {}
        expectedResult['cube'] = 'rbwgrorbrbworoygwrwyywwybbbwgoogyobogryrygbwgyrygbowog'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test030_rotate_R_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rgwwgrgybbyoorgryygroobywogbwgrwgwoorbwbywyrorgywobybb'
        inputDict['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['cube'] = 'rgywgbgybrobyryygoorowbywogbwgrwgwoorbwbyryrbrgwwooybg'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test040_rotate_r_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wwwygyoboggrbroyrbygogyrwgrybbyboorgrrwwwwyyrboboowgbg'
        inputDict['dir'] = 'r'
        
        expectedResult = {}
        expectedResult['cube'] = 'wwwygwobrrobgrrgbyggowyrbgrybbyboorgrrwwwgyyybowooygbo'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test050_rotate_B_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'owwyrobgoywwrwyyryrwbbyyobyrbrooggrowggobygbbrobwggwrg'
        inputDict['dir'] = 'B'
        
        expectedResult = {}
        expectedResult['cube'] = 'owwyrobgoywgrwryrwobrbywyybgbrgogwrowyyobygbbrobwggrog'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test060_rotate_b_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'ygryobbogbyygryyyyoboogooggrrgbygrrrwrwowwwwgowbwbbwrb'
        inputDict['dir'] = 'b'
        
        expectedResult = {}
        expectedResult['cube'] = 'ygryobbogbywgrryywoogbggooowrgrygbrrrbrowwwwgowbwbbyyy'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test070_rotate_L_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wrbywwbogrgoyrybbbwbwbbrrrwgrygyggyyrorbowoogowyoggywo'
        inputDict['dir'] = 'L'
        
        expectedResult = {}
        expectedResult['cube'] = 'rrbbwwoogrgoyrybbbwbybborrogggyyrygyworrowwogwwyyggbwo'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test080_rotate_l_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rbobbywywwwrgogbgrbwyoyrbbggwyyroogroogygrgwyyoobwrbrw'
        inputDict['dir'] = 'l'
        
        expectedResult = {}
        expectedResult['cube'] = 'ybobbybywwwrgogbgrbwgoyybboyorwrggyorogbgrwwygoorwryrw'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test090_rotate_U_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'oobybgrbooyywrbgwygboywwgrwwgwrgrrgyrobbyggwrbrbooyyow'
        inputDict['dir'] = 'U'
        
        expectedResult = {}
        expectedResult['cube'] = 'oyyybgrbogbowrbgwywgwywwgrwoobrgrrgygbrwyorgbbrbooyyow'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test100_rotate_u_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wrbyrgwygrrbogoowrybbyowgyygoyrywooyogrwbgrbgobwbwgbrw'
        inputDict['dir'] = 'u'
        
        expectedResult = {}
        expectedResult['cube'] = 'goyyrgwygwrbogoowrrrbyowgyyybbrywooyrgggbbowrobwbwgbrw'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test110_rotate_D_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wwrybbgygwrrgwgwryoybwybwooowyooogwyrgyrgorbborbyrbbgg'
        inputDict['dir'] = 'D'
        
        expectedResult = {}
        expectedResult['cube'] = 'wwrybbgwywrrgwggygoybwybwryowyooowoorgyrgorbbbyogrrgbb'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test120_rotate_d_on_nominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'oroyoyobbrobwrwwbrgogbyryogbgwgbryoworyygbbwgryygwgrww'
        inputDict['dir'] = 'd'
        
        expectedResult = {}
        expectedResult['cube'] = 'oroyoywbrrobwrwyoggogbyryowbgwgbrobboryygbbwgygwywwrgr'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test130_rotate_on_multiple_rotations(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wbywyoyygggbwgyroorbwgwgwrrroorbbgrobyybowbroboywrgwyg'
        inputDict['dir'] = 'flubruFLbRufdruDUFUDLbdul'
        
        expectedResult = {}
        expectedResult['cube'] = 'wywwyyyrwbroogrboybyggwoobywyrwbbrwrobyrobggogwrgrgbog'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test140_rotate_on_empty_rotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'brryrwrrboooowwoygybwgbbrbbgygoybwyyrgbrgrywwogwooggwy'
        inputDict['dir'] = ''
        
        expectedResult = {}
        expectedResult['cube'] = 'rybrrrbwryoowwwwygybwgbbrbbgyooygwywrgbrgrybgoooooggwy'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test150_rotate_on_missing_rotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'yywgwwwrrgwroyobywogygrrgybbbrbgrrgowwgwbyoroyogbobyob'
        
        expectedResult = {}
        expectedResult['cube'] = 'wgyrwyrwwowrryooywogygrrgybbbybgorggwwgwbyorrbogbobyob'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test910_missing_cube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test920_short_cube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbbbbbbb'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test930_long_cube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwwb'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test940_cube_with_illegal_characters(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrr666666666oooooooooyyyyyyyyywwwwwwwww'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test950_cube_with_illegal_characters(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrr666666666oooooooooyyyyyyyyywwwwwwwww'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test960_cube_with_wrong_amt_of_legal_characters(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test970_cube_with_non_unique_legal_elements(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test980_invalid_rotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['dir'] = 'x'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid direction'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test990_invalid_multiple_rotations(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['dir'] = 'FF FF'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid direction'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
        
        
        

