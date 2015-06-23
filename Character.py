from GameObject import GameObject
from GameObject import Item
import copy


class Character(GameObject):
    """description of class"""

    def __init__(self, preferences=object()):
        """

        :type preferences: object
        """
        super().__init__()
        self.prefs = preferences
        self.__fuz_dice = self.prefs.get_new_dice(3, 6, True)
        self.__inventory = {}

        stat_dict = self.prefs.get_stats()
        d_stat_dict = self.prefs.get_derived_stats()

        for key, value in stat_dict.items():
            value.set_attribute('lvl', 2)
            self.set_attribute(key, value)
        for key, value in d_stat_dict.items():
            self.set_attribute(key, value)

        self.calc_derived_stats()

    def fuz_roll(self, detailed=False):
        if detailed:
            self.__fuz_dice.roll()
            return self.__fuz_dice.latest_resultset()
        else:
            return self.__fuz_dice.roll()

    def set_stat(self, name, attribute, value):
        try:
            stat = self.get_attribute(name)
            stat.set_attribute(attribute, value)
        except Exception as e:
            print("error setting stat in Character")
            print(e)

    def set(self, command, value):
        try:
            commands = command.split('.', -1)
            command1 = commands[0]
            # print(str(commands))

            if command1 == 'skill':
                self.set_stat(commands[1], commands[2], int(value))
            if command1 == 'personality':
                # print('command[0] = ' + command1 + ' command[1] = ' + commands[1])
                stat = self.search_stat_with_attribute("category", commands[1])
                stat.set_attribute('name', value)
        except Exception as e:
            print(e)

    def search_stat_with_attribute(self, search_from, searched_name):
        for key, value in self.get_all_attributes().items():
            try:
                # print('search_from: ' + search_from + ' searched_name: ' +searched_name)
                if value.get_attribute(search_from) == searched_name:
                    # print('returning value')
                    return value
            except Exception:
                pass

    def get_stat(self, name, attribute, category_search=False, return_all=False):
        if category_search:
            all_results = []
            for key, value in self.get_all_attributes().items():
                try:
                    category = value.get_attribute('category')
                    if category == name:
                        if return_all:
                            all_results.append(value.get_attribute('name'))
                        else:
                            return value.get_attribute('name')

                except Exception:
                    pass
            if return_all:
                return all_results
        stat = self.get_attribute(name)
        return stat.get_attribute(attribute)

    def get_stat_list(self, list_name):
        stat_list = {}
        attribute_list = self.get_all_attributes()

        for key, value in attribute_list.items():
            try:
                stat_type = value.get_attribute('type')
                if stat_type == list_name:
                    stat_list[key] = value
            except Exception:
                pass
        return stat_list

    def get_inventory(self):
        return self.__inventory

    def clean_skills(self):
        dictionary = self.get_all_attributes()
        deletable = []
        # print('dict is ' +str(dict))

        for key, value in dictionary.items():
            try:
                type = value.get_attribute('type')
                # print(type)
                if type == 'skill':
                    lvl = value.get_attribute('lvl')
                    if lvl == 0:
                        deletable.append(value.get_attribute('name'))
            except Exception:
                pass
        for item in deletable:
            self.destroy_attribute(item)

    def add_stat_collection(self, collection, collection_type='type'):
        for key, value in collection.items():
            name = str.lower(key)
            # stat = self.prefs.get_stat(name)
            stat = copy.deepcopy(self.prefs.get_from_master(name))
            # print(stat)
            # print('key is ' +key)
            # if stat.get_attribute('name')!='undefined':
            try:
                # print('key is ' + key)
                stat.set_attribute('type', collection_type)
                stat.set_attribute('name', name)
                stat.set_attribute('lvl', int(value))
                self.set_attribute(name, stat)
            except Exception:
                pass
                # print(str(stat))
        self.calc_derived_stats()
        self.clean_skills()

    def add_cyberwear_collection(self, cyberwearlist):
        for cyberwear in cyberwearlist:
            name = cyberwear.get_attribute('name')
            # print('name is ' + name)
            self.__inventory[name] = cyberwear
        for key, value in self.__inventory.items():
            # print(str(value))
            pass

    def add_item_collection(self, itemlist):
        for i in range(0, len(itemlist[0])):
            item = Item(itemlist[1][i])
            item.set_attribute('type', itemlist[2][i])
            self.__inventory[item.get_attribute('name')] = item

    def add_skill(self, name, lvl=0, is_default=True, stat='null', diff=1, is_chippable=False, category='default', ip=0,
                  chipped=False):
        """

        :type name: str
        """
        skill = object()

        try:
            blueprint = copy.deepcopy(self.prefs.get_from_master(name))
        except:
            is_default = False
        if is_default:
            skill = copy.deepcopy(self.prefs.getSkill(name))
            skill.set_attribute('type', 'skill')
            skill.set_attribute('lvl', lvl)
            skill.set_attribute('ip', ip)
            skill.set_attribute('chip', chipped)
        else:
            skill = Stat(name, stat=stat, lvl=lvl, isChippable=is_chippable, category=category, diff=diff, ip=ip,
                         chip=chipped, type='skill')

        self.set_attribute(name, skill)
        skill.increase_experience(ip)

    def remove_all_attributes_of_type(self, type, attribute):
        """removes all attributes of type, who have attribute == type
        """
        to_be_removed = []
        all_attributes = self.get_all_attributes()
        for key, value in all_attributes.items():
            try:
                type2 = value.get_attribute(attribute)
                if type2 == type:
                    to_be_removed.append(key)
            except Exception as e:
                print(e)
        for key in to_be_removed:
            del (all_attributes[key])

    def add_personality(self, name, category, type='personality'):
        # print('name: ' + name + ' category: ' + category)
        stat = Stat(name=name, category=category, type=type)
        self.set_attribute(name, stat)

    def add_sibling(self, name, gender, age, relation, type='sibling', category='relative'):
        sibling = Stat(name=name, gender=gender, age=age, relation=relation, type=type, category=category)
        # print(str(sibling.get_all_attributes()))
        self.set_attribute(name, sibling)

    def add_complication(self, name, inten, freq, impor, type='complication'):
        complication = Stat(name=name, intensity=inten, frequency=freq, importance=impor, type=type)
        self.set_attribute(name, complication)

    def get_bpoints(self, skill_name):
        lvl = 0
        stat_points = 0
        # print('beginning bp function with character ' +self.get_attribute('player'))
        try:
            skill = self.get_attribute(skill_name)
            lvl = skill.get_attribute('lvl')
            print('1. ' + str(skill) + ' with lvl ' + str(lvl))
        except Exception:
            try:
                required_stat = self.prefs.get_skill_attribute(skill_name, 'stat')
                # print('required_stat is ' +str(required_stat))
                # print('required_stat is ' +required_stat)
                stat_points = self.get_stat(required_stat, 'lvl')

            except Exception:
                pass

        try:
            stat_name = skill.get_attribute('stat')
            print('stat_name is ' + str(stat_name))
            stat_points = self.get_stat(stat_name, 'lvl')
            # print('2. statpoints are ' +str(stat_points))
        except Exception:
            pass
        bp = lvl + stat_points
        # print('skill + stat is ' + str(bp) + ' (' + str(lvl) + '+'+str(stat_points)+')')
        return bp

    def calc_derived_stats(self):
        attribute_dict = self.get_all_attributes()
        derived_stats = []
        for key, value in attribute_dict.items():
            try:
                if value.get_attribute('type') != 0:
                    if value.get_attribute('type') == 'derived':
                        derived_stats.append(value)
            except Exception:
                pass

        for stat in derived_stats:
            sum = 0
            sources = stat.get_attribute('source_stats')
            divider = int(stat.get_attribute('divider'))
            multiplier = int(stat.get_attribute('multiplier'))
            for source in sources:
                if source != 'none':
                    attr = self.get_stat(source, 'lvl')
                    sum += int(attr)

            result = (sum * multiplier) / divider
            stat.set_attribute('lvl', result)

    def load(self):
        pass

    def save(self, db):
        skills = self.get_stat_list("skills")
        for skill, value in skills.items():
            chipped = skill.get_attribute('chipped')
            ip_cap = skill.get_attribute('lvl')
            ip = skill.get_attribute('ip')
            lvl = skill.get_attribute('lvl')
            db.add(0, 0, chipped, ip_cap, ip, lvl, search_with_skill_name=True, search_with_char_name=True, skill_name = skill.get_attribute('name'), char_name=self.get_attribute("name"))





    def __str__(self):
        returned = ''
        for key, value in self.get_all_attributes().items():
            returned = returned + str(value) + '\n'
        return returned


class Stat(GameObject):
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


class Effect(GameObject):
    def __init__(self, name='default', duration='forever', modifier=0, target_type='stat', target_name='int'):
        super().__init__()
        self.set_attribute('name', name)
        self.set_attribute('duration', duration)
        self.set_attribute('modifier', modifier)
        self.set_attribute('target_type', target_type)
        self.set_attribute('target_name', target_name)
        


