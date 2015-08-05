import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///system.db')
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker

class dbCharacter(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer)
    full_name= Column(String)
    first_name=Column(String)
    second_name=Column(String)
    last_name=Column(String)
    alias = Column(String)
    gender = Column(String)
    age = Column(Integer)
    born = Column(String)
    origin = Column(String)
    money = Column(Integer)
    Class = Column(String)

    prime_motivation = Column(String)
    valued_person = Column(String)
    valued_posession = Column(String)
    other_people = Column(String)
    inmode = Column(String)
    exmode = Column(String)
    quirks = Column(String)
    disorders = Column(String)
    phobias = Column(String)
    clothes = Column(String)
    hair = Column(String)
    affections = Column(String)

    Int = Column(String)
    Ref = Column(String)
    Tech = Column(String)
    Dex = Column(String)
    Pre = Column(String)
    Str = Column(String)
    Con = Column(String)
    Move = Column(String)
    Body = Column(String)
    Will = Column(String)

    Luck = Column(String)
    Hum = Column(String)
    Rec = Column(String)
    End = Column(String)
    Run = Column(String)
    Sprint = Column(String)
    Leap = Column(String)
    Swim = Column(String)
    Hits = Column(String)
    Stun = Column(String)
    SD = Column(String)
    Res = Column(String)

    family_rank = Column(String)
    parents = Column(String)
    parent_event = Column(String)
    family_event = Column(String)
    childhood = Column(String)
    childhood_event = Column(String)
    family_contact = Column(String)

    flags = Column(String)
    faction = Column(Integer)
    def saveCharacter(self, Character):
        player = Character.get_attribute('player')
        fname = Character.get_attribute('fname')
        sname = Character.get_attribute('sname')
        lname = Character.get_attribute('lname')
        alias = Character.get_attribute('alias')
        full_name = fname + ' ' + sname + ' ' + alias + ' ' + lname  
        Base.metadata.create_all(engine) 
        exists=False
        for name, in self.session.query(dbCharacter.full_name).\
            filter(dbCharacter.full_name == full_name):
            exists=True
        if exists:
            pass
        else:
                
            age = Character.get_attribute('age')
            prime_motivation = Character.get_stat('prime_motivation', 'prime_motivation', True, False)
            valued_person =    Character.get_stat('most_valued_person', 'most_valued_person', True, False)
            valued_posession = Character.get_stat('most_valued_posession', 'most_valued_posession', True, False)
            other_people = Character.get_stat('feels_about_people', 'feels_about_people', True, False)
            inmode = Character.get_stat('inmode', 'inmode', True, False)
            exmode = Character.get_stat('exmode', 'exmode', True, False)

            quirks = self.convert_array(Character.get_stat('quirk', 'quirk', True, True))
            disorders = self.convert_array(Character.get_stat('disorder', 'disorder', True, True))
            phobias = self.convert_array(Character.get_stat('phobia', 'phobia', True, True))
            clothes = self.convert_array(Character.get_stat('clothes', 'clothes', True, True))
            hair = self.convert_array(Character.get_stat('hair', 'hair', True, True))
            affections = self.convert_array(Character.get_stat('affection', 'affection', True, True))

            Int =  self.convert_stat(Character.get_stat('int', 'lvl'))
            Ref =  self.convert_stat(Character.get_stat('ref', 'lvl'))
            Tech = self.convert_stat(Character.get_stat('tech', 'lvl'))
            Dex =  self.convert_stat(Character.get_stat('dex', 'lvl'))
            Pre =  self.convert_stat(Character.get_stat('pre', 'lvl'))
            Str =  self.convert_stat(Character.get_stat('str', 'lvl'))
            Con =  self.convert_stat(Character.get_stat('con', 'lvl'))
            Move = self.convert_stat(Character.get_stat('move', 'lvl'))
            Body = self.convert_stat(Character.get_stat('body', 'lvl'))
            Will = self.convert_stat(Character.get_stat('will', 'lvl'))

            Character.calc_derived_stats()

            Luck = self.convert_stat(Character.get_stat('luck', 'lvl'))
            Hum = self.convert_stat(Character.get_stat('hum', 'lvl'))
            Rec = self.convert_stat(Character.get_stat('rec', 'lvl'))
            End = self.convert_stat(Character.get_stat('end', 'lvl'))
            Run = self.convert_stat(Character.get_stat('run', 'lvl'))
            Sprint = self.convert_stat(Character.get_stat('sprint', 'lvl'))
            Leap = self.convert_stat(Character.get_stat('leap', 'lvl'))
            Swim = self.convert_stat(Character.get_stat('swim', 'lvl'))
            Hits = self.convert_stat(Character.get_stat('hits', 'lvl'))
            Stun = self.convert_stat(Character.get_stat('stun', 'lvl'))
            SD = self.convert_stat(Character.get_stat('sd', 'lvl'))
            Res = self.convert_stat(Character.get_stat('res', 'lvl'))

            family_rank = Character.get_attribute('family_rank')
            parents = Character.get_attribute('parents')
            parent_event = Character.get_attribute('parent_event')
            family_event = Character.get_attribute('family_event')
            childhood =  Character.get_attribute('childhood_enviroment')
            childhood_event = Character.get_attribute('childhood_trauma_fortune')
            family_contact = Character.get_attribute('family_contact')

            c = dbCharacter(full_name=full_name, first_name=fname, second_name=sname, last_name=lname, alias=alias,
                            age=age, prime_motivation=prime_motivation, valued_person=valued_person, valued_posession=valued_posession,
                            other_people=other_people, inmode=inmode, exmode=exmode, quirks=quirks, disorders=disorders,
                            phobias=phobias, clothes=clothes, hair=hair, affections=affections, Int=Int, Ref=Ref, Tech=Tech, Dex=Dex,
                            Pre=Pre, Str=Str, Con=Con, Move=Move, Body=Body, Will=Will, Luck=Luck, Hum=Hum, Rec=Rec, End=End, Run=Run, 
                            Sprint=Sprint, Leap=Leap, Swim=Swim, Hits=Hits, Stun=Stun, SD=SD, Res=Res, family_rank=family_rank, 
                            parents=parents, parent_event=parent_event, family_event=family_event, childhood=childhood, 
                            childhood_event=childhood_event, family_contact=family_contact)
            self.add_skills(Character, c.id)

            self.session.commit()

    def add_skills(self, Character, id):
        cskills = Character.get_stat_list('skill')
        for key, value in cskills.items():
            name = value.get_attribute('name')
            chipped = value.get_attribute('chipped')
            ip_cap = value.get_attribute('lvl')
            ip = value.get_attribute('ip')
            lvl = value.get_attribute('lvl')
            skill_id = SkillBlueprints.search_by_name(name)
            s = Skills()
            s.add(skill_id, id, chipped, ip_cap, ip, lvl)

    def add_complications(self, Character, id):
        complications = Character.get_stat_list('complication')
        for key, value in complications:
            name = value.get_attribute('name')
            intensity = value.get_attribute('intensity')
            frequency = value.get_attribute('frequency')
            importance = value.get_attribute('importance')
            c = Complications()
            c.add(id, name, intensity, frequency, importance)

            

    def convert_stat(self, stat):
        stat = str(stat)
        if stat.count('/')==1:
            pass
        else:
            stat = stat + '/' + stat
        return stat

    def convert_array(self, array):
        text = ''
        for cell in array:
            text = text + cell + ';'
        return text

    def get_by_name(self, name):
        query = self.session.query(dbCharacter).filter(dbCharacter.full_name==name)
        return query.first()



    def setSession(self, session):
        self.session = session


