from tkinter import *
from tkinter import ttk
import decimal
class GUIFactory(object):
    """description of class"""
    def __init__(self):
        pass

class UIObject(object):
    def __init__(self, master, controller= 'None'):
        self.frame = ttk.Frame(master)
        self.contr = controller

        self.frame.grid(column=0, row=0)

class text_and_inputfield(UIObject):
    def __init__(self, master, topic, width_label=15, width_num=2, controller='None'):
        super().__init__(master, controller)
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

class TextBox(UIObject):
    def __init__(self, master, controller, header, width_num, height_num, column_num=0, row_num=0, ):
        super().__init__(master, controller)
        self.frame = ttk.LabelFrame(master, text=header)
        self.box = Text(self.frame, width=width_num, height=height_num, wrap = 'word')
        s1 = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.box.yview)
        self.box['yscrollcommand'] = s1.set
        self.frame.grid(column=column_num, row=row_num)
        self.box.grid(column = 0, row=0)
        s1.grid(column = 1, row = 0, sticky=(N,S))
    def new_text(self, text):
        self.box.delete(1.0, 'end')
        self.box.insert(1.0, text)

class CustomListBox(UIObject):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        self.box = Listbox(self.frame, height=10, width=40)
        s1 = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.box.yview)
        self.box['yscrollcommand'] = s1.set

        self.box.grid(column=0, row=0)
        s1.grid(column = 1, row = 0, sticky=(N,S))

    def add(self, text):
        self.box.insert(END, text)
        self.box.selection_set(0)

class CustomPanedWindow(UIObject):
    def __init__(self, master, controller, vertical=True):
        super().__init__(master, controller)
        self.components = {}
        if vertical:
            self.group = ttk.Panedwindow(self.frame, orient=VERTICAL)
        else:
            self.group = ttk.Panedwindow(self.frame, orient=HORIZONAL)

    def add(self, component):
        pass




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
        menu_settings.add_command(label='Skills', command=self.skill_manager)
        menu_edit.add_command(label='Task handler', command=self.task_handler)
        self.root.mainloop()

    def load_char(self):
        window = Toplevel(self.root)
        c = CharacterSheet(window, self.contr)
    def dv_settings(self):
        window = Toplevel(self.root)
        dv = ModifyDvValues(window, self.contr)
    def skill_manager(self):
        window = Toplevel(self.root)
        skills = SkillManager(window, self.contr)
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

        self.tools_group = ttk.Panedwindow(self.vertical_group, orient=HORIZONTAL)

        self.skill_var = StringVar()
        self.entry_skill = ttk.Entry(self.tools_group, textvariable=self.skill_var) 
        self.skill_var.trace('w', self.change_skill)

        self.dv_group =ttk.Panedwindow(self.tools_group, orient=VERTICAL)
        self.dv_var = StringVar()


        self.btn_roll_all = ttk.Button(self.tools_group, text='Roll all', command=self.roll_all)

        #Must bind with global dv table
        everyday = ttk.Radiobutton(self.dv_group, text='everyday', variable=self.dv_var, value=14, command=self.change_dv)
        challenging = ttk.Radiobutton(self.dv_group, text='challenging', variable=self.dv_var, value=18, command=self.change_dv)
        hard = ttk.Radiobutton(self.dv_group, text='hard', variable=self.dv_var, value=22, command=self.change_dv)
        verhard = ttk.Radiobutton(self.dv_group, text='very hard', variable=self.dv_var, value=26, command=self.change_dv)
        impossible = ttk.Radiobutton(self.dv_group, text='impossible', variable=self.dv_var, value=30, command=self.change_dv)

        self.dv_group.add(everyday)
        self.dv_group.add(challenging)
        self.dv_group.add(hard)
        self.dv_group.add(verhard)
        self.dv_group.add(impossible)

        self.tools_group.add(self.entry_skill)
        self.tools_group.add(self.dv_group)
        self.tools_group.add(self.btn_roll_all)
        self.vertical_group.add(self.tools_group)

        self.header_group = ttk.Panedwindow(self.vertical_group, orient=HORIZONTAL)
        
        self.make_header()

        self.vertical_group.add(self.header_group)

        player_roster = self.contr.get_pc_roster()
        self.player_entry_dict = {}
        for player, character in player_roster.items():
            player_group = ttk.Panedwindow(self.vertical_group, orient=HORIZONTAL)
            
            print('here player is ' +player)
            player_name = character.get_attribute('player')
            char_name = character.get_attribute('fname')

            self.player_entry_dict[player] = PlayerLine(self.vertical_group, self.contr, player_name, character)

            


            #player_group.grid(column=0, row=0)
            self.vertical_group.add(self.player_entry_dict[player].frame)

        #self.header_group.grid(column=0, row=0)
        self.vertical_group.grid(column=0, row=0)
        self.horizontal_group.grid(column=0, row=0)

    def change_dv(self, *args):
        dv = self.dv_var.get()
        for key, value in self.player_entry_dict.items():
            value.dv_var.set(dv)
    def change_skill(self, *args):
        skill = self.skill_var.get()
        for key, value in self.player_entry_dict.items():
            value.search_var.set(skill)
    def roll_all(self, *args):
        for key, value in self.player_entry_dict.items():
            value.roll()

    def make_header(self):
        lbl_player = ttk.Label(self.header_group, text='player', width=7)
        lbl_char = ttk.Label(self.header_group, text='character', width=10)
        lbl_search = ttk.Label(self.header_group, text = 'search',width=7)
        lbl_skill = ttk.Label(self.header_group, text='skill',width=6)
        lbl_bp = ttk.Label(self.header_group, text='bp',width=3)
        lbl_mod=ttk.Label(self.header_group, text='mod',width=4)
        lbl_dv=ttk.Label(self.header_group, text='dv', width=3)
        lbl_prob=ttk.Label(self.header_group, text='prob', width=5)

        lbl_roll = ttk.Label(self.header_group, text='roll', width=5)
        lbl_result = ttk.Label(self.header_group, text='result', width=20)

        self.header_group.add(lbl_player)
        self.header_group.add(lbl_char)
        self.header_group.add(lbl_search)
        self.header_group.add(lbl_skill)
        self.header_group.add(lbl_bp)
        self.header_group.add(lbl_mod)
        self.header_group.add(lbl_dv)
        self.header_group.add(lbl_prob)
        self.header_group.add(lbl_roll)
        self.header_group.add(lbl_result)

