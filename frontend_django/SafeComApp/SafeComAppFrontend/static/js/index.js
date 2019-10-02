console.log("HOLA A TODOS");

$(".seleccionador").click(function () {
    console.log("aa");
    var cedula = $(this).find('td:first').html();
    alert(cedula);
});
console.log("fff");