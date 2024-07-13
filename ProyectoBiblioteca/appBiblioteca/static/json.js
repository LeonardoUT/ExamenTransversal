$(document).on('click', '.verMas', function () {
    $("#modalVerDetalle").modal('toggle')
    $(".detTitulo").html($(this).attr('data-titulo'))
    $(".detAño").html($(this).attr('data-año'))
    $(".detDescripcion").html($(this).attr('data-descripcion'))
  })