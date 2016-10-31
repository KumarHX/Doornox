from django.contrib import admin
from jobapp.models import Userinfo, Job, Message, Recommendation, Friendship, Starred, ContactUsMsg, SearchTerm

class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'fbid', 'lnkdid', 'gid', 'location', 'work_location', 'company', 'job_title', 'funny_saying', 'resume_link', 'lnkd_pubprofile', 'lnkd_img_url', 'goog_img_url', 'datetime', 'num_logins', 'last_login')

class JobAdmin(admin.ModelAdmin):
    list_display = ('poster', 'company_name', 'location', 'job_title', 'job_description', 'salary_min', 'salary_max', 'career_level', 'company_link', 'glassdoor_link', 'additional_comments', 'datetime')

class MessageAdmin(admin.ModelAdmin):
	list_display = ('_from', '_to', 'to_email', 'content', 'read', 'datetime', 'attachment_path')

class RecommendationAdmin(admin.ModelAdmin):
	list_display = ('recommender', 'recommendee', 'receiver', 'receiver_email', 'preference', 'cover_letter_link')

class FriendshipAdmin(admin.ModelAdmin):
	list_display = ('user_1', 'user_2')

class StarredAdmin(admin.ModelAdmin):
	list_display = ('job', 'user')

class ContactUsMsgAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content')

class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'num_results', 'searcher', 'date')

admin.site.register(Userinfo, UserinfoAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(Starred, StarredAdmin)
admin.site.register(ContactUsMsg, ContactUsMsgAdmin)
admin.site.register(SearchTerm, SearchTermAdmin)
