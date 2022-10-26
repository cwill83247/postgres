from sqlalchemy import (                                                    #std
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base                     #std
from sqlalchemy.orm import sessionmaker                                     #std

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")                             #std
base = declarative_base()                                               #std  set to the declarative base class..... 

# create a class-based model for the "Programmer" table    this is the table schema so a blank template.....
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


#my attempt at creating a table and inputting infomation
class Player(base):
    __tablename__ = "Player"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    club = Column(String)
    


# instead of connecting to the database directly, we will ask for a session        #std
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)                                                          #NOTE uppercase S

# opens an actual session by calling the Session() subclass defined above          #std
session = Session()  

# creating the database using declarative_base subclass
base.metadata.create_all(db)                                                              # NOTE new variable with lowecase s 

# creating records on our Progammer table  we then need to add instance to session , and then commit that to the DB
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

chris_williams = Programmer(
    first_name="Chris",
    last_name="Williams",
    gender="M",
    nationality="British",
    famous_for="Newbie"
)

# add each instance of our programmers to our session
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)
# session.add(ada_lovelace)                 ### if you keep these sessiosn will add duplicate entries 

#players table my attempt

chris_williams = Player(
    first_name="Chris",
    last_name="Williams",
    position="midfielder",
    club="everton"
   
)

jack_williams = Player(
    first_name="Jack",
    last_name="Williams",
    position="midfielder",
    club="man utd" 
)
# session
session.add(chris_williams)    #adding records
session.add(jack_williams)

session.commit()            #commitng them to the db




# updating a single record
#programmer = session.query(Programmer).filter_by(id=7).first()     #if dont add the .first would have ot use a for loop to iterate even though only 1 record..
#programmer.famous_for = "World President"
# commit our session to the database
#session.commit()

# updating multiple records
#people = session.query(Programmer)
#for person in people:                          #NOTE indentation is important as its PYthon dont forget this !!!!!
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
if programmer is not None:
    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
         session.delete(programmer)
         session.commit()
         print("Programmer has been deleted")
    else:
         print("Programmer not deleted")
else:
    print("No records found")


#reading the data querying the databse 
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )

#reading the players data querying the databse 
players = session.query(Player)
for player in players:
    print(
        player.id,
        player.first_name + " " + player.last_name,
        player.club,
        player.position,
        sep=" | "
    )    