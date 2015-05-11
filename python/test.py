#engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

import mapper
from mapper import *
print( "Tabele: ", mapper.engine.table_names() )


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=mapper.engine)

Base.metadata.bind = mapper.engine
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

nowa_maszyna = Maszyna(opis = "Nowa maszyna")

session.add( nowa_maszyna )
session.flush()
session.commit()

print( "Maszyny:" )
for maszyna in session.query(Maszyna):
	print( maszyna )

nowa_operacja = Operacja(koszt = 5, id_zadania = zadanie.id)
session.add( nowa_operacja)
session.flush()
session.commit()

print( "Operacje: ")
for operacja in session.query(Operacja):
	print( operacja )


print( "Powiazania Operacji z Maszynami:" )
nowe_powiazanie = PowiazanieOperacjiZMaszyna(id_operacje = nowa_operacja.id, id_maszyna = maszyna.id)
session.add(nowe_powiazanie)
session.flush()
session.commit()

for powiazanie in session.query( PowiazanieOperacjiZMaszyna ):
	print( powiazanie )

print ( "Zapisane permutacje:" )
nowe_permutacje = PermutacjaOperacji(id_operacja = nowa_operacja.id, kolejnosc = 1)
session.add(nowe_permutacje)
session.flush()
session.commit()

for permutacja in session.query( PermutacjaOperacji ):
	print (permutacja)
