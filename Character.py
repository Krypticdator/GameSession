from GameObject import GameObject
class Character(GameObject):
    """description of class"""

    def __init__(self, preferences=object()):
        super().__init__()
        self.prefs = preferences

        stat_dict=self.prefs.get_stats()
        d_stat_dict = self.prefs.get_derived_stats()

        for key, value in stat_dict.items():
            value.set_attribute('lvl', 2)
            self.set_attribute(key, value)
        for key, value in d_stat_dict.items():
            self.set_attribute(key, value)

        self.calc_derived_stats()

    def get_stat(self, name, attribute):
        stat = self.get_attribute(name)
        return stat.get_attribute(attribute)

    def clean_skills(self):
        dict = self.get_all_attributes()
        deletable = []
        for key, value in dict.items():
            try:
                type = value.get_attribute('type')
                if type=='skill':
                    lvl = value.get_attribute('lvl')
                    if lvl ==0:
                        deletable.append(value.get_attribute('name'))
            except Exception:
                pass
        for item in deletable:
            del self.


    def add_stat_collection(self, collection):
        for key, value in collection.items():
            name = str.lower(key)
            #stat = self.prefs.get_stat(name)
            stat = self.prefs.get_from_master(name)
            #print(stat)
            if stat.get_attribute('name')!='undefined':  
                try:
                    stat.set_attribute('name',name)
                    stat.set_attribute('lvl',int(value))
                    self.set_attribute(name, stat)
                except Exception:
                    pass
                #print(value)
        self.calc_derived_stats()
        self.clean_skills()

    
                

    def add_skill(self, name, lvl=0, isDefault=True, stat='null', diff=1, isChippable=False, category='default'):
        skill = object()
        if isDefault:
            skill = self.prefs.getSkill(name)
            skill.set_attribute('lvl',lvl)
        else:
            skill = Stat(name, stat=stat, lvl=lvl, isChippable=isChippable, category=category, diff=diff)

        self.set_attribute(name, skill)

    def get_bpoints(self, skill_name):
        skill = self.get_attribute(skill_name)
        lvl = skill.get_attribute('lvl')

        stat_name = skill.get_attribute('stat')
        stat_points = self.get_stat(stat_name,'lvl')
        bp = lvl + stat_points
        return bp
        
    def calc_derived_stats(self):
        attribute_dict = self.get_all_attributes()
        derived_stats = []
        for key, value in attribute_dict.items():
            if value.get_attribute('type')!=0:
                if value.get_attribute('type')=='derived':
                    derived_stats.append(value)
        
        for stat in derived_stats:
            sum=0
            sources = stat.get_attribute('source_stats')
            divider = int(stat.get_attribute('divider'))
            multiplier = int(stat.get_attribute('multiplier'))
            for source in sources:
                if source!='none':
                    attr = self.get_stat(source,'lvl')
                    sum = sum + int(attr)

            result = (sum * multiplier) / divider
            stat.set_attribute('lvl',result)




    def load(self):
        pass

    def save(self):
        pass

class Stat(GameObject):
    def __init__(self, name='undefined', type='skill', stat='int', lvl=0, ip=0, diff=1, chip=False, frequency=0, importance=0, intensity=0, original=0, description='undefined', category='undefined', isChippable=False, source_stats=[], divider=1, multiplier=1):
        super().__init__()
        self.set_attribute('name', str.lower(name))
        self.set_attribute('type', type)
        self.set_attribute('lvl', int(lvl))
        self.set_attribute('description', description)
        if type=='skill':
            self.set_attribute('stat', str.lower(stat))
            self.set_attribute('ip', int(ip))
            self.set_attribute('diff',int(diff))
            self.set_attribute('chip', chip)
            self.set_attribute('category',str.lower(category))
            self.set_attribute('ischippable', isChippable)
        elif type=='complication':
            self.set_attribute('frequency', int(frequency))
            self.set_attribute('importance', int(importance))
            self.set_attribute('importance', int(importance))
            self.set_attribute('category', str.lower(category))
        elif type=='stat':
            self.set_attribute('original', original)
        elif type=='derived':
            self.set_attribute('source_stats', source_stats)
            self.set_attribute('divider', int(divider))
            self.set_attribute('multiplier', int(multiplier))
        elif type=='perk':
            pass
        elif type=='talent':
            pass

    def increase_experience(self, exp):
        pool = self.get_attribute('ip')
        lvl = self.get_attribute('lvl')
        diff_mod = self.get_attribute('diff')
        cp_mod=1 #Kuinka nopeasti tasot kasvavat
        pool += exp

        while pool>(lvl*diff_mod*cp_mod):
            limit = (lvl +1) * diff_mod * cp_mod
            pool -=limit
            lvl = lvl +1

        self.set_attribute('lvl',lvl)
        self.set_attribute('ip',pool)
    def __str__(self):
        name = self.get_attribute('name')
        lvl = self.get_attribute('lvl')
        return name + ' ' + str(lvl)

class Effect(GameObject):
    def __init__(self, name='default', duration='forever', modifier=0, target_type='stat', target_name='int'):
        super().__init__()
        self.set_attribute('name', name)
        self.set_attribute('duration', duration)
        self.set_attribute('modifier', modifier)
        self.set_attribute('target_type', target_type)
        self.set_attribute('target_name', target_name)
        


