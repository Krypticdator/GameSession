from tkinter import *
from tkinter import ttk
class GUIFactory(object):
    """description of class"""
    def __init__(self):
        pass

class UIObject(object):
    def __init__(self, master, controller = 'None'):
        self.frame = ttk.Frame(master)
        self.contr = controller

class text_and_inputfield:
    def __init__(self, master, topic, width_label=15, width_num=2):
        self.frame = ttk.Frame(master)
        self.textlabel = ttk.Label(self.frame, text=topic,width=width_label)
        self.entry = ttk.Entry(self.frame, textvariable=variable, width=width_num)
        self.variable = StringVar()

        self.frame.grid(column = 0, row = 0)
        self.textlabel.grid(column=0, row=0 )
        self.entry.grid(column=1, row=0)

class entry_field(UIObject):
    def __init__(self, master, width_num=15):
        super().__init__(master)
        self.variable = StringVar()
        self.frame = ttk.Frame(master)
        self.entry = ttk.Entry(self.frame, textvariable=variable, width = width_num)


class StartMenu(object):
    def __init__(self, contr):
        self.contr = contr
        self.root = Tk()
        self.root.title('Roleplaying assistant')
        self.root.option_add('*tearOff', FALSE)

        menubar = Menu(self.root)
        self.root['menu'] = menubar

        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Tools')
        menu_file.add_command(label='Load Character', command=self.load_char)
        self.root.mainloop()

    def load_char(self):
        window = Toplevel(self.root)
        c = CharacterSheet(window, self.contr)

class CharacterSheet(object):
    def __init__(self, master, controller):
         self.frame = ttk.Frame(master)
         self.contr = controller
         contr.add_ui_component("character sheet",self)

class ModifyDvValues(UIObject):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        #self.frame = ttk.Frame(master)
        self.challenged =    text_and_inputfield(self.frame, 'easy')
        self.everyday =      text_and_inputfield(self.frame, 'everyday')
        self.competent =     text_and_inputfield(self.frame, 'challenging')
        self.heroic =        text_and_inputfield(self.frame, 'hard')
        self.incredible =    text_and_inputfield(self.frame, 'very hard')
        self.legendary =     text_and_inputfield(self.frame, 'extreme')

        self.btn_save = ttk.Button(self.frame, text='save')

        self.frame.grid(column=0, row = 0)
        self.challenged.frame.grid(column = 0, row =0)
        self.everyday.frame.grid(column = 0, row = 1)
        self.competent.frame.grid(column = 0, row = 2)
        self.heroic.frame.grid(column = 0, row = 3)
        self.incredible.frame.grid(column = 0, row = 4)
        self.legendary.frame.grid(column = 0, row = 5)

        self.btn_save.grid(column=0, row = 6)
         
      






         






