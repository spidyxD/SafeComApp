/*
* JS MAIN FILE TO IMPROVE JAJA
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

function mapDatesListVisitsEdit(){
    let elements = document.getElementsByClassName("toFormatDatetime");
    elements = Array.from(elements); //convert to array
    elements.forEach(function(element) {
        if(element.value === "None"){
            element.value = "Sin Salida";
        }else{
            element.value = toFormatDatetime(element.value);
        }
    });
}

$(function () {
    console.log("on ready");
    $('table').DataTable();

    $(document).on("click", "#seleccionador", function (e) {
        $("#inputCedula").val($(this).closest("tr").find("td:eq(0)").text());
        $("#inputName").val($(this).closest("tr").find("td:eq(1)").text());
        $("#inputPrimerApe").val($(this).closest("tr").find("td:eq(2)").text());
        $("#inputSegundoApe").val($(this).closest("tr").find("td:eq(3)").text());
        $("#tablaPersonasModal").modal("hide");
    });

    $(document).on("click", "#seleccionadorVehicle", function (e) {

        $("#inputPlaca").val($(this).closest("tr").find("td:eq(0)").text());
        $("#inputMarca").val($(this).closest("tr").find("td:eq(1)").text());
        $("#inputModelo").val($(this).closest("tr").find("td:eq(2)").text());
        $("#inputColor").val($(this).closest("tr").find("td:eq(3)").text());
        $("#inputCedula").val($(this).closest("tr").find("td:eq(4)").text());
        $("#inputNombreCompleto").val($(this).closest("tr").find("td:eq(5)").text());

        $("#tablaVehiclesModal").modal("hide");
    });

    mapDatesListVisits();
    mapDatesListVisitsEdit();

});

