class ValidateWeapon(object):
    """description of class"""
    def __init__(self):
        self.__fails = {'type':False, 'wa':False, 'con':False, 'av':False, 'dmg':False, 'shots':False, 'rof':False, 'rel':False, 'range':False, 'cost':False}

    def run_tests(self, type, wa, con, av, dmg, shts, rof, rel, range, cost):
        #'name', 'type',  'wa',   'con',  'av',   'dmg',  'ammo', 'shts', 'rof',  'rel',  'range', 'cost'
        self.__fails['type']  = self.test_type(type)
        self.__fails['wa']    = self.test_WA(wa)
        self.__fails['con']   = self.test_con(con)
        self.__fails['av']    = self.test_ava(av)
        self.__fails['dmg']   = self.test_dmg(dmg)
        self.__fails['shots'] = self.test_shots(shts)
        self.__fails['rof']   = self.test_rof(rof)
        self.__fails['rel']   = self.test_rel(rel)
        self.__fails['range'] = self.test_range(range)
        self.__fails['cost']  = self.test_cost(cost)

        fail = False
        for key, value in self.__fails.items():
            if value==True:
                fail = True
                print('failed weapon')
        #print(str(self.__fails))
        return fail

    def test_type(self, type):
        fail = False

        if type == "P":
            typetext = 'Pistol'
        elif type == "SMG":
            typetext = 'Submachinegun'
        elif type == "SHT":
            typetext = 'Shotgun'
        elif type == "RIF":
            typetext = 'Rifle'
        elif type == "HVY":
            typetext = "Heavy"
        else:
            fail = True
        return fail

    def test_ava(self, ava):
        fail = False
        if ava == 'E':
            avatext = 'Excellent'
        elif ava == 'C':
            diff = 18
            avatext = 'Common'
        elif ava == 'P':
            avatext = 'Poor'
        elif ava == 'R':
            avatext = 'Rare'
        elif ava == 'N':
            avatext = 'Unavailable'
        else:
            fail = True
        return fail

    def test_con(self, con):
        fail = False
        if con =='P':
            context = 'Pocket, Pants or Sleeve'
        elif con == 'J':
            context = 'Jacket, Coat or Shoulder Rig'
        elif con == 'L':
            context = 'Long Coat'
        elif con == 'N':
            context = 'Cant be Hidden'
        else:
            fail = True
        return fail

    def test_WA(self, wa):
        fail = False
        try:
            wa_int = int(wa)
        except Exception:
            fail = True
        return fail

    def test_dmg(self, dmg):
        dmg_dices=0
        dmg_sides=0
        bonus_dmg=0
        fail = False
        #print(len(dmg))
        #print(dmg)
        if len(dmg)==3:
            line = dmg.split('d',-1)
            #print(line)
            try:
                dmg_dices=int(line[0])
                dmg_sides=int(line[1])
            except Exception:
                fail=True
        elif len(dmg)==4:
            line = dmg.split('d', -1)
            try:
                dmg_dices=int(line[0])
                dmg_sides=int(line[1])
            except Exception:
                fail=True
            
        elif len(dmg)==5:
            if dmg.count('+')==1:
                try:
                    line = dmg.split('+', -1)
                    plus_mod = int(line[1])
                    base_damage = line[0].split('d', -1)
                    dmg_dices=int(base_damage[0])
                    dmg_sides=int(base_damage[1])
                except Exception:
                    fail = True
            elif dmg.count('-')==1:
                try:
                    line = dmg.split('-', -1)
                    plus_mod = int(line[1])
                    base_damage = line[0].split('d', -1)
                    dmg_dices=int(base_damage[0])
                    dmg_sides=int(base_damage[1])
                except Exception:
                    fail = True
            else:
                fail=True
        else:
            fail=True
        return fail

    def test_shots(self, shots):
        fail=False
        try:
            number = int(shots)
        except Exception:
            fail = True
        return fail

    def test_rof(self, rof):
        fail = False
        try:
            if rof.count('/')==1:
                array = rof.split('/')
                rof = array[1]
            number = int(rof)
        except Exception:
            fail = True
        return fail

    def test_rel(self, rel):
        fail = False
        text = ''
        if rel.count('*')==1:
            rel = rel[:-1]
        if rel == 'UR':
            text = 'Unreliable'
        elif rel == 'ST':
            text = 'Standard'
        elif rel == 'VR':
            text = 'Very reliable'
        else:
            text = 'fail'
            fail=True
        return fail

    def test_range(self, range):
        fail = False
        try:
            number = int(range[:-1])
        except Exception:
            fail=True
        return fail

    def test_cost(self, cost):
        fail = False
        try:
            number = int(cost)
        except Exception:
            self.fail=True
        return fail

