__author__ = 'Toni'

def Property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @property.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)
        return prop

class Stat(object):
    name = Property('name', str)
    def __init__(self, name):
        self.name = name
        va




class StatOld():
    def __init__(self, name='undefined', type='skill', stat='int', lvl=0, ip=0, diff=1, chip=False, frequency=0,
                 importance=0, intensity=0, original=0, description='undefined', category='undefined',
                 is_chippable=False, source_stats=None, divider=1, multiplier=1, age=0, gender='male',
                 relation='undefined'):
        super().__init__()
        if source_stats is None:
            source_stats = []
        self.set_attribute('name', str.lower(name))
        self.set_attribute('type', type)
        self.set_attribute('lvl', int(lvl))
        self.set_attribute('description', description)
        if type == 'skill':
            self.set_attribute('stat', str.lower(stat))
            self.set_attribute('ip', int(ip))
            self.set_attribute('diff', int(diff))
            self.set_attribute('chip', chip)
            self.set_attribute('category', str.lower(category))
            self.set_attribute('ischippable', is_chippable)
        elif type == 'complication':
            self.set_attribute('frequency', int(frequency))
            self.set_attribute('importance', int(importance))
            self.set_attribute('intensity', int(intensity))
            self.set_attribute('category', str.lower(category))
        elif type == 'stat':
            self.set_attribute('original', original)
        elif type == 'derived':
            self.set_attribute('source_stats', source_stats)
            self.set_attribute('divider', int(divider))
            self.set_attribute('multiplier', int(multiplier))
        elif type == 'perk':
            pass
        elif type == 'talent':
            pass
        elif type == 'sibling':
            self.set_attribute('age', age)
            self.set_attribute('relation', relation)
            self.set_attribute('gender', gender)
        else:
            self.set_attribute('category', category)

    def increase_experience(self, exp):
        pool = self.get_attribute('ip')
        lvl = self.get_attribute('lvl')
        diff_mod = self.get_attribute('diff')
        cp_mod = 1  # Kuinka nopeasti tasot kasvavat
        pool += exp

        while pool > (lvl * diff_mod * cp_mod):
            limit = (lvl + 1) * diff_mod * cp_mod
            pool -= limit
            lvl += 1

        self.set_attribute('lvl', lvl)
        self.set_attribute('ip', pool)

    def __str__(self):
        name = self.get_attribute('name')
        lvl = self.get_attribute('lvl')
        return name + ' ' + str(lvl)
