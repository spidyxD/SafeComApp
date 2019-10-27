$(function () {
    console.log("on ready");
    $('table').DataTable();

    $(document).on("click", "#seleccionador", function (e) {
        $("#inputCedula").val($(this).closest("tr").find("td:eq(0)").text());
        $("#tablaPersonasModal").modal("hide");
    });
});

function setDateformatIN(date){
    var formatDate  = new Date(date);
    document.getElementById("inDate").value = formatDate
}

function setDateformatOUT(date){
    var formatDate  =  new Date(date);
    document.getElementById("outDate").value = formatDate
}