class WeaponBlueprint(Base):       
    __tablename__ = 'weapon_blueprints'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    wa = Column(String)
    con = Column(String)
    av = Column(String)
    dmg = Column(String)
    ammo = Column(String)
    shts = Column(String)
    rof = Column(String)
    rel = Column(String)
    range = Column(String)
    cost = Column(String)
    weight = Column(String)
    flags = Column(String)
    options = Column(String)
    alt_munitions= Column(String)
    description = Column(String)
    category = Column(String)
    source = Column(String)

    def __repr__(self):
        return "<WeaponBlueprints(name='%s', type='%s', wa='%s', con='%s', av='%s', dmg='%s', ammo='%s', shts='%s', rof='%s', rel='%s', range='%s', cost='%s', weight='%s', flags='%s', options='%s', alt_munitions='%s', description='%s', category='%s')>" % (
            self.name, self.type, self.wa, self.con, self.av, self.dmg, self.ammo, self.shts, self.rof, self.rel, self.range, self.cost, self.weight, self.flags, self.options, self.alt_munitions, self.description, self.category)

    def add_wpn(self, wpn_name, type, wa, con, av, dmg, ammo, shts, rof, rel, range, cost, weight='NA', flags='NA', options='NA', alt_munitions='NA', description='NA', category='NA', source='NA'):
        Base.metadata.create_all(engine) 
        exists=False
        for name, in self.session.query(WeaponBlueprint.name).\
            filter(WeaponBlueprint.name == wpn_name):
            exists=True
        if exists:
            pass
        else:
            wpn = WeaponBlueprint(name=wpn_name, type=type, wa=wa, con=con, av=av, dmg=dmg, ammo=ammo, shts=shts, rof=rof, rel=rel, range=range, cost=cost, weight=weight, flags=flags, options=options, alt_munitions=alt_munitions, description=description, category=category, source=source )
            self.session.add(wpn)
            self.session.commit()

    def print_table(self):
        for instance in self.session.query(WeaponBlueprint).order_by(WeaponBlueprint.id):
            print(instance.name)

    def query_all(self):
        query = self.session.query(WeaponBlueprint).order_by(WeaponBlueprint.id)
        return query.all()

    def search_with_name(self, name):
        query = self.session.query(WeaponBlueprint).filter(WeaponBlueprint.name==name)
        return query.first()

    def update_wpn(self, name, type, wa, con, av, dmg, ammo, shts, rof, rel, range, cost, weight, flags, options, alt_munitions, description, category):
        query = self.session.query(WeaponBlueprint).filter(WeaponBlueprint.name==name)
        wpn = query.first()
        wpn.name = name
        wpn.type = type
        wpn.wa = wa
        wpn.con = con
        wpn.av = av
        wpn.dmg = dmg
        wpn.ammo = ammo
        wpn.shts = shts
        wpn.rof = rof
        wpn.rel = rel
        wpn.range = range
        wpn.cost = cost
        wpn.weight = weight
        wpn.flags = flags
        wpn.options = options
        wpn.alt_munitions = alt_munitions
        wpn.description = description
        wpn.category = category
        self.session.commit()

    def setSession(self, session):
        self.session = session;
        
