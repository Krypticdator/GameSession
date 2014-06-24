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
    def __init__(self, master, controller, label_text, label_length=10):
        super().__init__(master, controller)
        self.variable = StringVar()
        self.lbl_text = ttk.Label(self.frame, text=label_text, width=label_length)
        self.lbl_value = ttk.Label(self.frame, textvariable=self.variable)
        self.lbl_text.grid(column=0, row=0)
        self.lbl_value.grid(column = 1, row = 0)

    def set(self, value):
        self.variable.set(value)

    def get(self):
        return self.variable.get()
        

class EntryField(UIObject):
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
        menu_edit.add_command(label='Task handler', command=self.task_handler)
        self.root.mainloop()

    def load_char(self):
        window = Toplevel(self.root)
        c = CharacterSheet(window, self.contr)
    def dv_settings(self):
        window = Toplevel(self.root)
        dv = ModifyDvValues(window, self.contr)
    def task_handler(self):
        window = Toplevel(self.root)
        th = TaskHandler(window, self.contr)

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

         self.Int = label_and_value(self.mental_group, self.contr, 'Int', 5)
         self.Will = label_and_value(self.mental_group, self.contr, 'Will', 5)
         self.Pre = label_and_value(self.mental_group, self.contr, 'Pre', 5)

         #Physical group
         self.physical_frame = ttk.Labelframe(stats_group, text='Physical')
         self.physical_group = ttk.Panedwindow(self.physical_frame, orient=VERTICAL)

         self.Con = label_and_value(self.physical_group, self.contr, 'Con', 5)
         self.Str = label_and_value(self.physical_group, self.contr, 'Str', 5)
         self.Body = label_and_value(self.physical_group, self.contr, 'Body', 5)

         #Combat group
         self.combat_frame = ttk.Labelframe(stats_group, text='Combat')
         self.combat_group = ttk.Panedwindow(self.combat_frame, orient=VERTICAL)

         self.Ref = label_and_value(self.combat_group, self.contr, 'Ref', 5)
         self.Dex = label_and_value(self.combat_group, self.contr, 'Dex', 5)
         self.Tech = label_and_value(self.combat_group, self.contr, 'Tech', 5)

         #Movement
         self.movement_frame = ttk.Labelframe(stats_group, text='Movement')
         self.movement_group = ttk.Panedwindow(self.movement_frame, orient = VERTICAL)

         self.Move = label_and_value(self.movement_group, self.contr, 'Move', 5)

         #DERIVED STATS
         derived_frame = ttk.Labelframe(self.frame, text='Derived stats')
         self.Luck = label_and_value(derived_frame, self.contr, 'Luck', 5)
         self.Hum = label_and_value(derived_frame, self.contr, 'Hum', 5)
         self.Rec = label_and_value(derived_frame, self.contr, 'Rec', 5)
         self.End = label_and_value(derived_frame, self.contr, 'End', 5)

         self.Run = label_and_value(derived_frame, self.contr, 'Run', 5)
         self.Sprint = label_and_value(derived_frame, self.contr, 'Sprint', 5)
         self.Swim = label_and_value(derived_frame, self.contr, 'Swim', 5)
         self.Leap = label_and_value(derived_frame, self.contr, 'Leap', 5)

         self.Stun = label_and_value(derived_frame, self.contr, 'Stun', 5)
         self.Hits = label_and_value(derived_frame, self.contr, 'Hits', 5)
         self.Sd = label_and_value(derived_frame, self.contr, 'SD', 5)
         self.Res = label_and_value(derived_frame, self.contr, 'Res', 5)

         self.load_character()

         #SKILLS
         self.skill_frame = ttk.Labelframe(self.frame, text='Skills')
         self.skill_group = ttk.Panedwindow(self.skill_frame, orient=VERTICAL)
         skill_list = self.contr.get_char_stat_list('skill')
         self.skill_ui_components = {}

         sorted_list = []
         for key, value in skill_list.items():
             self.skill_ui_components[key] = label_and_value(self.skill_group, self.contr, key, 20)
             self.skill_ui_components[key].set(value.get_attribute('lvl'))
             sorted_list.append(key)
             #self.skill_group.add(self.skill_ui_components[key].frame)
         sorted_list.sort()

         for key in sorted_list:
             self.skill_group.add(self.skill_ui_components[key].frame)


        

         basic_stats_frame.grid(column=0, row=0)
         derived_frame.grid(column=0, row=1, sticky=(W))
         self.skill_frame.grid(column=0, row=2, sticky=(W))
         self.skill_group.grid(column=0, row=0)
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

         self.Luck.frame.grid(column=0, row=0)
         self.Hum.frame.grid(column=0, row=1)
         self.Rec.frame.grid(column=0, row=2)
         self.End.frame.grid(column=0, row=3)

         self.Run.frame.grid(column=1, row=0)
         self.Sprint.frame.grid(column=1, row=1)
         self.Swim.frame.grid(column=1, row=2)
         self.Leap.frame.grid(column=1, row=3)

         self.Stun.frame.grid(column=2, row=0)
         self.Hits.frame.grid(column=2, row=1)
         self.Sd.frame.grid(column=2, row=2)
         self.Res.frame.grid(column=2, row=3)

         self.contr.add_ui_component('character_sheet', self)


         

    def load_character(self):
        self.contr.load_character('preferences/Rasmus_Shawn Everette Slow Curve Manning.xml')
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

        Luck = self.contr.get_char_stat('luck', 'lvl')
        Hum = self.contr.get_char_stat('hum', 'lvl')
        Rec = self.contr.get_char_stat('rec', 'lvl')
        End = self.contr.get_char_stat('end', 'lvl')
        Run = self.contr.get_char_stat('run', 'lvl')
        Sprint = self.contr.get_char_stat('sprint', 'lvl')
        Swim = self.contr.get_char_stat('swim', 'lvl')
        Leap = self.contr.get_char_stat('leap', 'lvl')
        Stun = self.contr.get_char_stat('stun', 'lvl')
        Hits = self.contr.get_char_stat('hits', 'lvl')
        Sd = self.contr.get_char_stat('sd', 'lvl')
        Res = self.contr.get_char_stat('res', 'lvl')

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

        self.Luck.set(str(Luck))
        self.Hum.set(str(Hum))
        self.Rec.set(str(Rec))
        self.End.set(str(End))
        self.Run.set(str(Run))
        self.Sprint.set(str(Sprint))
        self.Swim.set(str(Swim))
        self.Leap.set(str(Leap))
        self.Stun.set(str(Stun))
        self.Hits.set(str(Hits))
        self.Sd.set(str(Sd))
        self.Res.set(str(Res))

        
         
         

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

