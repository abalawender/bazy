import uniwersalne
so = Session()
retVal += uniwersalne.Naglowek()
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)
    zadania = serwis.PobierzZadaniaFirmy(idFirmy)
    retVal += uniwersalne.Menu()
    retVal += uniwersalne.Zalogowany( firma )
except AttributeError:
    retVal += "Nie jestes zalgowowany"

retVal += "<div style='position:absolute;top:100px;'>"
retVal += "<table>"
for zadanie in zadania:
    retVal += "<tr>"
    retVal += "<td><a href=zlecenie?id=" + str(zadanie.id) + ">" + str(zadanie.id) + " " + str(zadanie.data_przyjecia)  + "</a></td>"
    retVal += "</tr>"
retVal += "</table>"

retVal += """
Zdefiniuj nowa operacje<br />
<form onsubmit="return false;" id="form_id">
<p id="dupa"></p>
<input type="text" value="%s" id="firma" hidden />
<input type="text" value="koszt" id="koszt" onchange="verifyInt(this, 'koszt'); " />
<!--<input type="text" value="zadanie" id="zadanie" onchange="verifyInt(this, 'zadanie');" />-->""" % idFirmy

retVal += "<select name='maszyna'>\n"
for m in serwis.PobierzWszystkieMaszyny():
    retVal += "<option value=" + str(m.id) + " >" + m.nazwa + "</option>\n"
retVal += "</select>\n"

retVal += """
<input type="button" onclick="f = this.form; if(verifyAll(f)) { arr.push([ parseInt(f.maszyna.value), parseInt(f.koszt.value)]); dupdate(); } else alert('niepoprawne dane!');" value="dodaj" />
<input type="button" onclick="arr.splice( $('input[name=toRemove]:checked')[0].id.slice(8), 1); dupdate();" value="usun zaznaczone" />
<input type="button" onclick="send(this);" value="wyslij!" />
</form>

<script>
var arr = [];

function verifyInt( that, val ) {
    if( parseInt(that.value) > 0 ) {
        that.value = parseInt(that.value);
        return true;
    }
    else that.value = val;
    return false;
}
function verifyAll( form ) {
    return verifyInt( form.firma, "%s" ) &
        verifyInt( form.koszt, "koszt" ); 
        //verifyInt( form.zadanie, "zadanie" );
}
function dupdate() {
    var tmp = ""
    for(a in arr) tmp += '<input type=radio name="toRemove" id="toRemove' + a + '" "value=' + a + ' />' + 'operacja #' + a + ' -> ' + 'maszyna #' + arr[a][0] + ', koszt  ' + arr[a][1] + '<br />';
    document.getElementById("dupa").innerHTML = tmp;
    document.getElementById("toRemove0").checked=true;
}
function send(that) {
    var tmp = "id_firmy="+parseInt(that.form.firma.value)+"&operacje_slownik=" + JSON.stringify( [arr] );
    $.ajax({
      type: "POST",
      url: "/DodajZlecenie",
      data: tmp
      //success: success,
      //dataType: dataType
    });
    document.location = '/exec/zlecenia';
}
dupdate();
</script>
""" % idFirmy

retVal += "</div>"

retVal += uniwersalne.Stopka()
