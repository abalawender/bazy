#retVal="<a href=/show/Maszyna>..</a>"
import uniwersalne
retVal = uniwersalne.Naglowek()
retVal += uniwersalne.Menu()
retVal+="""
<script>
    var url = "/show/Maszyna";
    $(location).attr('href',url);
</script>
"""
