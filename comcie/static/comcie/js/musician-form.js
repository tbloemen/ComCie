$("table thead div").on("click", function (e) {
  var mytext = e.target.innerHTML;
  var index = $(this).parent().index();
  addButton(mytext, index);
  $("table thead").each(function () {
    $(this).find("th").eq(index).hide();
  });
  $("table tbody tr").each(function () {
    $(this).find("td").eq(index).hide();
  });
});

function returnToTable(myButton) {
  var index = $(myButton).data("index");
  $("table thead").each(function () {
    $(this).find("th").eq(index).show();
  });
  $("table tbody tr").each(function () {
    $(this).find("td").eq(index).show();
  });
  $(myButton).remove();
}

function addButton(headerName, index) {
  $("#hiddenColumns").css("background-color", "orange");
  //$("$hiddenColumns button").
  $("#hiddenColumns").append(
    '<button type="button" data-index="' +
      index +
      '" class="btn btn-primary" onclick="returnToTable(this)">' +
      headerName +
      "</button>"
  );
}
