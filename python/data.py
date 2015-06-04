import json
so = Session()
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
except AttributeError:
    retVal += "Nie jestes zalgowowany"
    pass

if 'id' in parameters:
    zadanieId = parameters['id']
    zadanie = serwis.PobierzZadanieZOperacjami(zadanieId)
    nr_zadania = 1
    permutacja = serwis.PobierzPosortowaneZadanie(zadanieId)[0]
    if(len(permutacja) == 0):
        serwis.PosortujZadanie(zadanieId)
        permutacja = serwis.PobierzPosortowaneZadanie(zadanieId)[0]

    listaZadan = []
    for operacja in permutacja:
        kolejnosc = operacja.kolejnosc
        koszt = operacja.Powiazanie.koszt
        maszyna = operacja.Powiazanie.id_maszyna
        czasRozpoczecia = operacja.id*5 # liczba z dupy
        listaZadan.append((operacja.id, kolejnosc, koszt, maszyna, czasRozpoczecia))

    retVal = json.dumps({"data": [{
                "id": t[0]+1,
		"start_date": "2013-04-01 00:00:00",
		"duration": t[2],
		"text": "#%i" % t[0],
		"progress": 0,
		"sortorder": 0,
		"parent": 0,
		"open": True
        } for t in listaZadan] }, indent=4 )

    print( retVal )
