from django.contrib import admin
from .models import Poll, Choice, Vote
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.admin import SimpleListFilter


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by')



@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('poll', 'text', 'votes_count')
    list_filter = ('poll',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'choice', 'user')
    list_filter = ('poll', 'user')


