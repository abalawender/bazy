#engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

import mapper
from mapper import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=mapper.engine)
Base.metadata.bind = mapper.engine
Base.metadata.create_all()
import datetime
now = datetime.datetime.now()

class SerwisBazodanowy:
    def WyswietlZawartoscWszystkichTabel(self):
        print( "Tabele: ", mapper.engine.table_names() )

        print( "Dane o firmach:")
        for firma in session.query(DaneFirmy):
            print( firma )

        print( "Zadania:" )
        for zadanie in session.query(Zadanie):
            print( zadanie )

        print( "Maszyny:" )
        for maszyna in session.query(Maszyna):
            print( maszyna )

        print( "Operacje: ")
        for operacja in session.query(Operacja):
            print( operacja )

        print( "Powiazania Operacji z Maszynami:" )
        for powiazanie in session.query( PowiazanieOperacjiZMaszyna ):
            print( powiazanie )

        print ( "Zapisane permutacje:" )
        for permutacja in session.query( PermutacjaOperacji ):
            print (permutacja)

        #    def DodajZadanie(self, id_firmy, operacje):
        #            zadanie = Zadanie(data_przyjecia = now, id_firmy=id_firmy)
        #            session.add(zadanie)
        #            session.flush()
        #            
        #            operacje_slownik = [ {1 : 7, 2 : 5}, {1:2, 2:4}]  
        #
        #            for nowa_operacja in operacje_slownik:
        #                 operacja = Operacja(zadanie.id)
        #                 session.add(operacja)
        #                 session.flush()
        #                 for operacja_konkretna_maszyna in nowa_operacja:
        #                        polaczenieOperacjaMaszyna = PowiazanieOperacjiZMaszyna(id_operacje=operacja.id, id_maszyna = operacja_konkretna_maszyna.
        #
        #
        #                session.add( Operacja(id_zadania = zadanie.id)
        #                session.flush()
        #                session
    def DodajZadanie(self):
        print("Tu bedzie dodawanie zadan")


serwis = SerwisBazodanowy()
firma = DaneFirmy( nazwa="Monsters Inc.", adres="USA" )

session = Session()
session.add( firma )
session.flush()

zadanie = Zadanie( data_przyjecia=now, id_firmy=firma.id, data_obliczenia=now )
session.add( zadanie )
session.flush()

nowa_maszyna = Maszyna(opis = "Nowa maszyna")

session.add( nowa_maszyna )
session.flush()

nowa_operacja = Operacja(id_zadania = zadanie.id)
session.add( nowa_operacja)
session.flush()

nowe_powiazanie = PowiazanieOperacjiZMaszyna(id_operacje = nowa_operacja.id, id_maszyna = nowa_maszyna.id, koszt = 5)
session.add(nowe_powiazanie)
session.flush()

nowe_permutacje = PermutacjaOperacji(id_operacja = nowa_operacja.id, kolejnosc = 1)
session.add(nowe_permutacje)
session.flush()
session.commit()

serwis = SerwisBazodanowy()
serwis.WyswietlZawartoscWszystkichTabel()
