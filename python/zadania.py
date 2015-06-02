import uniwersalne
so = Session()
retVal += uniwersalne.Naglowek()
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    zadania = serwis.PobierzZadaniaFirmy(idFirmy)
    retVal += uniwersalne.Menu()
    retVal += uniwersalne.Zalogowany( firma )

    retVal += "<table style='position:absolute;top:100px;'>"
    for zadanie in zadania:
        retVal += "<tr>"
        retVal += "<td><a href=zadanie?id=" + str(zadanie.id) + ">" + str(zadanie.id) + " " + str(zadanie.data_przyjecia)  + "</a></td>"
        retVal += "</tr>"
    retVal += "</table>"
except AttributeError:
    retVal += "Nie jestes zalgowowany"
    pass

retVal += uniwersalne.Stopka()
