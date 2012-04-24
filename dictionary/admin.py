from django.contrib.contenttypes import generic
from django.contrib import admin
from dictionary.models import *

class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('term', 'description', 'tags',)
    list_filter = ('alpha_position', 'tags',)
    search_fields = ('term', 'description',)
        
admin.site.register(Dictionary, DictionaryAdmin)