
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pres_model import *

engine = create_engine('sqlite:///../DATA/PRES', echo=False) # , 
     # pool_size=20, max_overflow=0)

Session = sessionmaker(bind=engine)
session = Session()

for row in session.query(President).all():
    print(row.firstname,row.lastname)
 
session2 = Session()
    
for row in session2.query(President).filter(President.lastname == 'Roosevelt'):
    print("{0.firstname} from {0.birthplace},{0.state} ({0.party})".format(row))

p = session2.query(President).filter(President.lastname=='Lincoln').one()
print(p)
print(isinstance(p,President))
p.firstname = 'Ebenezer'

# print(json.dumps(p))

session2.commit()

new_state = State('South Carolina')
session2.add(new_state)
session2.commit()

new_pres = President(45,'Colbert','Steven',None,None,'Myrtle Beach',new_state.id,None,None,22)

session2.add(new_pres)
session2.commit()

