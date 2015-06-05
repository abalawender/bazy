import uniwersalne
so = Session()

retVal += uniwersalne.Naglowek()
zalogowany = False
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    retVal += uniwersalne.Menu()
    retVal += uniwersalne.Zalogowany( firma )
    zalogowany = True
except AttributeError:
    retVal += "Nie jestes zalgowowany"

if 'id' in parameters and zalogowany:
    zadanieId = parameters['id']
    retVal += "<div style='position:absolute;top:100px;'>"
    retVal += "<table>"
    zlecenie = serwis.PobierzZlecenie(zadanieId)
    nr_zadania = 1
    for zadanie in zlecenie.zadania:
        retVal += "<tr><td> Zadanie: " + str(nr_zadania) + "</td><td></td></tr>"
        nr_zadania += 1
        for operacja in zadanie.operacje:
            retVal += "<tr><td></td><td> Operacja: koszt "+ str(operacja.koszt) + ", maszyna " \
            + str(operacja.maszyny.nazwa) + "<td></tr>"

    retVal += "<tr><td><a href=gantt?id=" + str(zadanieId) + ">Wykres gantta</a></td></tr>"
    retVal += "</table>"


    retVal += "</div>"


retVal += uniwersalne.Stopka()
