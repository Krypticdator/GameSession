from XmlController import XmlController
import copy
from Character import Stat
from Character import Effect
from random import randrange
from FileController import FileControl
from GameObject import Weapon
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
        self.__weapons = []

        self.load_tables()
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


        #print(effects)

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

    def table(self, name):
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
                #print(sibling_num)
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
        character.add_stat_collection(stats, 'stat')
        character.add_stat_collection(skills, 'skill')
        #print(str(talents))
        character.add_stat_collection(talents, 'talent')
        character.add_stat_collection(perks, 'perk')

        cyberwear = x.get_cyberwear_from_character()
        character.add_cyberwear_collection(copy.deepcopy(cyberwear))

        items = x.get_dataset('items', False, False, False, simple=True, simple_no_dict=True, simple_with_param=True, simple_param='type')
        character.add_item_collection(copy.deepcopy(items))

        lp = Lifepath(self)
        lp.convert_from_xml(filepath)

        character.set_attribute('lifepath', lp)

        #print(str(character.get_stat('light sleeper', 'name')))
        #print(str(character))
   
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

    def transfer_wpns_from_txt_to_sql(self):
        f = FileControl()
        wpn_arrays = []

        l_pistols_array = f.read_file_to_segments('data/wpns/txtfiles/l_pistols.txt', ';', True)
        
        wpn_arrays.append(l_pistols_array)
        
        for array in wpn_arrays:
            for w in array:
                #print(w[0])
                wpn = Weapon(w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11], '0', w[12], w[13])
                validation = wpn.validate()
                if validation == False:
                    #print('successful validation of weapon')
                    self.__weapons.append(wpn)
        return self.__weapons



class Table(object):
    def __init__(self, dice_sides=10, dice_dices=1):
        self.__options = []
        self.__dice = Dice(dice_dices, dice_sides)
        self.__last_roll = 0

    def add_option(self, from_num=1, to_num=1, return_value='undefined', update_dice_sides=True):
        o = Option(from_num, to_num,return_value)
        self.__options.append(o)
        if update_dice_sides:
            self.__dice.set_sides(len(self.__options))

    def get_option(self, number):
        ''''returns option specified by given number
        can be string or number'''
        for option in self.__options:
            returned = option.is_right_option(number)
            if returned!='not this one':
               return returned

    def get_random_option(self):
        roll = self.__dice.roll()
        self.__last_roll = roll
        return self.get_option(roll)

    def get_r_number(self):
        roll = self.__dice.roll()
        return roll

    def size(self):
        return len(self.__options)

    def num(self):
        return self.__last_roll
    
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
        if int(num) >= int(self.__from) and int(num)<=int(self.__to):
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

