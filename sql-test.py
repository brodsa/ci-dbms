from sqlalchemy import (
    create_engine, String, Column, Float, Integer
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

class People(base):
    __tablename__ = "People"
    PeopleId = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


addPerson = People(
    first_name="Test",
    last_name="Test"

)
    

# session.add(addPerson)
# session.commit()

persons = session.query(People)
for person in persons:
    print(person.PeopleId, person.first_name, person.last_name, sep=' | ')


person_id1 = session.query(People).filter_by(PeopleId=5).first()
# person_id1.first_name = "Alois"
# person_id1.last_name = "Lion"
# session.commit()
print(person_id1.first_name)

