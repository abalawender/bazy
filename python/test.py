import mapper
from mapper import *
from sqlalchemy.orm import sessionmaker
import datetime

Session = sessionmaker(bind=mapper.engine)
session = Session()
Base.metadata.bind = mapper.engine
Base.metadata.create_all()
now = datetime.datetime.now()

class SerwisBazodanowy:
    def wyswietlZawartoscWszystkichTabel(self):
            print( "Tabele: ", mapper.engine.table_names() )

            print( "Dane o firmach:")
            for firma in session.query(DaneFirmy):
                print( firma )

            print( "Zadania:" )
            for zadanie in session.query(Zlecenie):
                print( zadanie )

            print( "Maszyny:" )
            for maszyna in session.query(Maszyna):
                print( maszyna )

            print( "Operacje: ")
            for operacja in session.query(Zadanie):
                print( operacja )

            print( "Powiazania Operacji z Maszynami:" )
            for powiazanie in session.query( Operacja ):
                print( powiazanie )

            print ( "Zapisane permutacje:" )
            for permutacja in session.query( PermutacjaOperacji ):
                print (permutacja)

    def DodajZadanie(self, id_firmy,operacje_slownik):
            zadanie = Zlecenie(data_przyjecia = now, id_firmy=id_firmy, data_obliczenia=now)
            session.add(zadanie)
            session.flush()
            for nowa_operacja in operacje_slownik:
                 operacja = Zadanie(id_zadania = zadanie.id)
                 session.add(operacja)
                 session.flush()
                 for operacja_konkretna_maszyna in nowa_operacja:
                        polaczenieOperacjaMaszyna = Operacja(id_operacje=operacja.id, id_maszyna = operacja_konkretna_maszyna[0], koszt=operacja_konkretna_maszyna[1])
                        session.add(polaczenieOperacjaMaszyna)
                        session.flush()

            session.commit()
            return zadanie

    def PobierzWszystkieFirmy(self):
        return session.query (DaneFirmy)

    def PobierzFirme(self, idFirmy):
        return session.query(DaneFirmy).filter(DaneFirmy.id==idFirmy)[0]

    def PobierzZadaniaFirmy(self, idFirmy):
        return session.query(Zlecenie).filter(Zlecenie.id_firmy==idFirmy)

    def PobierzZadanieZOperacjami(self, idZadania):
        return session.query(Zlecenie).filter(Zlecenie.id == idZadania)[0]

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


if __name__ == "__main__":
    serwis = SerwisBazodanowy()
    serwis.wyswietlZawartoscWszystkichTabel()

