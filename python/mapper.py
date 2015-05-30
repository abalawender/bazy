import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/test", echo=not True)
#bXlwZ3VzZXJwYXNz

import sqlalchemy.ext.declarative
Base =  sqlalchemy.ext.declarative.declarative_base()

from sqlalchemy import Column, Integer, String, Date, Text

class DaneFirmy(Base):
        __tablename__ = 'dane_firmy'
        id = Column(Integer, primary_key=True)
        nazwa = Column(Text)
        adres = Column(Text)
        zadania = relationship("Zadanie")
        def __repr__(self):
            return "%i: %30s, %30s" %( self.id, self.nazwa, self.adres )

class Zadanie(Base):
        __tablename__ = 'zadania'
        id = Column(Integer, primary_key=True)
        data_przyjecia = Column(Date)
        id_firmy = Column(Integer, ForeignKey('dane_firmy.id'))
        data_obliczenia = Column(Date)
        operacje = relationship("Operacja")
        def __repr__(self):
            return "%i: %s, %4i, %s" % (self.id, self.data_przyjecia.ctime(), self.id_firmy, self.data_obliczenia.ctime() )

class Maszyna(Base):
        __tablename__ = 'maszyny'
        id = Column(Integer, primary_key=True)
        opis = Column(Text)
        relacjaOperacje = relationship('PowiazanieOperacjiZMaszyna')

        def __repr__(self):
                return "%i: %s" % (self.id, self.opis)

class Operacja(Base):
        __tablename__ = 'operacje'
        id = Column(Integer, primary_key=True)
        id_zadania=Column(Integer, ForeignKey('zadania.id'))
        powiazanieZMaszyna = relationship('PowiazanieOperacjiZMaszyna')
        def __repr__(self):
                return "Id: %i, zadanie: %i" % (self.id, self.id_zadania)

class PowiazanieOperacjiZMaszyna(Base):
        __tablename__ = 'maszyny_operacje'
        id = Column(Integer, primary_key=True)
        id_operacje = Column(Integer, ForeignKey('operacje.id'))
        id_maszyna = Column(Integer, ForeignKey('maszyny.id'))
        koszt = Column(Integer)
        def __repr__(self):
                return "Id: %i, maszyna: %i, operacja: %i " % (self.id, self.id_maszyna, self.id_operacje)

class PermutacjaOperacji(Base):
        __tablename__ = 'permutacja_operacje'
        id = Column(Integer, primary_key=True)
        id_operacja = Column(Integer)
        kolejnosc = Column(Integer)
        def __repr__(self):
                return "Id: %i, operacja: %i, optymalna pozycja: %i" % (self.id, self.id_operacja, 
self.kolejnosc)


