$(document).ready(function(){
    // callbacks
    $("#FeedbackButton").click(function() {
       
        //defining://

        ContactUsMsg_name = $('#ContactUsMsg_name').val();
        ContactUsMsg_email = $('#ContactUsMsg_email').val();
        ContactUsMsg_content = $('#ContactUsMsg_content').val();

        if (ContactUsMsg_name == '' || ContactUsMsg_email == '' || ContactUsMsg_content == ''){
            $('#FeedbackButtonDanger2').removeClass("hide"); // show
            $('#FeedbackButtonDanger').addClass("hide"); // hide
            $('#FeedbackButtonSuccess').addClass("hide"); // hide
        }
        else {
            $('#FeedbackButtonLoader').removeClass("hide"); // display loader

            csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
            $.post("/contactus/", {
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'name': ContactUsMsg_name,
                'email': ContactUsMsg_email,
                'content': ContactUsMsg_content
            }, function(data){
                if (data.response == 1) {
                    // hide ajax loader gif img here
                    $('#FeedbackButtonDanger').addClass("hide"); // hide
                    $('#FeedbackButtonDanger2').addClass("hide"); // hide
                    $('#FeedbackButtonSuccess').removeClass("hide"); // show
                    $('#FeedbackButtonLoader').addClass("hide"); // hide loader
                }
                else {
                    $('#FeedbackButtonSuccess').addClass("hide"); // hide
                    $('#FeedbackButtonDanger2').addClass("hide"); // hide
                    $('#FeedbackButtonDanger').removeClass("hide"); //show
                    $('#FeedbackButtonLoader').addClass("hide"); // hide loader
                }
            });
        }
    });
});