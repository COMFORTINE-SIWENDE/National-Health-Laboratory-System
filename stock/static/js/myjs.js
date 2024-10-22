$(function() {
    $('.table').paging({
        limit:6
    })
    $(".datetimeinput").datepicker({
        changeYear: true,
        changeMonth: true,
        dateFormat:'yy-mm-dd',
    });
});
