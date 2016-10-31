$(document).ready(function(){
    // callbacks

    $("#SearchButton").click(function() {
        if ($('#SearchText').val() != '') {
      		window.location.href = '/' + $('#SearchText').val().replace('/', ' ') + '/searchjobs/';
        }
    });

    $('#SearchText').keypress(function (e) {
        if (e.which == 13) {
            if ($('#SearchText').val() != '') {
                window.location.href = '/' + $('#SearchText').val().replace('/', ' ') + '/searchjobs/';
            }
        }
    });

});
