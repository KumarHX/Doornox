# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from urllib2 import urlopen, HTTPError
import json
from jobapp.models import Userinfo, Job, Message, Recommendation, Friendship, Starred, ContactUsMsg, SearchTerm
from django.db.models import Q
import datetime
from django.core import serializers
from django.core.mail import EmailMessage
from django.conf import settings
import boto
from boto.s3.connection import OrdinaryCallingFormat
import random, string
from urllib import quote

def gen_sec_key():
    return ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

def get_session_user(request):
    user_id = request.session.get('session_id')
    if user_id > 0:
        try:
            return Userinfo.objects.get(id=user_id)
        except:
            return None
    return None

def index(request): 
    is_session = request.session.get('session_id', 0)
    if (is_session > 0):
         return redirect('searchjobsall')
    else:
         return render(request, 'jobapp/index.html')
    # - non logged-in index (DONE)
    # should redirect to searchjobs if request.session is set
    # should load index template, providing it any necessary data

def about(request):
    return render(request, 'jobapp/about.html', {'user': get_session_user(request)})

def onlysignin(request):
    is_session = request.session.get('session_id', 0)
    if (is_session > 0):
        return redirect('searchjobsall')
    else:
        return render(request, 'jobapp/onlysignin.html', {'user': get_session_user(request)})

#creates 3 jobs when creating a profile
def profilejobset(user_id):
    for i in range(0,3):
        Job.objects.create(poster_id = user_id, datetime = datetime.datetime.utcnow())

# NEWSFEEDSEARCHJOBSINTEGRATION - also add datetime datetime=datetime.utcnow()


    #allows user to update
