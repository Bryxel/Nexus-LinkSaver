from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('category_create/', views.category_create, name='category_create'),
    path('category_edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category_delete/<int:id>/', views.category_delete, name='category_delete'),
    path('category_detail/<int:id>/', views.category_detail, name='category_detail'),

    path('category/<int:category_id>/link_create/', views.link_create, name='link_create'),
    path('link_edit/<int:id>/', views.link_edit, name='link_edit'),
    path('link_delete/<int:id>/', views.link_delete, name='link_delete'),


]