class PlayerLine(UIObject):
    def __init__(self, master, controller, player, character):
        super().__init__(master, controller)
        self.player_group = ttk.Panedwindow(self.frame, orient=HORIZONTAL)
        self.player = player
        self.character = character
        
        lbl_player = ttk.Label(self.player_group, text=player, width=7)
        lbl_char   = ttk.Label(self.player_group, text=character.get_attribute('fname'), width=10)

        self.search_var = StringVar()
        self.dv_var = StringVar()

        self.search_var.trace_variable('w',self.search_skill)
        self.dv_var.trace_variable('w',self.calc_probs)

        self.entry_search = ttk.Entry(self.player_group, width=7,textvariable=self.search_var)
        self.entry_dv     = ttk.Entry(self.player_group, width=3, textvariable=self.dv_var)

        self.skill_var = StringVar()
        self.bp_var = StringVar()
        self.mod_var = StringVar()
        self.prob_var = StringVar()
        self.result_var = StringVar()

        lbl_skill  = ttk.Label(self.player_group, textvariable=self.skill_var,width=6)
        lbl_bp     = ttk.Label(self.player_group, textvariable=self.bp_var,width=3)
        lbl_mod    = ttk.Label(self.player_group, textvariable=self.mod_var,width=4)
        
        lbl_prob   = ttk.Label(self.player_group, textvariable=self.prob_var, width=5)

        btn_roll = ttk.Button(self.player_group, text='roll', command=self.roll, width=5)
        lbl_result = ttk.Label(self.player_group, textvariable=self.result_var, width=20)

        self.player_group.add(lbl_player)
        self.player_group.add(lbl_char)
        self.player_group.add(self.entry_search)
        self.player_group.add(lbl_skill)
        self.player_group.add(lbl_bp)
        self.player_group.add(lbl_mod)
        self.player_group.add(self.entry_dv)
        self.player_group.add(lbl_prob)
        self.player_group.add(btn_roll)
        self.player_group.add(lbl_result)

        self.player_group.grid(column=0, row=0)

    def roll(self):
        fuz_set = self.contr.get_player_fuz_roll(self.player, True)
        dice_sum = sum(fuz_set)
        bp = int(self.bp_var.get())
        result = dice_sum + bp
        dv = int(self.dv_var.get())
        margin = result - dv

        if result >= dv:
            text = str(margin) + ' = ' + str(result) + '(' + str(bp) + '+' + str(dice_sum) + str(fuz_set) + ')'
            self.result_var.set(text)
            print(self.result_var.get())
        if result < dv:
            text = str(margin) + ' = ' + str(result) + '(' + str(bp) + '+' + str(dice_sum) + str(fuz_set) + ')'
            self.result_var.set(text)
            print('failure')

    def search_skill(self, *args):
        input = self.search_var.get()
        skill = self.contr.get_skill_from_short(input)
        bp = self.contr.get_char_bp_points(self.player, skill)
        self.bp_var.set(str(bp))
        self.skill_var.set(skill)
        self.calc_probs()

    def calc_probs(self, *args):
        dv = 0
        bp = 0

        try:
            dv = int(self.dv_var.get())
            bp = int(self.bp_var.get())
        except BaseException:
            pass
        percent = self.contr.calc_dv_probabilities(bp, dv)
        percent = '%.2f' % percent

        self.prob_var.set(str(percent))



