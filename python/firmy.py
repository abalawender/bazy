import uniwersalne
so = Session()
retVal += uniwersalne.Naglowek()

if 'id' in parameters: so.idFirmy = parameters['id']
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    retVal += "<div style='position:absolute;top:20px;left:20px;border: 3px dotted blue; border-radius: 15px;padding:15; width:400px; background-color:rgba(10,100,250,.1); text-align:center;'>\n"
    retVal += "<a href=firmy>Firmy</a> <a href=zadania>Zadania</a> <a href=maszyny>Maszyny</a>\n"
    retVal += "</div>\n"

    retVal += "<div style='position:absolute;top:20px;right:20px;border: 3px dotted green; border-radius: 15px;padding:15; width:400px; background-color:rgba(100,200,50,.1); text-align:center;'>"
    retVal += "Jestes zalogowny jako: " + firma.nazwa
    retVal += "<a href=wyloguj> Wyloguj </a>"
    retVal += "</div>"
except AttributeError:
    retVal += "<div style='margin-left:auto;margin-right:auto;position:relative;top:200px;border: 3px dotted red; background-color:rgba(250,60,10,.1); border-radius: 25px;padding:50px; width:400px; text-align:center;'>"
    retVal += "Nie jesteś zalogowany! Wybierz użytkownika:<br /><br /><select onChange='window.location.href=this.value' style='width:80%; border-radius: 5px; border: 1px solid black; background-color:rgba(250,250,250,.2); padding: 5px;'>\n"


    retVal += "<option disabled selected> -- wybierz firmę -- </option>\n"
    for firma in serwis.PobierzWszystkieFirmy():
        retVal += "\t<option value='firmy?id=" + str(firma.id) + "'>" + firma.nazwa + "</option>\n"
    retVal += "</select>"
    retVal += "</div>"

retVal += uniwersalne.Stopka()

