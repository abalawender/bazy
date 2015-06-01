
so = Session()

retVal = """ <html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>firma</title>
<link rel="stylesheet" type="text/css" href="/dynatable/jquery.dynatable.css" />
<!--<script src="dynatable/vendor/jquery-1.7.2.min.js"></script>-->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="/dynatable/jquery.dynatable.js"></script>
</head>
<body>
"""
if 'id' in parameters:
    so.idFirmy = parameters['id']
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    retVal += "<a href=firmy> Firmy </a>  <a href=zadania> Zadania </a>  <a href=maszyny> Maszyny </a>"
    retVal += "Jestes zalogowny jako:" + firma.nazwa
    retVal += "<a href=wyloguj> Wyloguj </a>"
except AttributeError:
    retVal += "Nie jestes zalgowowany"
    pass

retVal += "<table>"
for firma in serwis.PobierzWszystkieFirmy():
    retVal += "<tr>"
    retVal += "<td><a href=firmy?id=" + str(firma.id) + ">" + firma.nazwa + "</a></td>"
    retVal += "</tr>"

retVal += "</table> </body>"

