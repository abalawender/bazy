import uniwersalne
so = Session()

retVal += uniwersalne.Naglowek()
if 'id' in parameters:
    so.idFirmy = parameters['id']
    try:
        idFirmy = so.idFirmy
        firma = serwis.PobierzFirme(idFirmy)
        retVal += "<a href=firmy>Firmy</a> <a href=zadania>Zadania</a> <a href=maszyny>Maszyny</a>"

        retVal += "<div style='position:absolute;top:20px;right:20px;border: 3px dotted green; border-radius: 15px;padding:15; width:400px; text-align:center;'>"
        retVal += "Jestes zalogowny jako: " + firma.nazwa
        retVal += "<a href=wyloguj> Wyloguj </a>"
        retVal += "</div>"
    except AttributeError:
        retVal += "Nie jestes zalgowowany"
        pass

else:
    retVal += "<div style='margin-left:auto;margin-right:auto;position:relative;top:200px;border: 3px dotted green; border-radius: 25px;padding:50px; width:400px; text-align:center;'>"
    retVal += "Nie jesteś zalogowany! Wybierz użytkownika:<br /><select onChange='window.location.href=this.value' style='width:80%;'>\n"
    for firma in serwis.PobierzWszystkieFirmy():
        retVal += "\t<option value='firmy?id=" + str(firma.id) + "'>" + firma.nazwa + "</option>\n"
    retVal += "</select>"
    retVal += "</div>"

retVal += uniwersalne.Stopka()

