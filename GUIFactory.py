from tkinter import *
from tkinter import ttk
class GUIFactory(object):
    """description of class"""
    def __init__(self):
        pass

class UIObject(object):
    def __init__(self, master, controller= 'None'):
        self.frame = ttk.Frame(master)
        self.contr = controller

        self.frame.grid(column=0, row=0)

class text_and_inputfield:
    def __init__(self, master, topic, width_label=15, width_num=2):
        self.variable = StringVar()
        self.frame = ttk.Frame(master)
        self.textlabel = ttk.Label(self.frame, text=topic,width=width_label)
        self.entry = ttk.Entry(self.frame, textvariable=self.variable, width=width_num)
        

        self.frame.grid(column = 0, row = 0)
        self.textlabel.grid(column=0, row=0 )
        self.entry.grid(column=1, row=0)

class label_and_value(UIObject):
    def __init__(self, master, controller, label_text):
        super().__init__(master, controller)
        self.variable = StringVar()
        self.lbl_text = ttk.Label(self.frame, text=label_text)
        self.lbl_value = ttk.Label(self.frame, textvariable=self.variable)
        self.lbl_text.grid(column=0, row=0)
        self.lbl_value.grid(column = 1, row = 0)

    def set(self, value):
        self.variable.set(value)

    def get(self):
        return self.variable.get()
        

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
        menu_settings = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Tools')
        menubar.add_cascade(menu=menu_settings, label='Settings')
        menu_file.add_command(label='Load Character', command=self.load_char)
        menu_settings.add_command(label='DV table', command=self.dv_settings)
        self.root.mainloop()

    def load_char(self):
        window = Toplevel(self.root)
        c = CharacterSheet(window, self.contr)
    def dv_settings(self):
        window = Toplevel(self.root)
        dv = ModifyDvValues(window, self.contr)

class CharacterSheet(UIObject):
    def __init__(self, master, controller):
         super().__init__(master, controller)
         self.contr.add_ui_component("character sheet",self)

         #BASIC STATS
         basic_stats_frame = ttk.Labelframe(self.frame, text='Primary stats')
         stats_group = ttk.Panedwindow(basic_stats_frame, orient = HORIZONTAL)
        
         #Mental group
         self.mental_frame = ttk.Labelframe(stats_group, text='Mental')
         self.mental_group = ttk.Panedwindow(self.mental_frame, orient=VERTICAL)

         self.Int = label_and_value(self.mental_group, self.contr, 'Int')
         self.Will = label_and_value(self.mental_group, self.contr, 'Will')
         self.Pre = label_and_value(self.mental_group, self.contr, 'Pre')

         #Physical group
         self.physical_frame = ttk.Labelframe(stats_group, text='Physical')
         self.physical_group = ttk.Panedwindow(self.physical_frame, orient=VERTICAL)

         self.Con = label_and_value(self.physical_group, self.contr, 'Con')
         self.Str = label_and_value(self.physical_group, self.contr, 'Str')
         self.Body = label_and_value(self.physical_group, self.contr, 'Body')

         #Combat group
         self.combat_frame = ttk.Labelframe(stats_group, text='Combat')
         self.combat_group = ttk.Panedwindow(self.combat_frame, orient=VERTICAL)

         self.Ref = label_and_value(self.combat_group, self.contr, 'Ref')
         self.Dex = label_and_value(self.combat_group, self.contr, 'Dex')
         self.Tech = label_and_value(self.combat_group, self.contr, 'Tech')

         #Movement
         self.movement_frame = ttk.Labelframe(stats_group, text='Movement')
         self.movement_group = ttk.Panedwindow(self.movement_frame, orient = VERTICAL)

         self.Move = label_and_value(self.movement_group, self.contr, 'Move')

        

         basic_stats_frame.grid(column=0, row=0)
         stats_group.grid(column=0, row=0)
         self.mental_frame.grid(column=0, row=0)
         self.mental_group.grid(column=0, row=0)
         self.physical_frame.grid(column=0, row=0)
         self.physical_group.grid(column=0, row=0)
         self.combat_frame.grid(column=0, row=0)
         self.combat_group.grid(column=0, row=0)
         self.movement_frame.grid(column=0, row=0)
         self.movement_group.grid(column=0, row=0)

         stats_group.add(self.mental_frame)
         stats_group.add(self.physical_frame)
         stats_group.add(self.combat_frame)
         stats_group.add(self.movement_frame)

         self.mental_group.add(self.Int.frame)
         self.mental_group.add(self.Will.frame)
         self.mental_group.add(self.Pre.frame)

         self.physical_group.add(self.Con.frame)
         self.physical_group.add(self.Str.frame)
         self.physical_group.add(self.Body.frame)

         self.combat_group.add(self.Ref.frame)
         self.combat_group.add(self.Dex.frame)
         self.combat_group.add(self.Tech.frame)

         self.movement_group.add(self.Move.frame)

         self.contr.add_ui_component('character_sheet', self)
         #self.frame.pack()

         self.load_character()

    def load_character(self):
        self.contr.load_character('null')
        Int  = self.contr.get_char_stat('int','lvl')
        Will  = self.contr.get_char_stat('will','lvl')
        Pre  = self.contr.get_char_stat('pre','lvl')
        Con= self.contr.get_char_stat('con','lvl')
        Str= self.contr.get_char_stat('str','lvl')
        Body= self.contr.get_char_stat('body','lvl')
        Ref= self.contr.get_char_stat('ref','lvl')
        Dex= self.contr.get_char_stat('dex','lvl')
        Tech= self.contr.get_char_stat('tech','lvl')
        Move= self.contr.get_char_stat('move','lvl')

        self.Int.set(str(Int))
        self.Ref.set(str(Ref))
        self.Tech.set(str(Tech))
        self.Dex.set(str(Dex))
        self.Pre.set(str(Pre))
        self.Con.set(str(Con))
        self.Str.set(str(Str))
        self.Move.set(str(Move))
        self.Body.set(str(Body))
        self.Will.set(str(Will))

        
         
         

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

        self.btn_save = ttk.Button(self.frame, text='save', command=self.save)

        self.frame.grid(column=0, row = 0)
        self.challenged.frame.grid(column = 0, row =0)
        self.everyday.frame.grid(column = 0, row = 1)
        self.competent.frame.grid(column = 0, row = 2)
        self.heroic.frame.grid(column = 0, row = 3)
        self.incredible.frame.grid(column = 0, row = 4)
        self.legendary.frame.grid(column = 0, row = 5)

        self.btn_save.grid(column=0, row = 6)
        self.load()
       
    def save(self):
        easy = self.challenged.variable.get()
        everyday = self.everyday.variable.get()
        challenging = self.competent.variable.get()
        hard = self.heroic.variable.get()
        incredible = self.incredible.variable.get()
        extreme  =self.legendary.variable.get()

        dict = {}
        dict['easy'] = easy
        dict['everyday'] = everyday
        dict['challenging'] = challenging
        dict['hard'] = hard
        dict['incredible'] = incredible
        dict['extreme'] = extreme

        self.contr.save_to_xml('dvalues','dv', dict, 'preferences/dv.xml')

    def load(self):
        dict = self.contr.load_from_xml('preferences/dv.xml', 'dvalues')
       
        self.challenged.variable.set(str(dict['easy']))
        self.everyday.variable.set(str(dict['everyday']))
        self.competent.variable.set(str(dict['challenging']))
        self.heroic.variable.set(str(dict['hard']))
        self.incredible.variable.set(str(dict['incredible']))
        self.legendary.variable.set(str(dict['extreme']))






         






