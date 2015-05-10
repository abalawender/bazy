import sqlalchemy
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/test", echo=not True)
#engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
print( "Tabele: ", engine.table_names() )


import sqlalchemy.ext.declarative
Base =  sqlalchemy.ext.declarative.declarative_base()

from sqlalchemy import Column, Integer, String, Date, Text

class DaneFirmy(Base):
        __tablename__ = 'dane_firmy'
        id = Column(Integer, primary_key=True)
        nazwa = Column(Text)
        adres = Column(Text)
        def __repr__(self):
            return "%i: %40s, %40s" %( self.id, self.nazwa, self.adres )

class Zadanie(Base):
        __tablename__ = 'zadania'
        id = Column(Integer, primary_key=True)
        data_przyjecia = Column(Date)
        id_firmy = Column(Integer)
        data_obliczenia = Column(Date)
        def __repr__(self):
            return "%i: %s, %4i, %s" % (self.id, self.data_przyjecia.ctime(), self.id_firmy, self.data_obliczenia.ctime() )

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

Base.metadata.bind = engine
Base.metadata.create_all()
import datetime
now = datetime.datetime.now()

firma = DaneFirmy( nazwa="Monsters Inc.", adres="USA" )
zadanie = Zadanie( data_przyjecia=now, id_firmy=1, data_obliczenia=now )

session = Session()
session.add( firma )
session.flush()
#session.commit()

print( "Dane o firmach:")
for firma in session.query(DaneFirmy):
    print( firma )

session.add( zadanie )
session.flush()
session.commit()

print( "Zadania:" )
for zadanie in session.query(Zadanie):
    print( zadanie )