class SkillManager(UIObject):
    def load_skills(self):
        self.skills = []

        for key, value in self.contr.prefs.get_skills_dictionary().items():
            self.skills.append(key)

        self.skills.sort()

        for skill in self.skills:
            self.skillslist.add(self.contr.prefs.get_skill_attribute(skill, 'name'))

    
    def __init__(self, master, controller):
        super().__init__(master, controller)
        self.skillslist = CustomListBox(self.frame, controller)
        self.edit_group = ttk.Panedwindow(self.frame, orient=VERTICAL)
        self.name = text_and_inputfield(self.edit_group, 'name', 15, 15)
        self.stat = text_and_inputfield(self.edit_group, 'stat', 6, 6)
        self.short = text_and_inputfield(self.edit_group, 'short', 6,6)
        self.category = text_and_inputfield(self.edit_group, 'category', 15, 15)
        self.description = TextBox(self.edit_group, controller, 'description', 40, 10)
        self.chippable = text_and_inputfield(self.edit_group, 'chip', 6,6)
        self.diff = text_and_inputfield(self.edit_group, 'diff', 6,6)

        self.btn_save = ttk.Button(self.frame, text='save', command=self.save)

        self.var_short_info = StringVar()

        self.short_info = ttk.Label(self.edit_group, textvariable=self.var_short_info)

        self.name.variable.trace('w', self.save_changes)
        self.stat.variable.trace('w', self.save_changes)
        self.short.variable.trace('w', self.short_changes)
        self.category.variable.trace('w', self.save_changes)
        self.chippable.variable.trace('w', self.save_changes)
        self.diff.variable.trace('w', self.save_changes)

        self.skillslist.box.bind('<<ListboxSelect>>', self.get_skill_details)

        self.edit_group.add(self.name.frame)
        self.edit_group.add(self.stat.frame)
        self.edit_group.add(self.short.frame)
        self.edit_group.add(self.category.frame)
        self.edit_group.add(self.description.frame)
        self.edit_group.add(self.chippable.frame)
        self.edit_group.add(self.diff.frame)
        self.edit_group.add(self.short_info)

        self.skillslist.frame.grid(column=0, row=0, sticky=(N, S))
        self.edit_group.grid(column=1, row=0, sticky=(E))
        self.name.frame.grid(column=0, row=0)
        self.stat.frame.grid(column=0, row=1)
        self.short.frame.grid(column=0, row=2)
        self.category.frame.grid(column=0, row=3)
        self.chippable.frame.grid(column=0, row=4)
        self.diff.frame.grid(column=0, row=5)
        self.short_info.grid(column=0, row=6)
        self.btn_save.grid(column=1, row =8)
        self.description.frame.grid(column=0,row=7)

        self.load_skills()

    def save_changes(self, *args):
        name = self.name.variable.get()
        stat = self.stat.variable.get()
        short = self.short.variable.get()
        category = self.category.variable.get()
        chip = self.chippable.variable.get()
        diff = self.diff.variable.get()
        self.contr.prefs.set_skill_attribute(name, 'name',name)
        self.contr.prefs.set_skill_attribute(name, 'stat', stat)
        self.contr.prefs.set_skill_attribute(name, 'short', short)
        self.contr.prefs.set_skill_attribute(name, 'category', category)
        self.contr.prefs.set_skill_attribute(name, 'ischippable', chip)
        self.contr.prefs.set_skill_attribute(name, 'diff', diff)

    def short_changes(self, *args):
        short = self.short.variable.get()
        print('variable short is ' + short)
        
        number_of_same = 0
        saved_short = ''
        for skill in self.skills:
            try:
                saved_short = self.contr.prefs.get_skill_attribute(skill, 'short')
            except Exception:
                saved_short = 'null'
            #print('saved short is ' + saved_short)
            if saved_short !='null':
                if short==saved_short:
                    print('saved and local short are the same')
                    number_of_same = number_of_same + 1
                    print(str(number_of_same))
                else:
                    pass
        self.var_short_info.set(str(number_of_same))
        self.save_changes()


    def get_skill_details(self, *args):
        id = self.skillslist.box.curselection()
        luku = int(id[0])
        skill = self.skillslist.box.get(luku)

        name = self.contr.prefs.get_skill_attribute(skill, 'name')
        stat = self.contr.prefs.get_skill_attribute(skill, 'stat')
        category = self.contr.prefs.get_skill_attribute(skill, 'category')
        chip = self.contr.prefs.get_skill_attribute(skill, 'ischippable')
        diff = self.contr.prefs.get_skill_attribute(skill, 'diff')
        description = self.contr.prefs.get_skill_attribute(skill, 'description')
        short = self.contr.prefs.get_skill_attribute(skill, 'short')

        self.name.variable.set(name)
        self.stat.variable.set(stat)
        self.category.variable.set(category)
        self.chippable.variable.set(chip)
        self.diff.variable.set(diff)
        self.description.new_text(description)
        self.short.variable.set(short)

    def save(self):
        self.contr.prefs.save_skills()
