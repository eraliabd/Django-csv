from django.contrib import admin
from .models import About, RecentWork, Contact, Skill, Comment, ReplyComment


class RecentWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')
    list_display_links = ('id', 'title')
    list_filter = ('created',)
    search_fields = ('title',)


admin.site.register(About)
admin.site.register(RecentWork, RecentWorkAdmin)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Comment)
admin.site.register(ReplyComment)
