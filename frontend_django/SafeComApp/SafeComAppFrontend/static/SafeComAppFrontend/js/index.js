/*
* JS MAIN FILE
* */

function toFormatDatetime(date){
    let dateObj = new Date(date.split(' ')[0]);
    return `${dateObj.getUTCDate()}/${dateObj.getUTCMonth()}/${dateObj.getUTCFullYear()} 
    ${dateObj.getHours()}:${dateObj.getUTCMinutes()}`
}


function mapDatesListVisits(){
    let elements = document.getElementsByClassName("toFormatDatetime");
    elements = Array.from(elements); //convert to array
    elements.forEach(function(element) {
        if(element.innerText === "None"){
            element.innerText = "Sin Salida";
        }else{
            element.innerText = toFormatDatetime(element.innerText);
        }
    });
}

$(function () {
    console.log("on ready");
    $('table').DataTable();

    $(document).on("click", "#seleccionador", function (e) {
        $("#inputCedula").val($(this).closest("tr").find("td:eq(0)").text());
        $("#tablaPersonasModal").modal("hide");
    });

    mapDatesListVisits();
    /*
    *
    * new Date("2019-11-01T19:57:11.891738-06:00").getUTCMonth()
10
new Date("2019-11-01T19:57:11.891738-06:00").getUTCDate()
2
new Date("2019-11-01T19:57:11.891738-06:00").getUTCFullYear()*/

});

