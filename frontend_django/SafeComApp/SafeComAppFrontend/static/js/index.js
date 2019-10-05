
  $(function()
  {
    $(document).on("click", "#seleccionador", function(e) {
        $("#inputCedula").val($(this).closest("tr").find("td:eq(0)").text());
        $("#tablaPersonasModal").modal("hide");
    });
  });