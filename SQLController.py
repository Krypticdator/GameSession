import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///masterdb.db')
Base = declarative_base()

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

class dbCharacter(Base):
    __tablename__ = 'character'
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

    def addCharacter(self, Character):
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
            SD = self.convert_stat(Character.get_stat('SD', 'lvl'))
            Res = self.convert_stat(Character.get_stat('res', 'lvl'))

            

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
        
         

class SQLController():
    """description of class"""
    def __init__(self):
        try:
            Session = sessionmaker(bind=engine)
            self.session = Session()
            Base.metadata.create_all(engine)
            self.__db = {}
            wpn = WeaponBlueprint()
            wpn.setSession(self.session)
            self.add_table('wpn_blueprints', wpn)
            
             
            
        except Exception as e:
            print('error connecting to database: ' +database)
            print(e)
            #self.db.close()
        finally:
            #self.db.close()
            pass
    def __del__(self):
        self.session.close()

    def add_table(self, name, db):
        self.__db[name] = db

    def table(self, name):
        try:
            return self.__db[name]
        except Exception as e:
            print(e)




