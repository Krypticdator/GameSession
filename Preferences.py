from XmlController import XmlController
import copy
from Character import Stat
from Character import Effect
from random import randrange
from FileController import FileControl
class Preferences(FileControl):
    """description of class"""
    def __init__(self):
        self.__stats = {}
        self.__skills = {}
        self.__derived_stats = {}
        self.__complications = {}
        self.__talents = {}
        self.__perks = {}
        self.__master_directory={}
        self.__tables = {}
        self.__probability_tables = {}
        self.__effects = {}


        self.load_stats()
        self.load_skills()
        self.load_complications()
        self.load_perks_talents()

        self.commit_to_master(self.__derived_stats)
        self.commit_to_master(self.__stats)
        self.commit_to_master(self.__skills)
        self.commit_to_master(self.__complications)
        self.commit_to_master(self.__talents)
        self.commit_to_master(self.__perks)

        self.load_tables()

        self.load_probabilities()

   

    def load_stats(self):
        x = XmlController()
        x.load_file('preferences/preferences.xml')
        stats = x.get_dataset("primary_stats", True)

        for key, value in stats.items():
            self.__stats[key] = Stat(name=key, type='stat',description=value)

        params = ['name', 'first_source','second_source', 'multiplier','divider']
        derived_stats = x.get_dataset('secondary_stats',False,False,True,params)
        
        for array in derived_stats:
            sources = [array[1], array[2]]
            derived = Stat(name=array[0],type='derived',source_stats=sources, multiplier=array[3], divider=array[4])
            self.__derived_stats[array[0]]=derived

    def load_effects(self):
        x = XmlController()
        x.load_file('preferences/effects.xml')
        
        effects = x.get_dataset('effects',False,True)
        num = 0
        for array in effects:
            pass


        print(effects)

    def save_skills(self):
        x = XmlController()
        system = 'modified fuzion'
        x.create_root('skills')
        x.set_value('system', system,'root')
        for name, skill in self.__skills.items():
            x.create_sub_element('skill', 'root')
            x.create_sub_element('name','skill')
            x.set_text(name,'name')

            x.create_sub_element('stat','skill')
            try:
                x.set_text(skill.get_attribute('stat'),'stat')
            except Exception:
                x.set_text('not found','stat')

            x.create_sub_element('category','skill')
            try:
                x.set_text(skill.get_attribute('category'),'category')
            except Exception:
                x.set_text('not found','category')

            x.create_sub_element('description','skill')
            try:
                x.set_text(skill.get_attribute('description'),'description')
            except Exception:
                x.set_text('not found','description')

            x.create_sub_element('chippable','skill')
            try:
                x.set_text(skill.get_attribute('ischippable'),'chippable')
            except Exception:
                x.set_text('not found','chippable')

            x.create_sub_element('diff_modifier','skill')
            try:
                x.set_text(skill.get_attribute('diff'),'diff_modifier')
            except Exception:
                x.set_text('not found','diff_modifier')

            x.create_sub_element('short', 'skill')
            try:
                x.set_text(skill.get_attribute('short'), 'short')
            except Exception:
                x.set_text('not found','short')
        x.save_file('preferences/skills.xml')

    def load_skills(self):
        x = XmlController()
        try:
            x.load_file('preferences/skills.xml')
        except Exception:
            x.load_file('preferences/preferences.xml')
        extract = x.get_dataset('skills', False, True)
        #print(extract)
        for array in extract:
            skill = Stat(name=str.lower(array[0]), stat=str.lower(array[1]), category=str.lower(array[2]), description=array[3], isChippable=array[4], diff=array[5])
            try:
                skill.set_attribute('short', array[6])
            except Exception:
                skill.set_attribute('short', 'not found') 
            self.__skills[str.lower(array[0])]=skill


        #print(self.__skills)
    def load_complications(self):
        x = XmlController()
        x.load_file('preferences/preferences.xml')
        extract = x.get_dataset('complications',False, True)

        for array in extract:
            complication = Stat(name=array[0], category=array[1], description=array[2], type='complication')
            self.__complications[array[0]]=complication

    def load_perks_talents(self):
        x=XmlController()
        x.load_file('preferences/preferences.xml')
        extract = x.get_dataset('perks',False, True)

        for array in extract:
            perk = Stat(name=array[0], description=array[1])
            self.__perks[array[0]]=perk

        extract = x.get_dataset('talents', False, True)

        for array in extract:
            talent = Stat(name=array[0], description=array[1])
            self.__talents[array[0]]=talent

    def load_table(self, table_name):
        x=XmlController()
        x.load_file('preferences/preferences.xml')
        table = x.read_table(table_name)
        t = Table() 
        #print(table_name)
        for option in table:
            t.add_option(option[0], option[1],option[2],True)

        #print(t)
        return copy.deepcopy(t)

    def load_tables(self):
        x = XmlController()
        x.load_file('preferences/preferences.xml')
        tables = x.read_table_names()
        for name in tables:
            self.__tables[name] = self.load_table(name)

    def table(name):
        return copy.deepcopy(self.__tables[name])

    def random_table_choice(self, table_name):
        return copy.deepcopy(self.__tables[table_name].get_random_option())
        

    def load_character(self, filepath, character):
        x=XmlController()
        x.load_file(filepath)
        player = x.get_node_value('info','player')
        fname = x.get_node_value('info', 'first_name')
        sname = x.get_node_value('info', 'second_name')
        lname = x.get_node_value('info', 'last_name')
        alias = x.get_node_value('info', 'alias')
        age = x.get_node_value('info', 'age')

        personality_array = x.get_dataset('personality',False, simple=True, simple_no_dict=True)
        
        for i in range(0,len(personality_array[0])):
            key =personality_array[0][i]
            value = personality_array[1][i]

            character.add_personality(value, key)

        family_dict = x.get_dataset('family', False, simple=True)

        for key, value in family_dict.items():
            #print('key is ' +str(key)+ ' and value is ' +str(value))
            character.set_attribute(str(key), str(value))
        
        tag_params = ['age', 'gender', 'relation']
        siblings_array = x.get_dataset('family', False, False, True, tag_params)
        #print(str(siblings_array))

        siblings_names = x.get_dataset('family', False, simple=True, simple_no_dict=True)
        #print(str(siblings_names))
        names = []
        for i in range(len(siblings_names[0])):
            key = siblings_names[0][i]
            value = siblings_names[1][i]

            if key=='sibling':
                names.append(value)
        sibling_num=0
        for array in siblings_array:
            if len(array)!=0:
                print(sibling_num)
                character.add_sibling(names[sibling_num], array[1], array[0], array[2])
                    
                sibling_num = sibling_num + 1

        stats = x.get_dataset('attributes', dictionary = True, dict_tag_name='type')
        skills = x.get_dataset('skills',True, dict_tag_name='type')
        talents = x.get_dataset('talents', True, dict_tag_name='type')
        perks = x.get_dataset('perks', True, dict_tag_name='type')

        comp_params = ['type', 'frequency', 'importance', 'intensity']
        complications = x.get_dataset('complications', False, False, True, comp_params)

        for array in complications:
            character.add_complication(array[0], array[3], array[1], array[2])


        character.set_attribute('player',player)
        character.set_attribute('fname', fname)
        character.set_attribute('sname', sname)
        character.set_attribute('lname', lname)
        character.set_attribute('alias', alias)
        character.set_attribute('age', age)
        character.add_stat_collection(stats)
        character.add_stat_collection(skills)
        character.add_stat_collection(talents)
        character.add_stat_collection(perks)

        cyberwear = x.get_cyberwear_from_character()
        character.add_cyberwear_collection(copy.deepcopy(cyberwear))


        #print(stats)
   
    def get_stat(self, name):
        returned=Stat();
        try:
            returned = copy.deepcopy(self.__stats[name])
        except Exception:
            pass
        return returned

    def get_stats(self):
        return copy.deepcopy(self.__stats)
    def get_derived_stats(self):
        return copy.deepcopy(self.__derived_stats)

    def getSkill(self, name):
        returned = Stat();
        try:
            returned = copy.deepcopy(self.__skills[name])
        except Exception:
            pass

        return returned

    def get_skills_dictionary(self):
        return self.__skills

    def get_skill_attribute(self, skill_name, attribute):
        try:
            skill = self.__skills[skill_name]
            return skill.get_attribute(attribute)
        except Exception:
            return 'error'
    def set_skill_attribute(self,skill_name, attribute, value):
        try:
            skill = self.__skills[skill_name]
            skill.set_attribute(attribute, value)
        except Exception:
            pass

    def commit_to_master(self, dictionary):
        for key, value in dictionary.items():
            self.__master_directory[key]=value

    def get_from_master(self, name):
        attribute = Stat()
        try:
            attribute = self.__master_directory[name]
        except Exception:
            pass
        return attribute

    def load_probabilities(self):
        file = self.read_file_to_segments('preferences/math_results.txt',';',True)
        bp_num=0
        for i in range(0,59):
            self.__probability_tables[i] = Table()
        for line in file:
            bp = int(line[0])
            dv = int(line[1])
            prob = float(line[2])

            self.__probability_tables[bp].add_option(dv, dv, prob, True)

    def get_probability(self, bp=0, dv=0):
        table = self.__probability_tables[bp]
        prob = table.get_option(dv)
        return prob

    def get_new_dice(self, dices, sides, fuzion=False):
        d = Dice(dices, sides, fuzion)
        return copy.deepcopy(d)
            

