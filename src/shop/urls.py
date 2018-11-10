from django.conf.urls import url
from django.urls import re_path, path
from . import views

urlpatterns = [
     path('shop/', views.product_list, name= 'product_list'),
     re_path(r'^shop/(?P<category_slug>[-\w]+)/$', views.product_list, name= 'product_list_by_category'),
     re_path(r'^shop/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name= 'product_detail')
]