from GUIFactory import StartMenu
from Preferences import Preferences
from XmlController import XmlController
from SQLController import WeaponSqlController, WeaponBlueprint
from Character import Character
class Controller(object):
    """description of class"""
    def __init__(self):
        self.prefs = Preferences()
        self.__ui_components = {}
        self.__pc_roster = {}
        self.__skill_shorts = {}
        pc_filepaths = []
        #pc_filepaths.append('preferences/Rasmus_Shawn Everette Slow Curve Manning.xml')
        pc_filepaths.append('preferences/Toni_Elias Josue Ultra Arm Good.xml')
        self.load_pc_roster(pc_filepaths)

        self.prepare_skill_shorts()

        weapons = self.prefs.transfer_wpns_from_txt_to_sql()
        wpn_table=WeaponBlueprint()

        #self.__wpn_db = WeaponSqlController()

        #print(weapons)
        for weapon in weapons:
            name = str(weapon.get_attribute('name'))
            type = str(weapon.get_attribute('type'))
            wa = str(weapon.get_attribute('wa'))
            con = str(weapon.get_attribute('con'))
            av = str(weapon.get_attribute('av'))
            dmg = str(weapon.get_attribute('dmg'))
            ammo = str(weapon.get_attribute('ammo'))
            shts = str(weapon.get_attribute('shts'))
            rof = str(weapon.get_attribute('rof'))
            rel = str(weapon.get_attribute('rel'))
            range = str(weapon.get_attribute('range'))
            cost = str(weapon.get_attribute('cost'))
            wpn_table.add_wpn(name, type, wa, con, av, dmg, ammo, shts, rof, rel, range, cost)
        #wpn_table.print_table()
            

        
       

     
        start = StartMenu(self)
        
    def load_pc_roster(self, filepath_table):
        for path in filepath_table:
            c = Character(self.prefs)
            self.prefs.load_character(path, c)
            player = c.get_attribute('player')
            self.__pc_roster[player] = c
            #print(str(c))

    def load_wpn_sql_table(self):
        wpn = WeaponBlueprint()
        return wpn.query_all()

    def load_single_sql_wpn(self, name):
        wpn = WeaponBlueprint()
        return wpn.search_with_name(name)

    def update_sql_wpn(self, name, type, wa, con, av, dmg, ammo, shts, rof, rel, range, cost, weight, flags, options, alt_munitions, description, category):
        wpn_table = WeaponBlueprint()
        wpn_table.update_wpn(name, type, wa, con, av, dmg, ammo, shts, rof, rel, range, cost, weight, flags, options, alt_munitions, description, category)

    def prepare_skill_shorts(self):
        skills = self.prefs.get_skills_dictionary()

        for key, value in skills.items():
            try:
                short = value.get_attribute('short')
                name = value.get_attribute('name')
                self.__skill_shorts[short] = name
            except Exception:
                pass
    def get_skill_from_short(self, short):
        try:
            skill = self.__skill_shorts[short]
            return skill
        except Exception:
            return 'error'

    def get_pc_roster(self):
        return self.__pc_roster

    def load_character(self, filepath):
        self.c = Character(self.prefs)
        self.prefs.load_character(filepath,self.c)

    def get_player_fuz_roll(self, player, detailed=False):
        
        search_for = str.strip(player)
        return self.__pc_roster[search_for].fuz_roll(detailed)
    
            
        
    def get_char_stat(self, name, attribute, search_category=False, return_all=False):
        if search_category:
            return self.c.get_stat(name, name, True, return_all)
        return self.c.get_stat(name, attribute)
    
    def get_char_attribute(self, name):
        return self.c.get_attribute(name)

    def get_char_stat_list(self, stat_type):
        return self.c.get_stat_list(stat_type)

    def get_char_inventory(self):
        return self.c.get_inventory()

    def get_char_bp_points(self, player, skill, detailed=False):
        character = self.__pc_roster[player]
        array = []
        if detailed:
            source_stat_name = character.get_stat(skill, 'stat')
            source_stat_lvl = character.get_stat(source_stat_name, 'lvl')
            skill_lvl = character.get_stat(skill, 'lvl')
            array.append(source_stat_lvl)
            array.append(skill_lvl)
            return array
        
        bp = character.get_bpoints(skill)
        return bp
        

    def add_ui_component(self, comp_name, component):
        self.__ui_components[comp_name] = component

    def save_to_xml(self, root_name, childname, values_dict, filepath):
        x = XmlController()
        x.create_root(root_name)
        for key, value in values_dict.items():
            x.create_sub_element(childname, 'root')
            x.set_text(value, childname)
            x.set_value('type',key, childname)

        x.save_file(filepath)

    def load_from_xml(self, filename, root_name):
        x = XmlController()
        x.load_file(filename)
        return x.get_dataset(root_name, True, dict_tag_name='type')

    def calc_dv_probabilities(self, bp, dv):
        percent = self.prefs.get_probability(bp, dv)
        return percent



