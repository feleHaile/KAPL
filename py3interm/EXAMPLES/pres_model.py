

from sqlalchemy import create_engine,Column, Integer, String, Date, Sequence,  ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()
# Base.RIMconfig = RimConfig(option,....)

print(dir(Base))

class President(Base):
    __tablename__ = 'presidents'

    term_id = Column(Integer, primary_key=True)
    lastname = Column(String(50)    )       
    firstname = Column(String(50))
    birthplace = Column(String(128))
    state = Column(Integer, ForeignKey("states.id"))    
    birthdate = Column(Date)
    deathdate = Column(Date)
    termstartdate = Column(Date)
    termenddate = Column(Date)
    party = Column(Integer, ForeignKey("parties.id"))    

    def __init__(self, term_id, lastname, firstname, birthdate,
        deathdate, birthplace, birthstate, termstartdate, termenddate, party
    ):
        self.term_id = term_id
        self.lastname = lastname       
        self.firstname = firstname
        self.birthplace = birthplace
        self.state = birthstate
        self.birthdate = birthdate
        self.deathdate = deathdate
        self.termstartdate = termstartdate
        self.termenddate = termenddate
        self.party = party

    def __repr__(self):
        return "<President('{0.term_id}','{0.lastname}', '{0.firstname}','{0.birthplace}','{0.birthdate}','{0.deathdate}','{0.termstartdate}','{0.termenddate}')>".format(self)

    def __str__(self):
        return "{0.term_id} {0.firstname} {0.lastname}".format(self)

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    state = Column(String(30))

    def __init__(self, state):
        self.state = state

    def __repr__(self):
        return "<State('{0.state}')>".format(self)

    def __str__(self):
        return "{0.state}".format(self)

class Party(Base):
    __tablename__ = 'parties'
    id = Column(Integer, primary_key=True)
    party = Column(String(64))

    def __init__(self, party):
        self.party = party

    def __repr__(self):
        return "<Party('{0.party}')>".format(self)

    def __str__(self):
        return "{0.party}".format(self)
