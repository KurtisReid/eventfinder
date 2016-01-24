console.log("Just seeing that things work...");

$(document).foundation();
window.prettyPrint && prettyPrint();
$('#dp1').fdatepicker({
    format: 'mm-dd-yyyy',
    disableDblClickSelection: true
});
