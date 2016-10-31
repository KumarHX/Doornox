$(document).ready(function(){
    // callbacks
    $("[data-toggle=popover]").popover();

    $(document).on('click', '#msgstartersend', function(){
        csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.post('/sendmessage/', {
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'toid': $('#curruserid').val(),
            'content': $('#msgstarter').val()
        }, function(resp){
            window.location.href = '/inbox/';
        });
    });
});
