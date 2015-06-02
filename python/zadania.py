import uniwersalne
so = Session()
retVal += uniwersalne.Naglowek()
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    zadania = serwis.PobierzZadaniaFirmy(idFirmy)
    retVal += "<div style='position:absolute;top:20px;left:20px;border: 3px dotted blue; border-radius: 15px;padding:15; width:400px; background-color:rgba(10,100,250,.1); text-align:center;'>\n"
    retVal += "<a href=firmy>Firmy</a> <a href=zadania>Zadania</a> <a href=maszyny>Maszyny</a>\n"
    retVal += "</div>\n"

    retVal += "<div style='position:absolute;top:20px;right:20px;border: 3px dotted green; border-radius: 15px;padding:15; width:400px; background-color:rgba(100,200,50,.1); text-align:center;'>"
    retVal += "Jestes zalogowny jako: " + firma.nazwa
    retVal += "<a href=wyloguj> Wyloguj </a>"
    retVal += "</div>"

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
