import uniwersalne
so = Session()
try:
    idFirmy = so.idFirmy
    firma = serwis.PobierzFirme(idFirmy)

    retVal = """
    <!DOCTYPE html>
    <head>
            <meta http-equiv="Content-type" content="text/html; charset=utf-8">
            <title>Load data from JSON file</title>
    </head>
            <script src="/gantt/codebase/dhtmlxgantt.js" type="text/javascript" charset="utf-8"></script>
            <link rel="stylesheet" href="/gantt/codebase/dhtmlxgantt.css" type="text/css" media="screen" title="no title" charset="utf-8">
    <body>
            <style type="text/css">
                    html, body{ padding:0px; margin:0px; height:100%; }
            </style>""" + uniwersalne.Menu() + uniwersalne.Zalogowany( firma ) + \
            """
            <div id="gantt_here" style='margin-left:auto;margin-right:auto;position:relative;top:100px;width:100%; height:70%;'></div>
            <script type="text/javascript">

            //gantt.config.scale_unit = "day";
            gantt.config.scale_unit = "hour";
            gantt.config.duration_unit = "hour"
            //gantt.config.date_scale = "%l, %F %d";
            gantt.config.date_scale = "%H:%i";
            gantt.config.date_grid = "%H:%i";
            gantt.config.min_column_width = 20;

            gantt.config.scale_height = 20*3;

            gantt.templates.task_cell_class = function(task, date){
                    if(date.getHours() == 8){
                            return "day_start";
                    }
                    if(date.getHours() == 18){
                            return "day_end";
                    }
                    return "";
            };


            var weekScaleTemplate = function(date){
                    var dateToStr = gantt.date.date_to_str("%d %M");
                    var weekNum = gantt.date.date_to_str("(week %W)");
                    var endDate = gantt.date.add(gantt.date.add(date, 1, "week"), -1, "day");
                    return dateToStr(date) + " - " + dateToStr(endDate) + " " + weekNum(date);
            };

            gantt.config.subscales = [
            //	{unit:"month", step:1, date:"%F, %Y"},
                    {unit:"week", step:1, template:weekScaleTemplate},
                    {unit:"hour", step:1, date:"%G"}

            ];

            gantt.ignore_time = function(date){
                    if(date.getDay() == 0 || date.getDay() == 6)
                            return true;
                    if(date.getHours() < 8 || date.getHours() > 18)
                            return true;

                    return false;
            };
                    gantt.config.xml_date = "%Y-%m-%d %H:%i:%s";
                    gantt.init("gantt_here");
                    var query = window.location.search.replace("?","");
                    if( query.length ) query = "?"+query;
                    console.log( query );
                    gantt.load("/exec/data"+query, "json");
                    //gantt.load("/data.json", "json");
            </script>
    </body>
    """
except AttributeError:
    retVal += "<div style='margin-left:auto;margin-right:auto;position:relative;top:200px;border: 3px dotted red; background-color:rgba(250,60,10,.1); border-radius: 25px;padding:50px; width:400px; text-align:center;'>Nie jesteś zalogowany!</div"
    pass