class SkillBlueprints(Base):
    __tablename__ = 'skill_blueprints'
    id = Column(Integer, primary_key=True)     
    name = Column(String)
    stat = Column(String)
    short = Column(String)
    diff = Column(String)
    category = Column(String)
    chip = Column(String)
    description = Column(String)
    flags = Column(String)

    def add(self, name, stat, short, diff, category, chip, description):
        exists=False
        for name, in self.session.query(SkillBlueprints.name).\
            filter(SkillBlueprints.name ==name):
            exists=True
        if exists:
            pass
        else:
            skill = SkillBlueprints(name=name, stat=stat, short=short, diff=diff, category=category, chip=chip, description=description)
            self.session.add(skill)
            self.session.commit()

    def update(self, name, stat, short, diff, category, chip, description):
        query = self.session.query(SkillBlueprints).filter(SkillBlueprints.name==name)
        skill = query.first()
        skill.name = name
        skill.stat = stat
        skill.short = short
        skill.diff = diff
        skill.category = category
        skill.chip = chip
        skill.description = description
        self.session.commit()

    def query_all(self):
        query = self.session.query(SkillBlueprints).order_by(SkillBlueprints.id)
        return query.all()
    def search_by_name(self, name):
        query =  self.session.query(SkillBlueprints).filter(SkillBlueprints.name == name)
        return query.first()
    def setSession(self, session):
        self.session = session

