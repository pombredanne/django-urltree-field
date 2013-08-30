# -*- coding: utf-8 -*-
from django.db import models
from django.forms.widgets import Input
from django.db.models.fields import CharField
from django.template.loader import render_to_string
from urltree.default_settings import *


class UrlTreeBrowseWidget(Input):
    input_type = 'text'
    
    class Media:
        css = {'all': (URLTREE_FIELD_CSS_URL,)}
        js = (URLTREE_JS_URL,)
    
    def render(self, name, value, attrs=None):
        if value is None:
            value = ""
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        final_attrs['search_icon'] = URLTREE_STATIC_URL + 'img/urltree_icon_show.gif'
        return render_to_string("urltree/custom_field.html", locals())


class UrlTreeField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(UrlTreeField, self).__init__(max_length=255, *args, **kwargs)
    
    def formfield(self, *args, **kwargs):
        kwargs['widget'] = UrlTreeBrowseWidget()
        return super(UrlTreeField, self).formfield(*args, **kwargs)
    
    def south_field_triple(self):
        """
        Return a suitable description of this field for South.
        """
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.CharField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