class Lifepath:
    '''TODO rewrite this some day'''

    def __init__(self, prefs, age=15):
        self.prefs = prefs
        self.events = []
        self.age = age

    def add_random_event(self, auto_increment=True, age='16'):
        datakeys = []
        if auto_increment:
            datakeys.append(self.age+1)
        else:
            datakeys.append(age)
        event_table = self.prefs.table('event_menu')
        event = event_table.get_r_number()
        datakeys.append(str(event))

        if event == 1:
            fourA_table = self.prefs.table('4A')
            luck_or_disaster = fourA_table.get_r_number()
            datakeys.append(luck_or_disaster)

            if luck_or_disaster == 1:
                pass

    def read_array_to_text(self, lifepath_array):
        lifepath = []
        for event in lifepath_array:
            text = ''
            type = event[1]
            #print('lifepath array' + str(event))

            if type == '1':
                luck_or_disaster = event[2]
                #print(str(event) + ' lifepath array')
                if len(event) > 3:
                    if event[3]=='0':
                        event[3] = '10'
                if luck_or_disaster == '1':
                    luck_table = self.prefs.table('lucky_table')
                    lucky = luck_table.get_option(event[3])
                    text = text + lucky
                    if event[3]=='1':
                        con_table = self.prefs.table('powerful_connection')
                        connection = con_table.get_option(event[4])
                        text = text + '. ' + connection
                else:
                    disaster_table = self.prefs.table('disaster_strikes')
                    disaster =  disaster_table.get_option(event[3])
                    text = text + disaster

                    if event[3] == '1':
                        debt = event[4]
                        debt_text = '. debt: ' + str(debt)
                        text = text + ' ' + debt_text
                    elif event[3] == '2':
                        time = event[4]
                        time_text = '. prisoned for ' + str(time) + ' months'
                        text = text + ' ' + time_text
                    elif event[3] == '3':
                        pass
                    elif event[3] == '4':
                        betrayel_table = self.prefs.table('betrayel_type')
                        betrayel = betrayel_table.get_option(event[4])
                        text = text + '. ' + betrayel_text
                    elif event[3] == '5':
                        accident_table = self.prefs.table('accident_type')
                        accident = accident_table.get_option(event[4])
                        text = text + '. ' + accident
                    elif event[3] == '6':
                        death_table = self.prefs.table('death_type')
                        death = death_table.get_option(event[4])
                        text = text + '. ' + death
                    elif event[3] == '7':
                        accusation_table = self.prefs.table('accusation_type')
                        accusation = accusation_table.get_option(event[4])
                        text = text + '. ' + accusation
                    elif event[3] == '8':
                        crime_table = self.prefs.table('crime_type')
                        crime = crime_table.get_option(event[4])
                        text = text + '. ' + crime
                    elif event[3] == '9':
                        corp_table = self.prefs.table('corporation_type')
                        corp = corp_table.get_option(event[4])
                        text = text + '. ' + corp
                    elif event[3] == '10':
                        breakdown_table = self.prefs.table('breakdown_type')
                        breakdown = breakdown_table.get_option(event[4])
                        text = text + '. ' + breakdown
            elif type == '2':
                friend_or_enemy = event[2]

                if friend_or_enemy == '1':
                    text = text + 'friend: '
                    friend_table = self.prefs.table('friend_relationships')
                    friend = friend_table.get_option(event[3])
                    text = text + ' ' + friend
                elif friend_or_enemy == '2':
                    #[e_type, cause, relation, reaction, resource]
                    enemy_type = event[3]
                    cause = event[4]
                    relation = event[5]
                    reaction = event[6]
                    resource = event[7]

                    e_types = self.prefs.table('enemy_who')
                    causes = self.prefs.table('enemy_cause')
                    relations = self.prefs.table('enemy_hate')
                    reactions = self.prefs.table('enemy_do')
                    resources = self.prefs.table('enemy_resources')

                    e_txt = e_types.get_option(enemy_type) + ', '
                    cause_txt = causes.get_option(cause) + ', '
                    relation_txt = relations.get_option(relation) + ', '
                    reaction_txt = reactions.get_option(reaction) + ', '
                    resource_txt = resources.get_option(resource) + '.'

                    text = text + e_txt + cause_txt + relation_txt + reaction_txt + resource_txt
            elif type == '3':
                relationship = event[2]
                love_table = self.prefs.table('love_events')
                love_txt = love_table.get_option(relationship)
                text = text + love_txt
                if relationship == '1':
                    pass
                elif relationship == '2':
                    tragic_table = self.prefs.table('love_tragic')
                    mutual_feelings = self.prefs.table('love_mutual')
                    txt = tragic_table.get_option(event[3])
                    #print(len(event))
                    feelings = mutual_feelings.get_option(event[4])
                    text = text + '. ' + txt + '. ' + feelings
                elif relationship == '3':
                    problem_table = self.prefs.table('love_problems')
                    txt = problem_table.get_option(event[4])
                    text = text + '. ' + txt
                elif relationship == '4':
                    pass
                elif relationship == '5':
                    complicated_table = self.prefs.table('love_complicated')
                    txt = complicated_table.get_option(event[4])
                    text = text + '. ' + txt
            else:
                text = 'nothing happened'
            lifepath.append(str(event[0]) + ' ' + text)
        return lifepath




    def convert_from_xml(self, filepath):
        x = XmlController()
        x.load_file(filepath)

        all_tags = ['age', 'type', 'disaster_type', 'amount', 'prison_time', 'effect', 'betrayel_type', 'accident_type'
                   ,'death_type', 'accusation', 'hunter', 'corporation_type', 'complication', 'lucky_type', 'connection_type'
                  , 'friend_type', 'relation', 'reaction', 'enemy_type', 'cause', 'resources', 'love_type', 'mutual_feelings'
                 , 'tragic_type', 'problem' ]
        events = x.get_dataset('lifepath', False, False, True, tag_params=all_tags, tag_collection_with_dict=True)
        #print(str(events))
        
        #OH GOD THE HORROR 
        #print('the horror')

        
        lifepath = []
        
        for event in events:
            datakeys = []
            age = event['age']
            type = event['type']

            datakeys.append(age)

            #print('type is ' +type)

            if type == 'disaster' or type== 'lucky':
                #print('if statements for disaster and lucky')
                datakeys.append('1')
                if type == 'lucky':
                    datakeys.append('1')
                    lucky_type = str.lower(event['lucky_type'])
                    if lucky_type =='powerful connection':
                        datakeys.append('1')
                        connection = str.lower(event['connection_type'])
                        if connection=='it\'s in a local security force.':
                            datakeys.append('1')
                        elif connection=='it\'s in a local altcult leader\'s office.':
                            datakeys.append('2')
                        elif connection=='it\'s in the city mgr\'s office.':
                            datakeys.append('3')
                    elif lucky_type=='fortune':
                        datakeys.append('2')
                        amount = event['amount']
                        datakeys.append(amount)
                    elif lucky_type=='sensei':
                        datakeys.append('4')
                    elif lucky_type=='teacher':
                        datakeys.append('5')
                    elif lucky_type=='nomads':
                        datakeys.append('7')
                    elif lucky_type=='altcult contact':
                        datakeys.append('8')
                    elif lucky_type=='boostergang':
                        datakeys.append('9')
                    elif lucky_type=='combat teacher':
                        datakeys.append('10')
                elif type=='disaster':
                    datakeys.append('2')
                    disaster_type = str.lower(event['disaster_type'])

                    if disaster_type == 'debt':
                        datakeys.append('1')
                        amount = event['amount']
                        datakeys.append(amount)
                    elif disaster_type == 'prison/hostage':
                        datakeys.append('2')
                        prison_time = event['prison_time']
                        datakeys.append(prison_time)
                    elif disaster_type == 'drugs/illness':
                        datakeys.append('3')
                    elif disaster_type == 'betrayel':
                        datakeys.append('4')
                        betrayel_type = str.lower(event['betrayel_type'])

                        if betrayel_type == 'you are being blackmailed.':
                            datakeys.append('1')
                        elif betrayel_type == 'your secret was exposed':
                            datakeys.append('2')
                        elif betrayel_type == 'you were betrayed by a close friend in either romance or career (you choose).':
                            datakeys.append('3')
                    elif disaster_type == 'accident':
                        datakeys.append('5')
                        accident_type = str.lower(event['accident_type'])

                        if accident_type == 'you were terribly maimed and must subtract -2 from your dex.':
                            datakeys.append('1')
                        elif accident_type == 'you were hospitalized for x months that year.':
                            datakeys.append('2')
                        elif accident_type == 'you have lost x months of memory of that year.':
                            datakeys.append('3')
                        elif accident_type == 'you constantly relive nightmares of the accident and wake up screaming.':
                            datakeys.append('4')
                    elif disaster_type == 'death':
                        datakeys.append('6')
                        death_type = str.lower(event['death_type'])
                        if death_type == 'they died accidentally.':
                            datakeys.append('1')
                        elif death_type == 'they were murdered by unknown parties.':
                            datakeys.append('2')
                        elif death_type == 'they were murdered and you know who did it. you just need the proof.':
                            datakeys.append('3')
                    elif disaster_type == 'false accusation':
                        datakeys.append('7')
                        accu_type = str.lower(event['accusation'])
                        if accu_type == 'the accusation is theft':
                            datakeys.append('1')
                        elif accu_type == 'the accusation is cowardice':
                            datakeys.append('2')
                        elif accu_type == 'the accusation is murder':
                            datakeys.append('3')
                        elif accu_type == 'the accusation is rape':
                            datakeys.append('4')
                        elif accu_type == 'the accusation is lying or betrayel':
                            datakeys.append('5')
                    elif disaster_type == 'crime':
                        datakeys.append('8')
                        hunter = str.lower(event['hunter'])
                        if hunter == 'only a couple local renta-cops want you':
                            datakeys.append('1')
                        elif hunter == 'it\'s an entire local Security force':
                            datakeys.append('2')
                        elif hunter == 'it\'s an Altcult Militia':
                            datakeys.append('3')
                        elif hunter == 'it\'s the FBI or equivalent national police force':
                            datakeys.append('4')
                    elif disaster_type == 'corporation':
                        datakeys.append('9')
                        corp_type = str.lower(event['corporation_type'])

                        if corp_type == 'it\'s a small, local firm':
                            datakeys.append('1')
                        elif corp_type == 'it\'s a larger corp with offices Citywide':
                            datakeys.append('2')
                        elif corp_type == 'it\'s a big, national corp with agents in most major cities':
                            datakeys.append('3')
                        elif corp_type == 'it\'s a huge multinational megacorp with armies, ninja and spies everywhere':
                            datakeys.append('4')
                    elif disaster_type == 'breakdown':
                        datakeys.append('10')
                        compl = str.lower(event['complication'])
                        if compl == 'it is some type of nervous disorder, probably from a bioplague- lose 1 pt. ref':
                            datakeys.append('1')
                        if compl == 'it is some kind of mental problem; you suffer anxiety attacks and phobias. lose 1 pt from your pre stat':
                            datakeys.append('2')
                        if compl == 'it is a major psychosis. you hear voices, are violent, irrational, depressive. lose 1 pt from your pre, 1 from ref':
                            datakeys.append('3')

                    
            elif type == 'friend' or type =='enemy':
                #print('friends 4ever?')
                datakeys.append('2')
                if type == 'friend':
                    datakeys.append('1')
                    friend_type = str.lower(event['friend_type'])
                    if friend_type == 'like a big brother/sister to you':
                        datakeys.append('1')
                    elif friend_type == 'like a kid sister/brother to you':
                        datakeys.append('2')
                    elif friend_type == 'a teacher or mentor':
                        datakeys.append('3')
                    elif friend_type == 'a partner or co-worker':
                        datakeys.append('4')
                    elif friend_type == 'an old lover (choose which one)':
                        datakeys.append('5')
                    elif friend_type == 'an old enemy (choose which one)':
                        datakeys.append('6')
                    elif friend_type == 'like a foster parent to you':
                        datakeys.append('7')
                    elif friend_type == 'a relative':
                        datakeys.append('8')
                    elif friend_type == 'reconnect with an old childhood friend':
                        datakeys.append('9')
                    elif friend_type == 'met through a common interest':
                        datakeys.append('10')
                elif type == 'enemy':
                    datakeys.append('2')
                    cause = str.lower(event['cause'])
                    e_type = str.lower(event['enemy_type'])
                    relation = str.lower(event['relation'])
                    reaction = str.lower(event['reaction'])
                    resource = str.lower(event['resources'])

                    e_types = self.prefs.table('enemy_who')
                    causes = self.prefs.table('enemy_cause')
                    relations = self.prefs.table('enemy_hate')
                    reactions = self.prefs.table('enemy_do')
                    resources = self.prefs.table('enemy_resources')

                    values = [e_type, cause, relation, reaction, resource]
                    tables = [e_types, causes, relations, reactions, resources]

                    for table in tables:
                        for i in range(1, table.size()+1):
                            text = table.get_option(i)
                            for value in values:
                                if str.lower(text) == value:
                                    datakeys.append(str(i))
                                    #print('lifepath xml: ' + str.lower(text) + ' == ' + str(value))
                                else:
                                    #print('lifepath xml: ' + str.lower(text) + ' != ' + value)
                                    pass
                            #print(datakeys)

            elif type == 'love':
                datakeys.append('3')
                love_type = str.lower(event['love_type'])
                if love_type == 'happy':
                    datakeys.append('1')
                elif love_type == 'tragic love':
                    datakeys.append('2')
                    tragic_type = str.lower(event['tragic_type'])
                    mutuals = str.lower(event['mutual_feelings'])
                    tragic_table = self.prefs.table('love_tragic')

                    for i in range(1,11):
                        text = str.lower(tragic_table.get_option(i))
                        #print(text + ' == ' + tragic_type)
                        if text == tragic_type:
                            datakeys.append(str(i))

                    mutual_table = self.prefs.table('love_mutual')
                    for i in range(1, 11):
                        text = str.lower(mutual_table.get_option(i))
                        if text == mutuals:
                            datakeys.append(str(i))

                    #print(datakeys)
                    #print(event)
                elif love_type == 'with problems':
                    datakeys.append('3')
                    problem = str.lower(event['problem'])
                    problem_table = self.prefs.table('love_problems')
                    for i in range(1, 10):
                        text = str.lower(problem_table.get_option(i))
                        if text == problem:
                            datakeys.append(str(i))
                elif love_type == 'hot dates':
                    datakeys.append('4')
                elif love_type == 'complicated':
                    datakeys.append('5')
                    compl = str.lower(event['complication'])
                    comp_table = self.prefs.table('love_complicated')
                    for i in range(1, 10):
                        text = str.lower(comp_table.get_option(i))
                        if text == compl:
                            datakeys.append(str(i))          
            else:
                datakeys.append('4')
            lifepath.append(datakeys)
        self.events = lifepath
        #print(lifepath)
        return lifepath

            






