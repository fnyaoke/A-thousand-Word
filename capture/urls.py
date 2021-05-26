from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('search/', views.search_image, name='search_image'),
    path('category/(\d+)',views.category,name ='category')
]