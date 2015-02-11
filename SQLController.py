import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///masterdb.db')
Base = declarative_base()

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
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

    def __repr__(self):
        return "<WeaponBlueprints(name='%s', type='%s', wa='%s', con='%s', av='%s', dmg='%s', ammo='%s', shts='%s', rof='%s', rel='%s', range='%s', cost='%s', weight='%s', flags='%s', options='%s', alt_munitions='%s', description='%s', category='%s')>" % (
            self.name, self.type, self.wa, self.con, self.av, self.dmg, self.ammo, self.shts, self.rof, self.rel, self.range, self.cost, self.weight, self.flags, self.options, self.alt_munitions, self.description, self.category)

    def add_wpn(self, wpn_name, type, wa, con, av, dmg, ammo, shts, rof, rel, range, cost, weight='NA', flags='NA', options='NA', alt_munitions='NA', description='NA', category='NA'):
        Base.metadata.create_all(engine) 
        Session = sessionmaker(bind=engine)
        session = Session()
        exists=False
        for name, in session.query(WeaponBlueprint.name).\
            filter(WeaponBlueprint.name == wpn_name):
            exists=True
        if exists:
            pass
        else:
            wpn = WeaponBlueprint(name=wpn_name, type=type, wa=wa, con=con, av=av, dmg=dmg, ammo=ammo, shts=shts, rof=rof, rel=rel, range=range, cost=cost, weight=weight, flags=flags, options=options, alt_munitions=alt_munitions, description=description, category=category )
            session.add(wpn)
            session.commit()

    def print_table(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        for instance in session.query(WeaponBlueprint).order_by(WeaponBlueprint.id):
            print(instance.name)

    def query_all(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(WeaponBlueprint).order_by(WeaponBlueprint.id)
        return query.all()

    def search_with_name(self, name):
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(WeaponBlueprint).filter(WeaponBlueprint.name==name)
        return query.first()

    def update_wpn(self, name, type, wa, con, av, dmg, ammo, shts, rof, rel, range, cost, weight, flags, options, alt_munitions, description, category):
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(WeaponBlueprint).filter(WeaponBlueprint.name==name)
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
        session.commit()
        
         

class SQLController():
    """description of class"""
    def __init__(self, database):
        try:
            parameter = 'sqlite:///' + database
            
            #self.db = sqlite3.connect(database)
            #self.__database_name = database
        except Exception as e:
            print('error connecting to database: ' +database)
            print(e)
            #self.db.close()
        finally:
            #self.db.close()
            pass





