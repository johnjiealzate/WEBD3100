from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.route_base, name='base.html'), 
    path('routes/', views.route_list, name='route_list'), 
    path('routes/new/', views.route_create, name='route_create'), 
    path('routes/<str:pk>/edit/', views.route_update, name='route_update'), 
    path('routes/<str:pk>/delete/', views.route_delete, name='route_delete'), 
] 