class TaskHandler(UIObject):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        self.vertical_group = ttk.Panedwindow(self.frame, orient=VERTICAL)
        self.horizontal_group = ttk.Panedwindow(self.frame, orient=HORIZONTAL)

        self.header_group = ttk.Panedwindow(self.vertical_group, orient=HORIZONTAL)
        
        self.make_header()

        self.vertical_group.add(self.header_group)

        player_roster = self.contr.get_pc_roster()
        #player_elements_dictionary = {}
        for player, character in player_roster.items():
            player_group = ttk.Panedwindow(self.vertical_group, orient=HORIZONTAL)
            
            player_name = character.get_attribute('player')
            char_name = character.get_attribute('fname')

            lbl_player = ttk.Label(player_group, text=player_name, width=7)
            lbl_char = ttk.Label(player_group, text=char_name, width=10)
            lbl_search = ttk.Label(player_group, text = 'search',width=7)
            lbl_skill = ttk.Label(player_group, text='skill',width=6)
            lbl_bp = ttk.Label(player_group, text='bp',width=3)
            lbl_mod=ttk.Label(player_group, text='mod',width=4)
            lbl_dv=ttk.Label(player_group, text='dv', width=3)
            lbl_prob=ttk.Label(player_group, text='prob', width=5)

            player_group.add(lbl_player)
            player_group.add(lbl_char)
            player_group.add(lbl_search)
            player_group.add(lbl_skill)
            player_group.add(lbl_bp)
            player_group.add(lbl_mod)
            player_group.add(lbl_dv)
            player_group.add(lbl_prob)


            #player_group.grid(column=0, row=0)
            self.vertical_group.add(player_group)

        #self.header_group.grid(column=0, row=0)
        self.vertical_group.grid(column=0, row=0)
        self.horizontal_group.grid(column=0, row=0)

    def make_header(self):
        lbl_player = ttk.Label(self.header_group, text='player', width=7)
        lbl_char = ttk.Label(self.header_group, text='character', width=10)
        lbl_search = ttk.Label(self.header_group, text = 'search',width=7)
        lbl_skill = ttk.Label(self.header_group, text='skill',width=6)
        lbl_bp = ttk.Label(self.header_group, text='bp',width=3)
        lbl_mod=ttk.Label(self.header_group, text='mod',width=4)
        lbl_dv=ttk.Label(self.header_group, text='dv', width=3)
        lbl_prob=ttk.Label(self.header_group, text='prob', width=5)

        self.header_group.add(lbl_player)
        self.header_group.add(lbl_char)
        self.header_group.add(lbl_search)
        self.header_group.add(lbl_skill)
        self.header_group.add(lbl_bp)
        self.header_group.add(lbl_mod)
        self.header_group.add(lbl_dv)
        self.header_group.add(lbl_prob)








         






