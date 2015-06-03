import uniwersalne
so = Session()

retVal += uniwersalne.Naglowek()
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    retVal += uniwersalne.Menu()
    retVal += uniwersalne.Zalogowany( firma )
except AttributeError:
    retVal += "Nie jestes zalgowowany"
    pass

if 'id' in parameters:
    zadanieId = parameters['id']
    retVal += "<table style='position:absolute;top:100px;'>"
    zadanie = serwis.PobierzZadanieZOperacjami(zadanieId)
    nr_zadania = 1
    for operacja in zadanie.operacje:
        retVal += "<tr><td> Zadanie: " + str(nr_zadania) + "</td><td></td></tr>"
        for powiazanieZMaszyna in operacja.powiazanieZMaszyna:
            retVal += "<tr><td></td><td> Operacja: koszt "+ str(powiazanieZMaszyna.koszt) + ", maszyna " \
            + str(powiazanieZMaszyna.maszyny.opis) + "<td></tr>"



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

    import json
    dump = json.dumps( { "data" : [ {
                "id": t[0]+1,
		"start_date": "2013-04-01 00:00:00",
		"duration": t[2],
		"text": "#%i" % t[0],
		"progress": 0,
		"sortorder": 0,
		"parent": 0,
		"open": True
        } for t in listaZadan] }, indent=4 )

    print( dump )


    # print (permutacja)
        # koszt = operacja.koszt
        # maszyny = operacja.powiazanieZMaszyna.
    # for firma in serwis.PobierzWszystkieFirmy():
    #     retVal += "<tr>"
    #     retVal += "<td><a href=firmy?id=" + str(firma.id) + ">" + firma.nazwa + "</a></td>"
    #     retVal += "</tr>"

    retVal += "<tr><td><a href=gantt?id=" + str(zadanieId) + ">Wykres gantta</a></td></tr>"
    retVal += "</table>"



retVal += uniwersalne.Stopka()
