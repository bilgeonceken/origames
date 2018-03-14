$(function(){
  $(".fold-table tr.view").on("click", function(){
    $(this).toggleClass("open").next(".fold").toggleClass("open");
  });
});

$(document).ready(function()
    {
        $("#myTable1").tablesorter();
        $("#myTable2").tablesorter();
    }
);
