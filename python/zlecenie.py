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
        # koszt = operacja.koszt
        # maszyny = operacja.powiazanieZMaszyna.
    # for firma in serwis.PobierzWszystkieFirmy():
    #     retVal += "<tr>"
    #     retVal += "<td><a href=firmy?id=" + str(firma.id) + ">" + firma.nazwa + "</a></td>"
    #     retVal += "</tr>"
    retVal += "</table>"

retVal += uniwersalne.Stopka()
