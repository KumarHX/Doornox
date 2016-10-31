$(document).ready(function(){
    // callbacks
    $("[data-toggle=popover]").popover();

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

    $(document).on('click', '.msgstartersend', function(){
        index = $(this).attr('index');
        console.log('msgstarter: ' + encodeURIComponent($('#msgstarter' + index).val()))
        csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.post('/sendmessage/', {
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'toid': $('#curruserid' + index).val(), 
            'content': $('#msgstarter' + index).val()
        }, function(resp){
            console.log(resp);
            window.location.href = '/inbox/';
        });
    });

});
