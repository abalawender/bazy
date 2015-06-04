import json
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

    listaZadan = []
    for perm in permutacja:
        kolejnosc = perm.kolejnosc
        koszt = perm.operacja.koszt
        maszyna = perm.operacja.id_maszyna
        czasRozpoczecia = perm.id*5 # liczba z dupy
        listaZadan.append((perm.id, kolejnosc, koszt, 'Kutas', czasRozpoczecia))

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
