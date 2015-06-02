import uniwersalne
so = Session()

retVal += uniwersalne.Naglowek()
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    retVal += "<a href=firmy> Firmy </a>  <a href=zadania> Zadania </a>  <a href=maszyny> Maszyny </a>"
    retVal += "Jestes zalogowny jako:" + firma.nazwa
    retVal += "<a href=wyloguj> Wyloguj </a>"
except AttributeError:
    retVal += "Nie jestes zalgowowany"
    pass

if 'id' in parameters:
    zadanieId = parameters['id']
    retVal += "<table>"
    # zadanie = serwis.PobierzZadanieZOperacjami(zadanieId)
    # for operacja in zadanie.operacje:
        # koszt = operacja.koszt
        # maszyny = operacja.powiazanieZMaszyna.
    # for firma in serwis.PobierzWszystkieFirmy():
    #     retVal += "<tr>"
    #     retVal += "<td><a href=firmy?id=" + str(firma.id) + ">" + firma.nazwa + "</a></td>"
    #     retVal += "</tr>"
    retVal += "</table>"

retVal += uniwersalne.Stopka()
