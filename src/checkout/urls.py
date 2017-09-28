from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cart/add/(?P<slug>[\w_-]+)/$',views.create_cartitem,name='create_cartitem'),
    url(r'^cart/$',views.cart_item,name='cart_item'),
    url(r'^finish$',views.finish,name='finish'),
    url(r'^remove/(?P<id>[\w_-]+)/$',views.remove_item,name='remove_item'),
    url(r'^minus/(?P<id>[\w_-]+)/$', views.minus, name='minus'),
    url(r'^plus/(?P<id>[\w_-]+)/$', views.plus, name='plus'),
    ]