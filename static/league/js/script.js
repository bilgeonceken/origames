$(function(){
  $(".fold-table tr.view").on("click", function(){
    $(this).toggleClass("open").next(".fold").toggleClass("open");
  });
});

function init() {
  var sorter = tsorter.create('myTable2');
}

window.onload = init;
