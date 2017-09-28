"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from handler500 import Handler500
from django.conf.urls import *
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from core import views as core_views
from checkout import views as checkout_views
from contact import views as contact_views

import debug_toolbar
admin.autodiscover()





urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^login/', core_views.loginview, name="login"),
    url(r'^auth/', core_views.auth_and_login),
    url(r'^$', core_views.secured),
    url(r'^', include('allauth.urls')),
    url(r'^catalog/', include('catalog.urls', namespace='catalog')),
    url(r'^checkout/', include('checkout.urls', namespace='checkout')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = patterns('',
    # Examples:
#     url(r'^$', 'products.views.home', name='home'),
#     url(r'^s/$', 'products.views.search', name='search'),
#     url(r'^products/$', 'products.views.all', name='products'),
#     url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),
#     url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
#     url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
#     url(r'^cart/$', 'carts.views.view', name='cart'),
#     url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
#     url(r'^orders/$', 'orders.views.orders', name='user_orders'),
#     url(r'^ajax/dismiss_marketing_message/$', 'marketing.views.dismiss_marketing_message', name='dismiss_marketing_message'),
#     url(r'^ajax/email_signup/$', 'marketing.views.email_signup', name='ajax_email_signup'),
#     url(r'^ajax/add_user_address/$', 'accounts.views.add_user_address', name='ajax_add_user_address'),

#     # url(r'^blog/', include('blog.urls')),
#     #(?P<all_items>.*)
#     #(?P<id>\d+)
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
#     url(r'^accounts/login/$', 'accounts.views.login_view', name='account_login'),
#     url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
#     url(r'^accounts/address/add/$', 'accounts.views.add_user_address', name='add_user_address'),
#     url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),
#     url(r'^accounts/', include('allauth.urls')),
# )

# from django.conf.urls import url, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.views.static import serve
# from products import views as products_views
# from contact import views as contact_views
# from carts import views as carts_views
# from orders import views as orders_views
# from marketing import views as marketing_views
# from accounts import views as accounts_views
# from products.views import home
# admin.autodiscover()

# # urlpatterns = [
# #     url(r'^admin/', admin.site.urls),
# urlpatterns = [
#     # Examples:
#     url(r'^$', products_views.home, name='home'),
#     url(r'^s/$', 'products_views.search', name='search'),
#     url(r'^products/$', 'products_views.all', name='products'),
#     url(r'^products/(?P<slug>[\w-]+)/$', 'products_views.single', name='single_product'),
#     url(r'^cart/(?P<id>\d+)/$', 'carts_views.remove_from_cart', name='remove_from_cart'),
#     url(r'^cart/(?P<slug>[\w-]+)/$', 'carts_views.add_to_cart', name='add_to_cart'),
#     url(r'^cart/$', 'carts_views.view', name='cart'),
#     url(r'^checkout/$', 'orders_views.checkout', name='checkout'),
#     url(r'^orders/$', 'orders_views.orders', name='user_orders'),
#     url(r'^ajax/dismiss_marketing_message/$', 'marketing_views.dismiss_marketing_message', name='dismiss_marketing_message'),
#     url(r'^ajax/email_signup/$', 'marketing_views.email_signup', name='ajax_email_signup'),
    # url(r'^ajax/add_user_address/$', 'accounts_views.add_user_address', name='ajax_add_user_address'),

# ]

if settings.DEBUG:
	urlpatterns == static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
