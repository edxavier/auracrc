from django.conf.urls import patterns, include, url
from doc import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'doc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('inicio.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    	{ 'document_root' : settings.MEDIA_ROOT  }),
    url(r'^admin/', include(admin.site.urls)),
)
