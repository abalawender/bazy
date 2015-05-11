import sqlalchemy
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/Test", echo=not True)

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

class Maszyna(Base):
	__tablename__ = 'maszyny'
	id = Column(Integer, primary_key=True)
	opis = Column(Text)
	def __repr__(self):
		return "%i: %s" % (self.id, self.opis)

class Operacja(Base):
	__tablename__ = 'operacje'
	id = Column(Integer, primary_key=True)
	koszt = Column(Integer)
	id_zadania=Column(Integer)
	def __repr__(self):
		return "Id: %i, koszt: %i, zadanie: %i" % (self.id, self.koszt, self.id_zadania)

class PowiazanieOperacjiZMaszyna(Base):
	__tablename__ = 'maszyny_operacje'
	id = Column(Integer, primary_key=True)
	id_operacje = Column(Integer)
	id_maszyna = Column(Integer)
	def __repr__(self):
		return "Id: %i, maszyna: %i, operacja: %i" % (self.id, self.id_maszyna, self.id_operacje)

class PermutacjaOperacji(Base):
	__tablename__ = 'permutacja_operacje'
	id = Column(Integer, primary_key=True)
	id_operacja = Column(Integer)
	kolejnosc = Column(Integer)
	def __repr__(self):
		return "Id: %i, operacja: %i, optymalna pozycja: %i" % (self.id, self.id_operacja, 
self.kolejnosc)


