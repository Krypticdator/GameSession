from GUIFactory import StartMenu
from Preferences import Preferences
from XmlController import XmlController
from Character import Character
class Controller(object):
    """description of class"""
    def __init__(self):
        self.__ui_components = {}
        self.prefs = Preferences()
        start = StartMenu(self)
        

    def load_character(self, filepath):
        self.c = Character(self.prefs)
        self.prefs.load_character(filepath,self.c)
        
    def get_char_stat(self, name, attribute):
        return self.c.get_stat(name, attribute)

    def get_char_stat_list(self, stat_type):
        return self.c.get_stat_list(stat_type)
        

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



