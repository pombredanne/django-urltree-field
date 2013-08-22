from django.conf import settings
import os


URLTREE_STATIC_URL = getattr(settings, 'URLTREE_STATIC_URL', settings.STATIC_URL+'urltree/')

JQUERY_URL = URLTREE_STATIC_URL+'/js/jquery.min.js'
URLTREE_JS_URL = URLTREE_STATIC_URL+'/js/urltree.js'
URLTREE_FIELD_CSS_URL = URLTREE_STATIC_URL+'/css/urltree_field.css'
URLTREE_POPUP_JS_URL = URLTREE_STATIC_URL+'/js/urltree_popup.js'
URLTREE_POPUP_CSS_URL = URLTREE_STATIC_URL+'/css/urltree_popup.css'
