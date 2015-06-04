import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, String, Date, Text, DateTime
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/test2", echo=not True)
# engine = sqlalchemy.create_engine("postgresql://mypguser:bXlwZ3VzZXJwYXN@localhost:5466/test", echo=not True)
Base = sqlalchemy.ext.declarative.declarative_base()


class DaneFirmy(Base):
        __tablename__ = 'dane_firmy'
        id = Column(Integer, primary_key=True)
        nazwa = Column(Text, nullable=False)
        adres = Column(Text)
        zlecenia = relationship("Zlecenie")

        def __repr__(self):
            return "%i: %30s, %30s" % (self.id, self.nazwa, self.adres)


class Zlecenie(Base):
        __tablename__ = 'zlecenia'
        id = Column(Integer, primary_key=True)
        data_przyjecia = Column(DateTime, nullable=False)
        id_firmy = Column(Integer, ForeignKey('dane_firmy.id'), nullable=False)
        data_obliczenia = Column(DateTime)
        opis = Column(Text)
        zadania = relationship("Zadanie")

        def __repr__(self):
            return "%i: %s, %4i, %s" % \
                   (self.id, self.data_przyjecia.ctime(), self.id_firmy, self.data_obliczenia.ctime())


class Maszyna(Base):
        __tablename__ = 'maszyny'
        id = Column(Integer, primary_key=True)
        nazwa = Column(Text, nullable=False)
        opis = Column(Text)
        operacje = relationship("Operacja", backref='maszyny')

        def __repr__(self):
                return "%i: %s" % (self.id, self.nazwa)


class Zadanie(Base):
        __tablename__ = 'zadania'
        id = Column(Integer, primary_key=True)
        id_zlecenia = Column(Integer, ForeignKey('zlecenia.id'), nullable=False)
        operacje = relationship("Operacja")

        def __repr__(self):
                return "Id: %i, zadanie: %i" % (self.id, self.id_zadania)


class Operacja(Base):
        __tablename__ = 'operacje'
        id = Column(Integer, primary_key=True)
        id_zadanie = Column(Integer, ForeignKey('zadania.id'), nullable=False)
        id_maszyna = Column(Integer, ForeignKey('maszyny.id'), nullable=False)
        koszt = Column(Integer, nullable=False)
        permutacja = relationship("PermutacjaOperacji", backref='operacja')

        def __repr__(self):
                return "Id: %i, maszyna: %i, operacja: %i " % (self.id, self.id_maszyna, self.id_zadanie)


class PermutacjaOperacji(Base):
        __tablename__ = 'permutacja_operacje'
        id = Column(Integer, primary_key=True)
        id_operacji = Column(Integer, ForeignKey('operacje.id'), nullable=False)
        kolejnosc = Column(Integer, nullable=False)

        def __repr__(self):
                return "Id: %i, operacja: %i, optymalna pozycja: %i" % \
                       (self.id, self.id_operacja, self.kolejnosc)
