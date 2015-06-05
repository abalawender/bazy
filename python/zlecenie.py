import uniwersalne
so = Session()

retVal += uniwersalne.Naglowek()
zalogowany = False
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    retVal += uniwersalne.Menu()
    retVal += uniwersalne.Zalogowany( firma )
    zalogowany = True
except AttributeError:
    retVal += "Nie jestes zalgowowany"

if 'id' in parameters and zalogowany:
    zadanieId = parameters['id']
    retVal += "<div style='position:absolute;top:100px;'>"
    retVal += "<table>"
    zlecenie = serwis.PobierzZlecenie(zadanieId)
    nr_zadania = 1
    for zadanie in zlecenie.zadania:
        retVal += "<tr><td> Zlecenie: " + str(nr_zadania) + "</td><td></td></tr>"
        nr_zadania += 1
        for operacja in zadanie.operacje:
            retVal += "<tr><td></td><td> Zadanie: koszt "+ str(operacja.koszt) + ", maszyna " \
            + str(operacja.maszyny.nazwa) + "<td></tr>"

    retVal += "<tr><td><a href=gantt?id=" + str(zadanieId) + ">Wykres gantta</a></td></tr>"
    retVal += "</table>"


    retVal += """
    Zdefiniuj nową operację<br />
    <form onsubmit="return false;">
    <p id="dupa"></p>
    <input type="text" value="%s" id="firma" hidden />
    <input type="text" value="koszt" id="koszt" onchange="verifyInt(this, 'koszt'); " />
    <input type="text" value="zadanie" id="zadanie" onchange="verifyInt(this, 'zadanie');" />""" % idFirmy

    retVal += "<select name='maszyna'>\n"
    for m in serwis.PobierzWszystkieMaszyny():
        retVal += "<option value=" + str(m.id) + " >" + m.nazwa + "</option>\n"
    retVal += "</select>\n"

    retVal += """
    <input type="button" onclick="f = this.form; if(verifyAll(f)) { arr.push([f.firma.value, f.koszt.value, f.zadanie.value, f.maszyna.value]); dupdate(); } else alert('niepoprawne dane!');" value="add" />
    <input type="button" onclick="arr.splice( $('input[name=toRemove]:checked')[0].id.slice(8), 1); dupdate();" value="remove" />
    </form>

    <script>
    var arr = [];

    function verifyInt( that, val ) {
        if( parseInt(that.value) > 0 ) return true;
        else that.value = val;
        return false;
    }
    function verifyAll( form ) {
        return verifyInt( form.koszt, "koszt" ) & verifyInt( form.zadanie, "zadanie" );
    }
    function dupdate() {
        var tmp = ""
        for(a in arr) tmp += '<input type=radio name="toRemove" id="toRemove' + a + '" "value=' + a + ' />' + a + ' -> ' + arr[a] + '<br />';
        document.getElementById("dupa").innerHTML = tmp;
        document.getElementById("toRemove0").checked=true;
    }
    dupdate();
    </script>
    """
    retVal += "</div>"


retVal += uniwersalne.Stopka()
