

urlpatterns = patterns('',
    (r'^accounts/', include('registration.backends.default.urls')),

)
