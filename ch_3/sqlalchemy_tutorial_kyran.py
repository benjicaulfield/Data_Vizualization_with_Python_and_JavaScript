__author__ = 'Bradley'

nobel_winners = [
    {'category': 'Physics',
     'name': 'Albert Einstein',
     'nationality': 'Swiss',
     'sex': 'male',
     'year': 1921},
    {'category': 'Physics',
     'name': 'Paul Dirac',
     'nationality': 'British',
     'sex': 'male',
     'year': 1933},
    {'category': 'Chemistry',
     'name': 'Marie Curie',
     'nationality': 'Polish',
     'sex': 'female',
     'year': 1911}
]

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data/nobel_prize.db', echo=True)

Base = declarative_base()

class Winner(Base):
    __tablename__ = 'winners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))
    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>" %(self.name, self.category, self.year)

# class Winner(Base):
#     __tablename__ = 'winners'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     category = Column(String)
#     year = Column(Integer)
#     nationality = Column(String)
#     sex = Column(Enum('male', 'female'))
#
#     def __repr__(self):
#         return "<Winner(name='%s', category='%s', year='%s')>" %(self.name, self.category, self.year)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

albert = Winner(**nobel_winners[0])
session.add(albert)
session.new

session.expunge(albert)
session.new

winner_rows = [Winner(**w) for w in nobel_winners]
session.add_all(winner_rows)
session.commit()

session.query(Winner).count()

result = session.query(Winner).filter_by(nationality='Swiss')
list(result)

result = session.query(Winner).filter(\
    Winner.category == 'Physics', \
    Winner.nationality != 'Swiss')
list(result)

session.query(Winner).get(3)

res = session.query(Winner).order_by('year')
list(res)

def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop('id')
    return dat

winner_rows = session.query(Winner)
nobel_winners = [inst_to_dict(w) for w in winner_rows]

marie = session.query(Winner).get(3)
marie.nationality = 'French'
session.dirty
session.commit()
session.dirty
session.query(Winner).get(3).nationality

session.query(Winner).filter_by(name='Albert Einstein').delete()
list(session.query(Winner))

# Working with Dataset library

import dataset

db = dataset.connect('sqlite:///data/nobel_prize.db')
wtable = db['winners']
winners = wtable.find()
winners = list(winners)
winners

wtable = db['winners']
wtable.drop()

wtable = db['winners']
wtable.find()

nobel_winners = [
    {'category': 'Physics',
     'name': 'Albert Einstein',
     'nationality': 'Swiss',
     'sex': 'male',
     'year': 1921},
    {'category': 'Physics',
     'name': 'Paul Dirac',
     'nationality': 'British',
     'sex': 'male',
     'year': 1933},
    {'category': 'Chemistry',
     'name': 'Marie Curie',
     'nationality': 'Polish',
     'sex': 'female',
     'year': 1911}
]

with db as tx:
    for w in nobel_winners:
        tx['winners'].insert(w)

list(db['winners'].find())

winners = db['winners'].find()
dataset.freeze(winners, format='csv', filename='data/nobel_winners_ds.csv')
open('data/nobel_winners_ds.csv').read()

## MongoDB Tutorial
nobel_winners = [
    {'category': 'Physics',
     'name': 'Albert Einstein',
     'nationality': 'Swiss',
     'sex': 'male',
     'year': 1921},
    {'category': 'Physics',
     'name': 'Paul Dirac',
     'nationality': 'British',
     'sex': 'male',
     'year': 1933},
    {'category': 'Chemistry',
     'name': 'Marie Curie',
     'nationality': 'Polish',
     'sex': 'female',
     'year': 1911}
]

from pymongo import MongoClient

# client = MongoClient()
# db = client.nobel_prize
# coll = db.winners

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'

def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s'%(username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db_name]

db = get_mongo_database(DB_NOBEL_PRIZE)
coll = db[COLL_WINNERS]
coll.insert(nobel_winners)

res = coll.find({'category':'Chemistry'})
list(res)

res = coll.find({'year': {'$gt': 1930}})
list(res)

def mongo_coll_to_dicts(dbname='test', collname='test', query={}, del_id=True, **kw):
    db = get_mongo_database(dbname, **kw)
    res = list(db[collname].find(query))

    if del_id:
        for r in res:
            r.pop('_id')

    return res

mongo_coll_to_dicts(DB_NOBEL_PRIZE,COLL_WINNERS)

