from GUIFactory import StartMenu
from Preferences import Preferences
class Controller(object):
    """description of class"""
    def __init__(self):
        self.__ui_components = {}
        start = StartMenu(self)

    def add_ui_component(self, comp_name, component):
        self.__ui_components[comp_name] = component


