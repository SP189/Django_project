from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    #orders/create/
    url(r'^create/$', views.order_create, name='order_create'),

    url(r'^create/completed/$', views.completed ,name="completion_msg"),
]