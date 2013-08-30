# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import URLTree, URLNode


class URLTreeAdmin(admin.ModelAdmin):
    pass
    
class URLNodeAdmin(admin.ModelAdmin):
    list_filter = ('urltree', 'checked')
    list_display = ('url', 'checked', 'urltree', 'info')


admin.site.register(URLTree, URLTreeAdmin)
admin.site.register(URLNode, URLNodeAdmin)