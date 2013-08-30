from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('urltree.views',

    url(r'^build/$', 'build_tree', name='urltree-build'),
    url(r'^build/(?P<domain>[^/]+)/$', 'build_tree', name='urltree-build'),
    url(r'^process/(?P<domain>[^/]+)/$', 'process_nodes', name='urltree-process'),
    url(r'^get_logging/$', 'get_logging', name='get_logging'),
    url(r'^show/$', 'show_tree', name='urltree-show'),

)
