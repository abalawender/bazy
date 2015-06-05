import json
import datetime
now = datetime.datetime.now()
so = Session()
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
except AttributeError:
    retVal += "Nie jestes zalgowowany"
    pass

if 'id' in parameters:
    zlecenieId = parameters['id']
    permutacja = serwis.PobierzPermutacje(zlecenieId)
    if(permutacja.count() <= 0):
        serwis.PosortujZlecenie(zlecenieId)
        permutacja = serwis.PobierzPermutacje(zlecenieId)

    maszynyOperacje = []
    slownikMaszyn = {}
    licznikSlownik = 0
    # Wrzucanie permutacje na listy symbylizujace dana maszyne
    for perm in permutacja:
        if perm.operacja.id_maszyna not in slownikMaszyn:
            slownikMaszyn[perm.operacja.id_maszyna] = licznikSlownik
            licznikSlownik += 1
            maszynyOperacje.append([])
        maszynyOperacje[slownikMaszyn[perm.operacja.id_maszyna]].append(perm)

    for maszyna in maszynyOperacje:
        czasRozpoczecia = 0
        for perm in maszyna:
            czasRozpoczecia += perm.operacja.koszt
            perm.czasRozoczecia = czasRozpoczecia

    slownikZadanieId = {}
    licznikZadan = 1
    listaZadan = []
    for perm in permutacja:
        kolejnosc = perm.kolejnosc
        koszt = perm.operacja.koszt
        if perm.operacja.id_zadanie not in slownikZadanieId:
            slownikZadanieId[perm.operacja.id_zadanie] = licznikZadan
            licznikZadan += 1
        zadanie = slownikZadanieId[perm.operacja.id_zadanie]
        maszyna = perm.operacja.maszyny.nazwa
        czasRozpoczecia = perm.czasRozoczecia # liczba z dupy
        formatCzasu = "%Y-%m-%d %H:%M:%S"
        czas = now + datetime.timedelta(hours=czasRozpoczecia)

        czasString = czas.strftime(formatCzasu)
        listaZadan.append((perm.id, kolejnosc, koszt, maszyna, czasString, zadanie))

    retVal = json.dumps({"data": [{
                "id": t[1],
		"start_date": t[4],
		"duration": t[2],
		"text": "%s Zad:%s" %(t[3], t[5]),
		"progress": 0,
		"sortorder": 0,
		"parent": 0,
		"open": True
        } for t in listaZadan] }, indent=4 )

    print( retVal )
