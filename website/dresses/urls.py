from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dresses'

urlpatterns = [
    # /dresses/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/dresses/register
    url(r'^register/$',views.UserFormView.as_view(), name='register'),

    # /dresses/4242/
    url('^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail2'),

    #/dresses/lehengas/add/
    url(r'lehengas/add/$',views.LehengasCreate.as_view(), name='lehenga-add'),

    #dresses/lehengas/2/
    url(r'lehengas/(?P<pk>[0-9]+)/$',views.LehengasUpdate.as_view(), name='lehenga-update'),

    #dresses/lehengas/2/delete
    url(r'lehengas/(?P<pk>[0-9]+)/delete/$',views.LehengasDelete.as_view(), name='lehenga-delete'),

    url(r'login/$', views.login , name='login'),

    url(r'logout/$', views.logout , name='logout'),

    url(r'auth/$', views.auth_view , name='authentiate'),

    url(r'description/$', views.DescView.as_view(), name='description'),

    path('search/',views.search_list,name='search'),

    url(r'^list/$', views.product_list ,name='list')



]
