#engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

import mapper
from mapper import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=mapper.engine)
session = Session()


from sqlalchemy.orm import aliased
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

    def DodajZadanie(self, id_firmy,operacje_slownik):
            zadanie = Zadanie(data_przyjecia = now, id_firmy=id_firmy, data_obliczenia=now)
            session.add(zadanie)
            session.flush()
            for nowa_operacja in operacje_slownik:
                 operacja = Operacja(id_zadania = zadanie.id)
                 session.add(operacja)
                 session.flush()
                 for operacja_konkretna_maszyna in nowa_operacja:
                        polaczenieOperacjaMaszyna = PowiazanieOperacjiZMaszyna(id_operacje=operacja.id, id_maszyna = operacja_konkretna_maszyna[0], koszt=operacja_konkretna_maszyna[1])
                        session.add(polaczenieOperacjaMaszyna)
                        session.flush()

            session.commit()
            return zadanie

    def PobierzWszystkieFirmy(self):
        return session.query (DaneFirmy)

    def PobierzFirme(self, idFirmy):
        return session.query(DaneFirmy).filter(DaneFirmy.id==idFirmy)[0]

    def PobierzZadaniaFirmy(self, idFirmy):
        return session.query(Zadanie).filter(Zadanie.id_firmy==idFirmy)

    def PobierzZadanieZOperacjami(self, idZadania):
        return session.query(Zadanie).filter(Zadanie.id == idZadania)[0]

    def PobierzPosortowaneZadanie(self, idZadania):
        permutacje = []
        zadanie = self.PobierzZadanieZOperacjami(idZadania)
        for operacja in zadanie.operacje:
            for powiazanieZMaszyna in operacja.powiazanieZMaszyna:
                    permutacje.append(powiazanieZMaszyna.permutacja)

        return permutacje

    def PosortujZadanie(self, idZadania):
        powiazania = []
        zadanie = self.PobierzZadanieZOperacjami(idZadania)
        for operacja in zadanie.operacje:
            for powiazanieZMaszyna in operacja.powiazanieZMaszyna:
                 powiazania.append(powiazanieZMaszyna)

        powiazania.sort(key=lambda powiazanie: powiazanie.koszt)
        kolejnosc = 1
        for powiazanie in powiazania:
           permutacja = PermutacjaOperacji(id_maszyny_operacje = powiazanie.id, kolejnosc = kolejnosc)
           session.add(permutacja)
           session.flush()
        session.commit()

    def UsunZadanie(self, id_zadania):
        print('Tutaj bedzie usuwanie')


def Dodawanie_jakis_danych():
        firma = DaneFirmy( nazwa="Monsters Inc.", adres="USA" )

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
if __name__ == "__main__":
    Dodawanie_jakis_danych()
    serwis = SerwisBazodanowy()
    #serwis.DodajZadanie()
    serwis.WyswietlZawartoscWszystkichTabel()

