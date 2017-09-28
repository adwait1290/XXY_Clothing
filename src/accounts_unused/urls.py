from django.conf.urls import url
from django.contrib import admin
from . import views # This line is new!
urlpatterns = [  
	url(r'^ajax/add_user_address/$', 'views.add_user_address', name='ajax_add_user_address'),
    url(r'^accounts/register/$', 'views.registration_view', name='auth_register'),
    url(r'^accounts/address/add/$', 'views.add_user_address', name='add_user_address'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'views.activation_view', name='activation_view'),
]
