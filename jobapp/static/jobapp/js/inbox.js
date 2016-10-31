var global_names = {};
var global_fbids = {};
var global_goog_img_urls = {};
var global_lnkd_img_urls = {};

function getHRDate(dob) {
    date_string = '';
    minute = (dob.getMinutes() < 10 ? "0" : "") + dob.getMinutes();
    hour = (dob.getHours() < 13) ? dob.getHours() : dob.getHours() - 12;
    ampm = (dob.getHours() < 12 || dob.getHours() == 24) ? 'am' : 'pm';
    date_string = (dob.getMonth() + 1) + '/' + dob.getDate() + ' ' + hour + ':' + minute + ' ' + ampm;
    return date_string;
}

function RevDateComparator(a, b){ // flipped because want in reverse date order
    if (a[1] > b[1]) return -1;
    if (a[1] < b[1]) return 1;
    return 0;
}

function DateComparator(a, b){ 
    if (Date(a.datetime) < Date(b.datetime)) return -1;
    if (Date(a.datetime) > Date(b.datetime)) return 1;
    return 0;
}


function getThreadPartners() {
    $.get('/getthreadpartners/', function(threadpartners){
        for (i in threadpartners.reverse()) { // present in reverse date order
            date_string = getHRDate(new Date(threadpartners[i]['data']['datetime']));
            conditional_new_msg_text = (threadpartners[i]['data']['read']) ? '' : '<p style="color:#8B4513">Unread</p>';
            conditional_img = (threadpartners[i]['data']['lnkd_img_url'].trim() != '') ? '<img src="' + threadpartners[i]['data']['lnkd_img_url'] + '" width="100%" style="max-width:75px!important"/>' : ((threadpartners[i]['data']['fbid']) ? '<img src="http://graph.facebook.com/' + threadpartners[i]['data']['fbid'] + '/picture?type=large" width="100%" style="max-width:75px!important"/>' : '<img src="' + threadpartners[i]['data']['goog_img_url'] + '" width="100%" style="max-width:75px!important"/>');
            $('#names').html($('#names').html() + '<div class="row"><div class="col-xs-4"><a href="#" class="threadpartner" threadpartnerid="' + threadpartners[i]['id'] + '">' + conditional_img + '</a></div><div class="col-xs-8"><a href="#" class="threadpartner" threadpartnerid="' + threadpartners[i]['id'] + '"><strong> ' + threadpartners[i]['data']['fname'] + ' ' + threadpartners[i]['data']['lname'] + '</strong></a><br>' + date_string + '<br>' + conditional_new_msg_text + '</div></div><hr>');
            global_names[threadpartners[i]['id']] = threadpartners[i]['data']['fname'] + ' ' + threadpartners[i]['data']['lname'];
            global_fbids[threadpartners[i]['id']] = threadpartners[i]['data']['fbid'];
            global_goog_img_urls[threadpartners[i]['id']] = threadpartners[i]['data']['goog_img_url'];
            global_lnkd_img_urls[threadpartners[i]['id']] = threadpartners[i]['data']['lnkd_img_url']
            if (i == 0) 
                getThread(threadpartners[i]['id']);
        }
        $('.inboxloader').hide();
    });
}

function getThread(partnerid) {
    $('#toid').val(partnerid);
    console.log('partnerid: ', partnerid, 'global_lnkd_img_urls: ', global_lnkd_img_urls);
    if (global_lnkd_img_urls[partnerid] && global_lnkd_img_urls[partnerid].trim() != '')
        $('#fbpic').attr('src', global_lnkd_img_urls[partnerid]);
    else if (global_fbids[partnerid])
        $('#fbpic').attr('src', 'http://graph.facebook.com/' + global_fbids[partnerid] + '/picture?type=large');
    else if (global_goog_img_urls[partnerid])
        $('#fbpic').attr('src', global_goog_img_urls[partnerid]);
    $('#messagesender').html(global_names[partnerid]);
    $('#messagesenderurl1').attr('href', '/' + partnerid + '/publicprofile/');
    $('#messagesenderurl2').attr('href', '/' + partnerid + '/publicprofile/');
    $.get('/' + partnerid + '/getthread/', function(thread_msgs){
        var thread = '<div id="thread' + partnerid + '" class="thread">';
        var thread_msg_ids = [];
        for (i in thread_msgs) {
            attachment_code = (thread_msgs[i]['fields']['attachment_path'] != '') ? '<a href="https://s3-us-west-2.amazonaws.com/' + $('#s3bucket').val() + '/' + thread_msgs[i]['fields']['attachment_path'] + '">Attachment</a> - ' : '';
<<<<<<< HEAD
            read = (thread_msgs[i]['fields']['read']) ? 'READ' : 'UNREAD';
            thread +='<b>' + global_names[thread_msgs[i]['fields']['_from']] + '</b><br><p>' + thread_msgs[i]['fields']['content'] + ' - ' + attachment_code + getHRDate(new Date(thread_msgs[i]['fields']['datetime'])) + ' ' + read + '</p><br>';
            thread_msg_ids.push(thread_msgs[i]['pk']);
=======
            read = (thread_msgs[i]['fields']['read']) ? '✓ [seen]' : 'o [unseen]';
            console.log('read is: ', read)
            thread +='<b>' + global_names[thread_msgs[i]['fields']['_from']] + '</b><br><p>' + thread_msgs[i]['fields']['content'] + ' - ' + attachment_code + getHRDate(new Date(thread_msgs[i]['fields']['datetime'])) + ' ' + read + '</p><br>';
>>>>>>> a5167b8801d7ea68b8550b0114c1ed5b1247b88e
        }
        thread += '</div>';
        $('#threads').html(thread);
        $('#InboxReplyLoader').addClass("hide");
        csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.post('/markthreadasread/', { 
            thread_msg_ids: thread_msg_ids,
            csrfmiddlewaretoken: csrfmiddlewaretoken
        }, function(response){
            // console.log('marked thread as read, response', response);
        });
    });
}

$(document).ready(function(){
    global_names[$('#currid').val()] = $('#currfname').val() + ' ' + $('#currlname').val();
    global_fbids[$('#currid').val()] = $('#currfbid').val();
    getThreadPartners();

    $(document).on('click', '.threadpartner', function(){
        threadpartnerid = $(this).attr('threadpartnerid');
        getThread(threadpartnerid);
    })

    $('#InboxReplyButton').click(function(){
        $('#InboxReplyLoader').removeClass("hide");
        $('#replyform').ajaxForm(function() { 
            getThread($('#toid').val());
            $('#InboxReplyInput').val('');
            $('#fileToUpload').val('');
            $('#InboxReplyButton').attr('disabled',true);
        });
    });

    $('#InboxReplyInput').keyup(function(){
        if ($('#fileToUpload').val() == '') {
            console.log('in if for inboxreplyinput');
            if ($(this).val().length != 0)
                $('#InboxReplyButton').attr('disabled', false);            
            else
                $('#InboxReplyButton').attr('disabled',true);
        }
    });

    $('#fileToUpload').change(function(){
        if ($('#InboxReplyInput').val() == '') {
            console.log('in if for filetoupload');
            if ($(this).val())
                $('#InboxReplyButton').attr('disabled', false);
            else
                $('#InboxReplyButton').attr('disabled',true);
        }
    });
})
