import uniwersalne

so = Session()
retVal += uniwersalne.Naglowek()

if 'id' in parameters and 'pass' in parameters:
    idFirmy = parameters['id']
    password = parameters['pass']
    firma = serwis.PobierzFirme(idFirmy)
    if password == firma.haslo:
        so.idFirmy = idFirmy
    else:
        retVal += "<br>Bledne haslo!<br>"
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    retVal += "<script>document.location = '/exec/zlecenia';</script>"
    #retVal += uniwersalne.Menu()
    #retVal += uniwersalne.Zalogowany( firma )
except AttributeError:
    retVal += "<div style='margin-left:auto;margin-right:auto;position:relative;top:200px;border: 3px dotted red; background-color:rgba(250,60,10,.1); border-radius: 25px;padding:50px; width:400px; text-align:center;'>"
    retVal += "Nie jestes zalogowany! Wybierz uzytkownika:<br /><br /><select name=\"id\" form=\"firmy\" style='width:80%; border-radius: 5px; border: 1px solid black; background-color:rgba(250,250,250,.2); padding: 5px;'>\n"
    retVal += "<option disabled selected> -- wybierz firme -- </option>\n"
    for firma in serwis.PobierzWszystkieFirmy():
        retVal += "\t<option value='" + str(firma.id) + "'>" + firma.nazwa + "</option>\n"
    retVal += "</select>"
    retVal += "<form action=\"/exec/firmy\" id=\"firmy\" method=\"post\">" \
              "Haslo:<input type=\"password\" name=\"pass\">" \
              "<input type=\"submit\">" \
              "</form>"
    retVal += "</div>"

retVal += uniwersalne.Stopka()

