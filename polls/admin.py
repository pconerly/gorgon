from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)

