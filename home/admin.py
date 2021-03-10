from django.contrib import admin
from home.models import Messages, eventregister, complaintfile, meetingp, mreport

# Register your models here.

admin.site.register(Messages)
admin.site.register(eventregister)
admin.site.register(complaintfile)
admin.site.register(meetingp)
admin.site.register(mreport)