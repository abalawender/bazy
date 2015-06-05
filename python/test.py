import mapper
import contextlib
from mapper import *
from sqlalchemy.orm import sessionmaker
import datetime

Session = sessionmaker(bind=mapper.engine)
session = Session()
Base.metadata.bind = mapper.engine
Base.metadata.create_all()
now = datetime.datetime.now()

class SerwisBazodanowy:
    def __init__(self):
        self.session = session
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

    def DodajZlecenie(self, id_firmy, zadania_slownik):
            zlecenie = Zlecenie(data_przyjecia = now, id_firmy=id_firmy, data_obliczenia=None)
            session.add(zlecenie)
            session.flush()
            for nowe_zadanie in zadania_slownik:
                 zadanie = Zadanie(id_zlecenia = zlecenie.id)
                 session.add(zadanie)
                 session.flush()
                 for operacja in nowe_zadanie:
                        polaczenieOperacjaMaszyna = Operacja(id_zadanie=zadanie.id,
                                                             id_maszyna=operacja[0],
                                                             koszt=operacja[1])
                        session.add(polaczenieOperacjaMaszyna)
                        session.flush()

            session.commit()
            return zlecenie

    def PobierzWszystkieFirmy(self):
        return session.query (DaneFirmy)

    def PobierzFirme(self, idFirmy):
        return session.query(DaneFirmy).filter(DaneFirmy.id==idFirmy)[0]

    def PobierzZadaniaFirmy(self, idFirmy):
        return session.query(Zlecenie).filter(Zlecenie.id_firmy==idFirmy)

    def dodajFirme(self, nazwa, adres = None, haslo='qwerty'):
        firma = DaneFirmy(nazwa=nazwa, adres=adres, haslo=haslo)
        session.add(firma)
        session.flush()
        return firma

    def PobierzZlecenie(self, idZadania):
        return session.query(Zlecenie).filter(Zlecenie.id == idZadania)[0]

    def PobierzWszystkieMaszyny(self):
        return session.query(Maszyna)

    def PobierzPermutacje(self, idZlecenia):
        return session.query(PermutacjaOperacji).join(Operacja).join(Zadanie)\
            .filter(Zadanie.id_zlecenia == idZlecenia).order_by(PermutacjaOperacji.kolejnosc)

    def CzyZleceniePosortowane(self, idZlecenia):
        kwerenda = session.query(PermutacjaOperacji).join(Operacja).join(Zadanie)\
            .filter(Zadanie.id_zlecenia == idZlecenia)
        liczba_permutacji = kwerenda.count()
        return liczba_permutacji <= 0

    def PosortujZlecenie(self, idZlecenia):
        wszystkieOperacje = []
        zlecenie = self.PobierzZlecenie(idZlecenia)
        for zadanie in zlecenie.zadania:
            for operacja in zadanie.operacje:
                 wszystkieOperacje.append(operacja)

        wszystkieOperacje.sort(key=lambda oper: oper.koszt)
        kolejnosc = 1
        for operacja in wszystkieOperacje:
           permutacja = PermutacjaOperacji(id_operacji=operacja.id, kolejnosc = kolejnosc)
           kolejnosc += 1
           session.add(permutacja)
           session.flush()
        session.commit()

    def UsunZadanie(self, id_zadania):
        print('Tutaj bedzie usuwanie')

    def DodajMaszyne(self, nazwa, opis = None):
        maszyna = Maszyna(nazwa=nazwa, opis=opis)
        session.add(maszyna)
        session.flush()
        return maszyna


if __name__ == "__main__":
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        querry_rezult = con.execute('select \'drop table if exists \"\' || tablename '
                                    '|| \'\" cascade;\' from pg_tables '
                                    'where schemaname = \'public\';')
        for deleteQuerry in querry_rezult:
            con.execute(deleteQuerry[0])
        trans.commit()

    print('Tworze schemat bazy')
    Base.metadata.create_all()

    serwis = SerwisBazodanowy()
    serwis.wyswietlZawartoscWszystkichTabel()

    print('W bazie akualnie znajduje sie:')
    print('Zaczynam tworzenie przypadkowych danych:')

    nazwyFirm = ['ALIOR BANK', 'ASSECO POLAND', 'BOGDANKA',
            'BZ WBK', 'CYFROWY POLSAT', 'ENEA',
            'ENERGA', 'EUROCASH', 'KGHM POLSKA MIEDZ SA',
            'LPP', 'MBANK', 'ORANGE POLSKA', 'PEKAO',
            'PGE', 'PGNIG', 'PKN ORLEN', 'PKO BP',
            'PZU', 'SYNTHOS', 'TAURON POLSKA ENERGIA']

    firmy = []
    for nazwa in nazwyFirm:
        firmy.append(serwis.dodajFirme(nazwa=nazwa, haslo=nazwa[0:3].lower()))

    maszyny = []
    nazywyMaszyn = ['Frezarka nr 1',  'Frezarka nr 2', 'Frezarka nr 3', 'Tokarka',
                    'Wtryskarka', 'Odkurzacz', 'Myjka' ]
    for nazwaMaszyny in nazywyMaszyn:
        maszyny.append(serwis.DodajMaszyne(nazwaMaszyny))

    import random
    slownik = [[(maszyna, koszt), (maszyna, koszt) ],[(maszyna, koszt)] ]
    for firma in firmy:
        for nrOperacji in range(0, random.randint(0, 10)):
            zlecenie = []
            for nrZadania in range(0, random.randint(0, 10)):
                zadania=[]
                for nrOperacji in range(0, random.randint(0, 10)):
                    nrMaszyny = random.randint(0, len(maszyny)-1)
                    maszyna = maszyny[nrMaszyny]
                    zadania.append((maszyna.id, random.randint(0, 100)))
                zlecenie.append(zadania)
            serwis.DodajZlecenie(firma.id, zlecenie)
    serwis.wyswietlZawartoscWszystkichTabel()

