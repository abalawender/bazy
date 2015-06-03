
def Naglowek():
    return """<html>\n
                <head>\n
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n
                    <title>firma</title>\n
                    <link rel="stylesheet" type="text/css" href="/dynatable/jquery.dynatable.css" />\n
                    <!--<script src="dynatable/vendor/jquery-1.7.2.min.js"></script>-->\n
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>\n
                    <script src="/dynatable/jquery.dynatable.js"></script>\n
                </head>\n
                <body>\n
                """
def Zalogowany( firma ):
    return "<div style='position:absolute;top:20px;right:20px;border: 3px dotted green; border-radius: 15px;padding:15; width:400px; background-color:rgba(100,200,50,.1); text-align:center;'>\n" + \
    "Jestes zalogowny jako: " + firma.nazwa + "<a href=wyloguj> Wyloguj </a>\n" + \
    "</div>\n"

def Menu():
    return "<div style='position:absolute;top:20px;left:20px;border: 3px dotted blue; border-radius: 15px;padding:15; width:400px; background-color:rgba(10,100,250,.1); text-align:center;'>\n" + \
    "<a href=/exec/firmy>Firmy</a> <a href=/exec/zlecenia>Zlecenia</a> <a href=/exec/maszyny>Maszyny</a>\n" + \
    "</div>\n"

def Stopka():
    return "</body> </html>"
