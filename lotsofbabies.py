  GNU nano 2.2.6            File: lotsofbabies.py

###Implemeting Local file permissions-02122016
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Trader, Base, BabyItem, User

engine = create_engine('postgresql://jacob:jacob@localhost/lotsofbabies')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Beanie Lover", email="mail@citruservices.com",
             picture='http://i.imgur.com/AY0Onq9.jpg')
session.add(User1)
session.commit()

# Baby for Dollar General
trader1 = Trader(user_id=1, image="http://i.imgur.com/BppXwHU.jpg", name="Dolla$

session.add(trader1)
session.commit()

babyItem1 = BabyItem(user_id=1, image="http://i.imgur.com/FhoGDNx.jpg", name="L$
                     price="$9.99", category="TY_Classic", trader=trader1)

session.add(babyItem1)
session.commit()


babyItem2 = BabyItem(user_id=1, image="http://i.imgur.com/Uxiucvp.jpg", name="P$
                     price="$7.99", category="Peek-A-Boo", trader=trader1)

session.add(babyItem2)
session.commit()

babyItem3 = BabyItem(user_id=1, image="http://i.imgur.com/w07w0FD.jpg", name="G$
                     price="$6.99", category="Beanie_Boos", trader=trader1)

session.add(babyItem3)
session.commit()

babyItem4 = BabyItem(user_id=1, image="http://i.imgur.com/o3RyaY3.jpg", name="M$
                     price="$14.99", category="Frizzys", trader=trader1)

session.add(babyItem4)
session.commit()