def update_user(request):
    user_id = request.session.get('session_id')
    # try:
    user = Userinfo.objects.get(id=user_id)
    user.company = request.POST.get('company')
    user.work_location = request.POST.get('work_location')
    user.location = request.POST.get('location')
    user.job_title = request.POST.get('job_title')
    user.funny_saying = request.POST.get('funny_saying')
    user.resume_link = request.POST.get('resume_link')
    user.save()

    job1 = Job.objects.get(id=request.POST.get('job_id1'))

    if (job1.company_name != request.POST.get('job_companyname1')):
        job1.company_name = request.POST.get('job_companyname1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.location != request.POST.get('location1')):
        job1.location = request.POST.get('location1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.job_title != request.POST.get('job_title1')):
        job1.job_title = request.POST.get('job_title1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.job_description != request.POST.get('job_description1')):
        job1.job_description = request.POST.get('job_description1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.salary_min != request.POST.get('salary_min1')):
        if request.POST.get('salary_min1') == '':
            job1.salary_min = None
        else:
            job1.salary_min = request.POST.get('salary_min1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.salary_max != request.POST.get('salary_max1')):
        if request.POST.get('salary_max1') == '':
            job1.salary_max = None
        else:
            job1.salary_max = request.POST.get('salary_max1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.career_level != request.POST.get('career_level1')):
        job1.career_level = request.POST.get('career_level1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.additional_comments != request.POST.get('additional_comments1')):
        job1.additional_comments = request.POST.get('additional_comments1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.company_link != request.POST.get('company_link1')):
        job1.company_link = request.POST.get('company_link1')
        job1.datetime = datetime.datetime.utcnow()

    if (job1.glassdoor_link != request.POST.get('glassdoor_link1')):
        job1.glassdoor_link = request.POST.get('glassdoor_link1')
        job1.datetime = datetime.datetime.utcnow()

    job1.save()

    job2 = Job.objects.get(id=request.POST.get('job_id2'))

    if (job2.company_name != request.POST.get('job_companyname2')):
        job2.company_name = request.POST.get('job_companyname2')
        job2.datetime = datetime.datetime.utcnow()

    if (job2.location != request.POST.get('location2')):
        job2.location = request.POST.get('location2')
        job2.datetime = datetime.datetime.utcnow()

    if (job2.job_title != request.POST.get('job_title2')):
        job2.job_title = request.POST.get('job_title2')
        job2.datetime = datetime.datetime.utcnow()

    if (job2.job_description != request.POST.get('job_description2')):
        job2.job_description = request.POST.get('job_description2')
        job2.datetime = datetime.datetime.utcnow()

    if (job2.salary_min != request.POST.get('salary_min2')):
        if request.POST.get('salary_min2') == '':
            job2.salary_min = None
        else:
            job2.salary_min = request.POST.get('salary_min2')
        job2.datetime = datetime.datetime.utcnow()

    if (job2.salary_max != request.POST.get('salary_max2')):
        job2.salary_max = request.POST.get('salary_max2')
        job2.datetime = datetime.datetime.utcnow()
        if request.POST.get('salary_max2') == '':
            job2.salary_max = None
        else:
            job2.salary_max = request.POST.get('salary_max2')

    if (job2.career_level != request.POST.get('career_level2')):
        job2.career_level = request.POST.get('career_level2')
        job2.datetime = datetime.datetime.utcnow()
        
    if (job2.additional_comments != request.POST.get('additional_comments2')):
        job2.additional_comments = request.POST.get('additional_comments2')
        job2.datetime = datetime.datetime.utcnow()

    if (job2.company_link != request.POST.get('company_link2')):
        job2.company_link = request.POST.get('company_link2')
        job2.datetime = datetime.datetime.utcnow()

    if (job2.glassdoor_link != request.POST.get('glassdoor_link2')):
        job2.glassdoor_link = request.POST.get('glassdoor_link2')
        job2.datetime = datetime.datetime.utcnow()

    job2.save()
    
    job3 = Job.objects.get(id=request.POST.get('job_id3'))

    if (job3.company_name != request.POST.get('job_companyname3')):
        job3.company_name = request.POST.get('job_companyname3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.location != request.POST.get('location3')):
        job3.location = request.POST.get('location3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.job_title != request.POST.get('job_title3')):
        job3.job_title = request.POST.get('job_title3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.job_description != request.POST.get('job_description3')):
        job3.job_description = request.POST.get('job_description3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.salary_min != request.POST.get('salary_min3')):
        if request.POST.get('salary_min3') == '':
            job3.salary_min = None
        else:
            job3.salary_min = request.POST.get('salary_min3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.salary_max != request.POST.get('salary_max3')):
        if request.POST.get('salary_max3') == '':
            job3.salary_max = None
        else:
            job3.salary_max = request.POST.get('salary_max3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.career_level != request.POST.get('career_level3')):
        job3.career_level = request.POST.get('career_level3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.additional_comments != request.POST.get('additional_comments3')):
        job3.additional_comments = request.POST.get('additional_comments3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.company_link != request.POST.get('company_link3')):
        job3.company_link = request.POST.get('company_link3')
        job3.datetime = datetime.datetime.utcnow()

    if (job3.glassdoor_link != request.POST.get('glassdoor_link3')):
        job3.glassdoor_link = request.POST.get('glassdoor_link3')
        job3.datetime = datetime.datetime.utcnow()

    job3.save()

    return JsonResponse({'response': 1})
    # except:
    #    return JsonResponse({'response': 0}) 

def fblogin(request, access_token):
    try:
        content = urlopen(settings.FB_GRAPH_URL + '?access_token=' + access_token + '&fields=first_name,last_name,email,id,friends').read()
    except HTTPError:
        # if data.response is 0, then the access_token has expired, and
        # the user must re-login through facebook (assuming their server side session hasn't been started yet)
        return JsonResponse({
            'response': 0, 
            'error': 'could not get fb data, get a fresh access_token and retry'
        })    
    obj = json.loads(content)
    fbid = obj['id']
    fname = obj['first_name']
    lname = obj['last_name']
    email = obj['email']
    user_friends = []
    try:
        user_friends = obj['friends']['data']
    except:
        user_friends = []
    print 'user_friends: ', user_friends
    matches = Userinfo.objects.filter(email=email)
    if len(matches) > 0: # update
        match = matches[0]
        match.fname = fname
        match.lname = lname
        match.email = email
        if match.num_logins:
            print 'incrementing num_logins'
            match.num_logins = match.num_logins + 1
        else:
            match.num_logins = 1
        match.last_login = datetime.datetime.utcnow()
        print 'updating last_login time to ', datetime.datetime.utcnow()
        for friend in user_friends:
            try:
                friend_userinfo = Userinfo.objects.get(fbid=friend['id'])
                friendship_matches = Friendship.objects.filter(Q(user_1__id=match.id, user_2__id=friend_userinfo.id) | Q(user_1__id=friend_userinfo.id, user_2__id=match.id))
                if len(friendship_matches) < 1:
                    new_friendship = Friendship.objects.create(user_1_id=match.id, user_2_id=friend_userinfo.id)
            except:
                pass
        match.save()
        request.session['session_id'] = match.id
    else: # create
        new_user = Userinfo.objects.create(
            fbid=fbid, 
            fname=fname,
            lname=lname,
            email=email,
            datetime=datetime.datetime.utcnow(),
            num_logins=1,
            last_login=datetime.datetime.utcnow(),
        )
        for friend in user_friends:
            try:
                friend_userinfo = Userinfo.objects.get(fbid=friend['id'])
                friendship_matches = Friendship.objects.filter(Q(user_1__id=match.id, user_2__id=friend_userinfo.id) | Q(user_1__id=friend_userinfo.id, user_2__id=match.id))
                if len(friendship_matches) < 1:
                    new_friendship = Friendship.objects.create(user_1_id=match.id, user_2_id=friend_userinfo.id)
            except:
                pass
        profilejobset(new_user.id)
        request.session['session_id'] = new_user.id # a Userinfo ID
    return JsonResponse({'response': 1})

    # Done
    # use the access token retrieved from the jssdk to make a url request to the facebook api to retrieve user model fields
    # create a user if doesn’t exist (use email to determine uniqueness), otherwise update the user
    # log the user in using request.session and return json response
    # stores access token in session
    # stores fbid in users table 

def googlogin(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    image_url = request.POST.get('image_url')
    email = request.POST.get('email')
    print 'in googlogin image_url: ', image_url

    matches = Userinfo.objects.filter(email=email)
    if len(matches) > 0: # update
        match = matches[0]
        match.fname = fname
        match.lname = lname
        match.email = email
        match.goog_img_url = image_url
        if match.num_logins:
            print 'incrementing num_logins'
            match.num_logins = match.num_logins + 1
        else:
            match.num_logins = 1
        print 'updating last_login time to ', datetime.datetime.utcnow()
        match.last_login = datetime.datetime.utcnow()
        match.save()
        request.session['session_id'] = match.id
    else: # create
        new_user = Userinfo.objects.create(
            fname=fname,
            lname=lname,
            goog_img_url=image_url,
            email=email,
            datetime=datetime.datetime.utcnow(),
            num_logins=1,
            last_login=datetime.datetime.utcnow(),
        )
        profilejobset(new_user.id)
        request.session['session_id'] = new_user.id # a Userinfo ID
    return JsonResponse({'response': 1})


def lnkdconnect(request):
    user_id = request.session.get('session_id')
    try:
        session_user = Userinfo.objects.get(id=user_id)
        session_user.job_title = request.POST.get('job_title')
        session_user.company = request.POST.get('company_name')
        session_user.location = request.POST.get('loc')
        session_user.lnkd_pubprofile = request.POST.get('pubprofile')
        session_user.lnkdid = request.POST.get('lnkd_id')
        session_user.lnkd_img_url = request.POST.get('pictureurl')
        session_user.save()
        return JsonResponse({'response': 1})
    except:
        return JsonResponse({'response': 2})

    # - api url (7 hours)
    # connects linkedin info to account

def publicprofile(request, user_id): 
    session_id = request.session.get('session_id')
    if (session_id > 0):
        session_user = Userinfo.objects.get(id=session_id)
        user = Userinfo.objects.get(id = user_id)
        jobs = Job.objects.filter(poster = user).exclude(Q(job_title = "") | Q(company_name = ""))
        friendships = Friendship.objects.filter(Q(user_1__id=user_id) | Q(user_2__id=user_id))
        session_friendships = Friendship.objects.filter(Q(user_1__id=session_id) | Q(user_2__id=session_id))
        pp_friends = []
        for friendship in friendships:
            if friendship.user_1.id == int(user_id):
                pp_friends.append(friendship.user_2)
            else:
                pp_friends.append(friendship.user_1)
        session_friends = []
        for session_friendship in session_friendships:
            if session_friendship.user_1.id == int(session_id):
                session_friends.append(session_friendship.user_2)
            else:
                session_friends.append(session_friendship.user_1)
        second_deg_friends = [val for val in pp_friends if val in session_friends]
        friendship_matches = Friendship.objects.filter(Q(user_1__id=user_id, user_2__id=session_id) | Q(user_2__id=user_id, user_1__id=session_id))
        is_friend = len(friendship_matches) > 0
        return render(request, 'jobapp/publicprofile.html', {'user': session_user, 'puser': user, 'jobs' : jobs, 'friendships': friendships, 'second_deg_friends': second_deg_friends, 'is_friend': is_friend, 'siteurl': settings.SITE_URL})
    else:
        return redirect('onlysignin')
    # - logged-in tab (1 hours)
    # pass job object and filter by foriegn key
    # should load profile template, providing it any necessary data

def profile(request): 
    user_id = request.session.get('session_id')
    if (user_id > 0):
        user_id = request.session.get('session_id')
        jobs = Job.objects.filter(poster__id = user_id)
        friendships = Friendship.objects.filter(Q(user_1__id=user_id) | Q(user_2__id=user_id))
        user = Userinfo.objects.get(id = user_id)
        return render(request, 'jobapp/profile.html', {'user': user, 'jobs' : jobs, 'friendships': friendships})
    else:
        return redirect('onlysignin')
    # - logged-in tab (1 hours)
    # pass job object and filter by foriegn key
    # should load profile template, providing it any necessary data

def addjob(request): 
    pass
    # - api url (1 hours)
    # add job and return json response

def googconnect(request):
    pass
    # - redirect URI of google authentication (10 hours)
    # takes code and gets refresh token and access token using POST request
    # stores access token in session
    # stores gid in users table 
    # adds any contacts who are already on the platform (remember emails are unique)

def listgoogcontacts(request):
    pass
    #  - api url (2 hours)
    # lists google contacts of session user if they have connected via google

def invitegoogcontact(request):
    pass
    # - api url (4 hours)
    # emails a goog contact inviting them to join
    # go over the text of the email with Niki
    # Ask Niki to use bluehost.com ($6/mon starter) and register jobapp.com (domains should be $10/yr but you have to check which domain is available for you) and set up an email account from which to send mails from. Then you can add the following settings.py and use django’s send_mail or the other options to send emails.
    # EMAIL_HOST
    # EMAIL_PORT
    # EMAIL_HOST_USER
    # EMAIL_HOST_PASSWORD
    # EMAIL_USE_TLS = True

def contact(request): 
    return render(request, 'jobapp/contact.html', {'user': get_session_user(request)})
    # - logged-in tab (DONE)
    # should load contact template, providing it any necessary data

def contactus(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    content = request.POST.get('content')
    try:
        message = ContactUsMsg.objects.create(
            name = name,
            email = email,
            content = content,
        )
        msg = EmailMessage('Thank you for your feedback, ' + name, 'Thank you for the following message:\n\n' + content + '\n\nBest,\nThe Doornox Team', settings.EMAIL_HOST_USER, to=[email, settings.EMAIL_HOST_USER])
        msg.send()
        return JsonResponse({'response': 1})
    except:
        return JsonResponse({'response': 0})
    # - api url (1 hours)
    # emails “contact us” info to WEBMASTER_EMAIL (set in settings.py, Niki’s email for now)

def inbox(request):
    user_id = request.session.get('session_id')
    if user_id > 0:
        return render (request, 'jobapp/inbox.html', {'user': get_session_user(request), 's3bucket': settings.S3_BUCKET} )
    else:
        return redirect('onlysignin')
    # - logged-in tab (DONE)
    # dont load any data

def getmessages(request):
    receiver_id = request.session.get('session_id')
    mymgs = Message.objects.filter(Q(_to__id = receiver_id) | Q(_from__id = receiver_id))
    my_mgs_elab = []
    for mymg in mymgs:
        to_user = Userinfo.objects.get(id=mymg._to.id)
        from_user = Userinfo.objects.get(id=mymg._from.id)
        datetime = ''
        if mymg.datetime:
            datetime = mymg.datetime.strftime('%Y-%m-%d %H:%M:%S')
        
        my_mgs_elab.append({
            'fields': {
                '_to': int(mymg._to.id),
                '_to_name': to_user.fname + ' ' + to_user.lname,
                '_to_fbid': to_user.fbid,
                '_to_lnkdid': to_user.lnkdid,
                '_from': int(mymg._from.id),
                '_from_name': from_user.fname + ' ' + from_user.lname,
                '_from_fbid': from_user.fbid,
                '_from_lnkdid': from_user.lnkdid,
                'content': mymg.content,
                'datetime': datetime,
            }
        })

    return JsonResponse(my_mgs_elab, safe=False)

# - api url (2 hours)
# returns json response of all messages between session user and passed-in user

def getthread(request, partnerid):
    session_id = request.session.get('session_id')
    thread_msgs = Message.objects.filter(Q(_to__id=partnerid, _from__id=session_id) | Q(_from__id=partnerid, _to__id=session_id)).order_by('datetime')
    return HttpResponse(serializers.serialize("json", thread_msgs), content_type="application/json")

# - api url (2 hours)
# marks threads as read based on passed in thread ids
def markthreadasread(request):
    session_id = request.session.get('session_id')
    thread_msg_ids = request.POST.getlist('thread_msg_ids[]')
    for thread_msg_id in thread_msg_ids:
        try:
            thread_msg = Message.objects.get(id=thread_msg_id)
            if thread_msg._from.id != session_id: 
                thread_msg.read = True
                thread_msg.save()
        except:
            return JsonResponse({'response': 0})
    return JsonResponse({'response': 1})

# - api url
# returns json response of all conversation partners of session user

def getthreadpartners(request):
    session_id = request.session.get('session_id')
    mymgs = Message.objects.filter(Q(_to__id = session_id) | Q(_from__id = session_id))
    msgpartners = {}

    #get the message partner of of an email chain
    for mg in mymgs:
        if mg._from.id != session_id or mg._to.id != session_id: 
            mg_read = False
            if mg._from.id == session_id:
                msgpartnerid = mg._to.id
                datetime = mg.datetime
                mg_read = True
            else:
                msgpartnerid = mg._from.id
                datetime = mg.datetime
                mg_read = mg.read

            msgpartner_info = Userinfo.objects.get(id=msgpartnerid)
            if msgpartnerid in msgpartners:
                if msgpartners[msgpartnerid]['datetime'] < datetime:
                    msgpartners[msgpartnerid]['datetime'] = datetime
                    if not mg.read: # if any one mg is unread, mark thread as unread
                        msgpartners[msgpartnerid]['read'] = mg_read
            else:
                msgpartners[msgpartnerid] = {
                    'datetime': datetime, 
                    'fname': msgpartner_info.fname,
                    'lname': msgpartner_info.lname,
                    'fbid': msgpartner_info.fbid,
                    'goog_img_url': msgpartner_info.goog_img_url,
                    'lnkd_img_url': msgpartner_info.lnkd_img_url,
                    'read': mg_read
                }

    msgpartners_arr = []
    for msgpartnerid in msgpartners:
        msgpartners_arr.append({'id': msgpartnerid, 'data' : msgpartners[msgpartnerid]})
    msgpartners_arr = sorted(msgpartners_arr, key=lambda k: k['data']['datetime'])

    return JsonResponse(msgpartners_arr, safe=False)

def sendmessage(request):
    try:
        message = Message.objects.create(
            _from_id=request.session.get('session_id'),
            _to_id=request.POST.get('toid'),
            content=request.POST.get('content'),
            datetime=datetime.datetime.utcnow()
        )
        msg = EmailMessage(message._from.fname + ' ' + message._from.lname + ' has messaged you on Doornox' , 'Please visit your inbox: ' + settings.SITE_URL + '.' + '\n\nBest,\nThe Doornox Team', settings.EMAIL_HOST_USER, to=[message._to.email, settings.EMAIL_HOST_USER])
        msg.send()
        return JsonResponse({'response': 1})
    except:
        return JsonResponse({'response': 0})

    # from, to and creating a message
    # - api url (3 hours)
    # returns json response of the success of sending the passed-in message from session user to passed-in user

def sendmessagewithattachment(request):
    print 'request.POST: ', request.POST
    print 'request.FILES: ', request.FILES
    user_id = request.session.get('session_id')
    try:
        if request.FILES:
            attachment = request.FILES['fileToUpload']
            conn = boto.s3.connect_to_region('us-west-2', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, is_secure=True, calling_format = OrdinaryCallingFormat())
            print 'settings.S3_BUCKET: ', settings.S3_BUCKET
            bucket = conn.get_bucket(settings.S3_BUCKET)
            secret_key = gen_sec_key()
            k = bucket.new_key('attachments/' + str(user_id) + '/' + secret_key + attachment.name)
            attachment_content = attachment.read()
            k.set_contents_from_string(attachment_content)
            k.set_acl('public-read')
            message = Message.objects.create(
                _from_id=request.session.get('session_id'),
                _to_id=request.POST.get('toid'),
                content=request.POST.get('InboxReplyInput'),
                attachment_path='attachments/' + str(user_id) + '/' + quote(secret_key + attachment.name),
                datetime=datetime.datetime.utcnow()
            )
        else:
            message = Message.objects.create(
                _from_id=request.session.get('session_id'),
                _to_id=request.POST.get('toid'),
                content=request.POST.get('InboxReplyInput'),
                datetime=datetime.datetime.utcnow()
            )
        msg = EmailMessage(message._from.fname + ' ' + message._from.lname + ' has messaged you on Doornox' , 'Please visit your inbox: ' + settings.SITE_URL + '.' + '\n\nBest,\nThe Doornox Team', settings.EMAIL_HOST_USER, to=[message._to.email, settings.EMAIL_HOST_USER])
        msg.send()
        return JsonResponse({'response': 1})
    except:
        return JsonResponse({'response': 0})

    # from, to and creating a message 
    # - api url (3 hours)
    # also ability to add attachment using s3 link with permission
    # returns json response of the success of sending the passed-in message from session user to passed-in user

def searchjobsall(request):
    # NEWSFEEDSEARCHJOBSINTEGRATION get all jobs and order by date filter(...).order_by('-datetime') [and create job dates]
    jobs = Job.objects.exclude(Q(job_title = "") | Q(company_name = "")).order_by('-datetime')
    return render(request, 'jobapp/searchjobs.html', {'jobs': jobs, 'user': get_session_user(request), 'siteurl': settings.SITE_URL})

def num_searchterms(job, search_inputs):
    num_terms = 0
    search_inputs_seen = set()
    for search_input in search_inputs:
        search_input_lw = search_input.lower()
        if search_input_lw in job.company_name.lower() or \
            search_input_lw in job.location.lower() or \
            search_input_lw in job.job_title.lower() or \
            search_input_lw in job.job_description.lower() or \
            search_input_lw in job.company_link.lower() or \
            search_input_lw in job.glassdoor_link.lower() or \
            search_input_lw in job.poster.fname.lower() or \
            search_input_lw in job.poster.lname.lower():
            search_inputs_seen.add(search_input)
    return len(search_inputs_seen)

def searchjobs(request, search_input):
    # go through and collect all jobs containing search terms
    original_search_input = search_input
    search_input = search_input.replace(',', ' ')
    search_inputs = search_input.split()
    print 'search_inputs: ', search_inputs
    jobs = []
    for search_input in search_inputs:
        jobs += Job.objects.filter(Q(company_name__icontains = search_input) | Q(location__icontains = search_input) | Q(job_title__icontains = search_input) | Q(job_description__icontains = search_input) | Q(salary_min__icontains = search_input) | Q(salary_max__icontains = search_input) | Q(career_level__icontains = search_input) | Q(company_link__icontains = search_input) | Q(glassdoor_link__icontains = search_input) | Q(poster__fname__icontains = search_input) | Q(poster__lname__icontains = search_input) | Q(additional_comments__icontains = search_input)).exclude(Q(job_title = "") | Q(company_name = ""))
    jobs = list(set(jobs))
    # sort the jobs array by the number of searchterms that the job contains    
    jobs_with_counts = []
    for job in jobs:
        num_searchterms_v = num_searchterms(job, search_inputs)
        jobs_with_counts.append({'job': job, 'num_terms': num_searchterms_v})
        print 'job: ', job.company_name, job.job_title, ' num_searchterms: ', num_searchterms_v
    print 'jobs_with_counts: ', jobs_with_counts
    jobs_with_counts = sorted(jobs_with_counts, key=lambda k: -k['num_terms']) 
    print 'jobs_with_counts sorted: ', jobs_with_counts
    jobs_sorted = []
    for job_with_count in jobs_with_counts:
        jobs_sorted.append(job_with_count['job'])
    search_term = SearchTerm.objects.create(
        term=search_input,
        num_results=len(jobs),
        searcher=get_session_user(request),
        date=datetime.datetime.utcnow(),
    )
    return render(request, 'jobapp/searchjobs.html', {'search_input': original_search_input, 'jobs': jobs_sorted, 'user': get_session_user(request), 'siteurl': settings.SITE_URL})
    # - logged-in tab (2 hours)
    # should load search template, providing it any necessary data

def starredjobs(request):
    pass
    # - logged-in tab (2 hours)
    # should load search template, but instead feed it with starred jobs data

def job(request, jobid):
    job = Job.objects.get(id = jobid)
    return render(request, 'jobapp/job.html', {'job': job, 'user': get_session_user(request), 'siteurl': settings.SITE_URL}) 
    # - logged-out and logged-in page (2 hours)
    # should load job template, providing it any necessary data

def logout(request):
    # - logged-in tab (2 hours)
    # should logout user and redirect to non-loggedin home page
    request.session.flush()
    return redirect('index')