class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    blueprint_id = Column(Integer)
    character_id = Column(Integer)
    chipped = Column(Boolean)
    ip_cap = Column(Integer)
    ip = Column(Integer)
    lvl = Column(Integer)
    field = Column(String)
    flags = Column(String)
    cost = Column(Integer)

    def add(self, blueprint_id, character_id, chipped, ip_cap, ip, lvl, field='NA', flags='NA', cost=0, search_with_skill_name= False, search_with_char_name=False, skill_name = None, char_name = None):
        if(search_with_char_name):
            dbchar = dbCharacter.get_by_name(char_name)
            character_id = dbchar.id
        if(search_with_skill_name):
            dbskill = SkillBlueprints.search_by_name(skill_name)
            blueprint_id = dbskill.id

        for instance in self.session.query(Skills).order_by(Skills.id):
            if instance.blueprint_id==blueprint_id and character_id==instance.character_id:
                self.update(blueprint_id, character_id, chipped, ip_cap, ip, lvl, field, flags, cost)
                return

        skill = Skills(blueprint_id=blueprint_id, character_id=character_id, chipped=chipped, ip_cap=ip_cap, ip=ip, lvl=lvl, field=field, flags=flags, cost=cost)
        self.session.add(skill)
        self.session.commit()


    def update(self, blueprint_id, character_id, chipped, ip_cap, ip, lvl, field='NA', flags='NA', cost=0, skill_name = None, character_name = None):
        updated = None
        if(skill_name):
            dbskill = SkillBlueprints.search_by_name(skill_name)
            blueprint_id = dbskill.id
        if(character_name):
            dbchar = dbCharacter.get_by_name(character_name)
            character_id = dbchar.id
        for instance in self.session.query(Skills).order_by(Skills.character_id):
            if(instance.blueprint_id==blueprint_id and character_id==instance.character_id):
                updated = instance
                break
        if updated:
            updated.chipped = chipped
            updated.ip_cap = ip_cap
            updated.ip = ip
            updated.lvl = lvl
            updated.field = field
            updated.flags = flags
            updated.cost = cost
            self.session.commit()

    def get(self, name):
        skill = SkillBlueprints.search_by_name(name)
        id = skill.id
        query = self.session.query(Skills).filter(Skills.id==id)
        return query.first()

    def setSession(self, session):
        self.session = session

class Complications(Base):
    __tablename__ = 'complications'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer)
    name = Column(String)
    intensity = Column(Integer)
    frequency = Column(Integer)
    importance = Column(Integer)
    flags = Column(String)

    def setSession(self, session):
        self.session = session

    def add(self, character_id, name, intensity, frequency, importance, flags=None):
        comp = Complications(character_id=character_id, name=name, intensity=intensity, frequency=frequency, importance=importance)
        self.session.add(comp)
        self.session.commit()
    def update(self, character_id, name, intensity, frequency, importance, flags=None):
        pass
    def save(self, character_id, name, intensity, frequency, importance, flags=None):
        for comp in self.session.query(Complications).\
                filter(Complications.name==name).\
                filter(Complications.character_id ==character_id):
            comp.intensity = intensity
            comp.frequency = frequency
            comp.importance = importance
            comp.flags = flags
        self.session.commit()




class SQLController():
    """description of class"""
    def __init__(self):
        try:
            Session = sessionmaker(bind=engine)
            self.session = Session()
            Base.metadata.create_all(engine)
            self.__db = {}
            wpn = WeaponBlueprint()
            skillBP = SkillBlueprints()
            chars = dbCharacter()
            wpn.setSession(self.session)
            skillBP.setSession(self.session)
            chars.setSession(self.session)
            self.add_table('wpn_blueprints', wpn)
            self.add_table('skill_blueprints', skillBP)
            self.add_table('characters', chars)
            
             
            
        except Exception as e:
            print('error connecting to database')
            print(e)
            #self.db.close()
        finally:
            #self.db.close()
            pass
    def add_skill_to_character(self, character_name, skill_name, lvl, chipped):
        query = self.session.query(dbCharacter).filter(dbCharacter.full_name==character_name)
        character = query.first()
        query2 = self.session.query(SkillBlueprints).filter(SkillBlueprints.name==skill_name)
        skillBp = query2.first()

        blueprint_id = skillBp.id
        character_id = character.id
        skills = Skills()
        skills.add(blueprint_id, character_id, chipped, 0, 0, lvl)

    def add_character_to_database(self, character):
        c = self.table('characters')
        c.saveCharacter(character)




    def __del__(self):
        self.session.close()

    def add_table(self, name, db):
        self.__db[name] = db

    def table(self, name):
        try:
            return self.__db[name]
        except Exception as e:
            print(e)




