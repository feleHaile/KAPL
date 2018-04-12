
import datetime

from sqlalchemy import create_engine,Column, Integer, String, Date, Sequence,  ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

from pres_model import *

engine = create_engine('sqlite:///../DATA/PRES', echo=True)

months = [
    None, 
    'Jan','Feb','Mar','Apr','May','Jun',
    'Jul','Aug','Sep','Oct','Nov','Dec'
]

def mkdate(year,month,day):
    if year != "":
        m = int(months.index(month))
        d = datetime.date(int(year),m,int(day))
    else:
        d = None

    return d

Base.metadata.create_all(engine)

# returns Session function
Session = sessionmaker(bind=engine)

# make a session object
session = Session()

with open('../DATA/presidents.txt') as PRES:
    for row in PRES:
        (term_id, lastname, firstname, birth_y, birth_m, birth_d, death_y, death_m,
        death_d, birthplace, birthstate, termstart_y, termstart_m, termstart_d,
        termend_y, termend_m, termend_d, partyname) = row.split(':')

        birth = mkdate(birth_y, birth_m, birth_d)
        death = mkdate(death_y, death_m, death_d)
        termstart = mkdate(termstart_y, termstart_m, termstart_d)
        termend = mkdate(termend_y, termend_m, termend_d)

        # de-dupe
        state = State(birthstate)
        party = Party(partyname)
        session.add(state)
        session.add(party)
        
        session.commit()

        pres = President(term_id, lastname, firstname, birth, death, birthplace, 
            state.id, termstart, termend, party.id)

        session.add(pres)
        session.commit()