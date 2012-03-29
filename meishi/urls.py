from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('meishi.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'index'),
    url(r'^list_user/$', 'list_user'),
    url(r'^company_information/$', 'company_information'),
    url(r'^my_meishi/$', 'my_meishi'),
    url(r'^my_meishi.json/$', 'my_meishi_json'),
    url(r'^exchange/$', 'exchange'),
    url(r'^exchange_history/$', 'exchange_history'),
    url(r'^meishi/(?P<meishi_id>\d+)/$', 'meishi_detail'),
    url(r'^meishi/add/$', 'meishi_add'),
    url(r'^logout/$', 'logout_view'),
    # url(r'^(?P<meishi_id>\d+)/results/$', 'results'),
    # url(r'^(?P<meishi_id>\d+)/vote/$', 'vote'),
)
