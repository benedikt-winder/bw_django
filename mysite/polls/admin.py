from polls.models import Poll
from django.contrib import admin

#admin.site.register(Poll)

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Frage', {'fields':['question']}),
        ('Date information',{'fields':['pub_date']}),
    ]
    
    #fields = ['pub_date', 'question']
    
admin.site.register(Poll, PollAdmin)

