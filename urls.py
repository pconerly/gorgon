from django.conf.urls.defaults import *
#from views import default, hello

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'views.default', name="index"),
    ('^hello/$', 'views.hello'),
    ('^time/$', 'views.current_datetime'),
    (r'^polls/', include('polls.urls')),
    (r'^maps/', 'views.maps'),
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    ('^time/plus/(\d{1,2})/$', 'views.hours_ahead'),
    (r'^accounts/', include('registration.backends.default.urls')),  #include('pete_register.urls')),

)
