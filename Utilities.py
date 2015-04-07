from GUIFactory import UIObject
from GUIFactory import TextAndEntryfield
from tkinter import *
from tkinter import ttk
import asyncio

class SkillShortsInspector(UIObject):
    """description of class"""
    def __init__(self, master='none', controller='none'):
        if master=='none':
            self.root = Tk()
            super().__init__(self.root, controller)
        else:
            super().__init__(master, controller)
        self.skills_and_shorts = {}
     
        self.alphabetical = []
        self.ui_components = {}
        skill_blueprints = self.contr.get_all_skill_blueprints()

        for skill in skill_blueprints:
            self.skills_and_shorts[skill.name] = skill.short
            self.alphabetical.append(skill.name)
        self.alphabetical.sort()
        row_num = 0
        column_num=0
        for cell in self.alphabetical:
            skill = TextAndEntryfield(self.frame, cell, 15, 5, self.contr)
            skill.set(self.skills_and_shorts[cell])
            
            self.ui_components[cell] = skill
            skill.frame.grid(row=row_num, column = column_num, sticky=(N))
            row_num += 1
            if(row_num > 15):
                row_num = 0
                column_num += 1
        btn_check = ttk.Button(self.frame, text="check for doubles", command=self.check_for_doubles)
        btn_check.grid(column=0, row=17)
       
        #loop.close()
        self.root.mainloop()

    def check_for_doubles(self, *args):
        
        
        for skill in self.alphabetical:
            count = 0
            short = self.skills_and_shorts[skill]
            for key, value in self.ui_components.items():
                short2 = value.get()
                if short == short2:
                    count = count +1
                    if count >=2:
                        value.set(short2 + "*")
                        #self.root.update()
                



