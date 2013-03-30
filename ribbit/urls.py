from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ribbit_app.views.index'), # root
    url(r'^login$', 'ribbit_app.views.login_view'), # login
    url(r'^logout$', 'ribbit_app.views.logout_view'), # logout
    url(r'^ribbits$', 'ribbit_app.views.public'), # public ribbits
    url(r'^submit$', 'ribbit_app.views.submit'), # submit new ribbit
    url(r'^users/$', 'ribbit_app.views.users'), # users
    url(r'^users/(?P<username>\w{0,30})/$', 'ribbit_app.views.users'),
    url(r'^follow$', 'ribbit_app.views.follow'), # follow
    url(r'^signup$', 'ribbit_app.views.signup'), # signup
)  

urlpatterns += staticfiles_urlpatterns()