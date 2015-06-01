import uniwersalne
so = Session()

retVal += uniwersalne.Naglowek()
try:
    idFirmy = so.idFirmy
    delattr(so, "idFirmy")
    firma = serwis.PobierzFirme(idFirmy)
    retVal += "Wylogowano:" + firma.nazwa
    retVal += "<br><a href=firmy> Kliknij, aby zalogowac się ponownie </a>"
except AttributeError:
    retVal += "Nie jestes zalgowowany!"
    pass

retVal += uniwersalne.Stopka()
