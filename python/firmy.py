import uniwersalne
so = Session()
retVal += uniwersalne.Naglowek()

if 'id' in parameters: so.idFirmy = parameters['id']
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    retVal += uniwersalne.Menu()
    retVal += uniwersalne.Zalogowany( firma )
except AttributeError:
    retVal += "<div style='margin-left:auto;margin-right:auto;position:relative;top:200px;border: 3px dotted red; background-color:rgba(250,60,10,.1); border-radius: 25px;padding:50px; width:400px; text-align:center;'>"
    retVal += "Nie jesteś zalogowany! Wybierz użytkownika:<br /><br /><select onChange='window.location.href=this.value' style='width:80%; border-radius: 5px; border: 1px solid black; background-color:rgba(250,250,250,.2); padding: 5px;'>\n"
    retVal += "<option disabled selected> -- wybierz firmę -- </option>\n"
    for firma in serwis.PobierzWszystkieFirmy():
        retVal += "\t<option value='/exec/firmy?id=" + str(firma.id) + "'>" + firma.nazwa + "</option>\n"
    retVal += "</select>"
    retVal += "</div>"

retVal += uniwersalne.Stopka()