class Table(object):
    def __init__(self, dice_sides=10, dice_dices=1):
        self.__options = []
        self.__dice = Dice(dice_dices, dice_sides)

    def add_option(self, from_num=1, to_num=1, return_value='undefined', update_dice_sides=True):
        o = Option(from_num, to_num,return_value)
        self.__options.append(o)
        if update_dice_sides:
            self.__dice.set_sides(len(self.__options))

    def get_option(self, number):
        for option in self.__options:
            returned = option.is_right_option(number)
            if returned!='not this one':
               return returned

    def get_random_option(self):
        roll = self.__dice.roll()
        return self.get_option(roll)
    
    def __str__(self):
        line = ''
        for option in self.__options:
            line = line + str(option) + '\n'

        return line

class Option(object):
    def __init__(self, from_num, to_num, return_value):
        self.__from=from_num
        self.__to=to_num
        self.__return_value=return_value

    def is_right_option(self, num):
        if num >= int(self.__from) and num<=int(self.__to):
            return self.__return_value
        else:
            return 'not this one';

    def __str__(self):
        return str(self.__from) + '-' + str(self.__to) + ' ' + str(self.__return_value)

class Dice(object):
    def __init__(self, dices, sides, fuzion=False):
        self.__dices=dices
        self.__sides=sides
        self.__resultset = []
        self.__result=0
        self.__fuzion=fuzion

    def roll(self, method='default'):
        resultset = []
        total = 0
        if self.__fuzion:
            method='fuzion'
        if method=='default':
            self.__result = sum(randrange(self.__sides)+1 for die in range(self.__dices))
        else:
            for i in range(0,self.__dices):
                random_num = randrange(self.__sides)+1
                resultset.append(random_num)
                total += random_num
            self.__result = total
            
        if self.__fuzion:
            if self.__result == 18:
                for i in range(0, 2):
                    random_num=randrange(self.__sides)+1
                    self.__result +=random_num
                    resultset.append(random_num)
            if self.__result == 3:
                for i in range(0, 2):
                    random_num=randrange(self.__sides)+1
                    self.__result -=random_num
                    resultset.append(random_num*-1)
        self.__resultset.append(resultset)
                    
                        
        return self.__result

    def get_roll(self):
        return self.__result

    def latest_resultset(self):
        latest = len(self.__resultset)
        latest = latest -1
        return self.__resultset[latest]
    
    def set_dices(self, dices):
        self.__dices=dices

    def set_sides(self, sides):
        self.__sides=sides
   
        




