import uniwersalne
so = Session()
retVal += uniwersalne.Naglowek()
try:
    idFirmy = so.idFirmy
    zadania = serwis.PobierzZadaniaFirmy(idFirmy)
    firma = serwis.PobierzFirme(idFirmy)
    retVal += "<a href=firmy> Firmy </a>  <a href=zadania> Zadania </a>  <a href=maszyny> Maszyny </a>"
    retVal += "Jestes zalogowny jako:" + firma.nazwa
    retVal += "<a href=wyloguj> Wyloguj </a>"
except AttributeError:
    retVal += "Nie jestes zalgowowany"
    pass

retVal += "<table>"
for zadanie in zadania:
    retVal += "<tr>"
    retVal += "<td><a href=zadanie?id=" + str(zadanie.id) + ">" + str(zadanie.id) + " " + str(zadanie.data_przyjecia)  + "</a></td>"
    retVal += "</tr></table>"
retVal += uniwersalne.Stopka()
