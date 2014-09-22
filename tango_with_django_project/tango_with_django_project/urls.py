from django.conf.urls import patterns, include, url
from django.conf import settings # allows access to the variables defined within our project's settings.py file

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^tango_with_django_project/', include('tango_with_django_project.foo.urls')),
    url(r'^rango/', include('rango.urls')), # ADD THIS NEW TUPLE!

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# check if the Django project is run in the DEBUG mode
if settings.DEBUG: 
    # append new URL matching pattern
    urlpatterns += patterns(
    # handles the dispatching of uploaded media files
    'django.views.static',
    # every request starting with media/ will be served to  'django.views.static'
    (r'media/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}), )
