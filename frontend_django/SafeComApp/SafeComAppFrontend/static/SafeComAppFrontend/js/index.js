$(function () {
    console.log("on ready");
    $('table').DataTable();

    $(document).on("click", "#seleccionador", function (e) {
        $("#inputCedula").val($(this).closest("tr").find("td:eq(0)").text());
        $("#tablaPersonasModal").modal("hide");
    });
});

$(function () {
    console.log("on ready");
    $('table').DataTable();

    $(document).on("click", "#seleccionador", function (e) {
        $("#inputOwner").val($(this).closest("tr").find("td:eq(0)").text());
        $("#tablaPersonasModal").modal("hide");
    });
});
