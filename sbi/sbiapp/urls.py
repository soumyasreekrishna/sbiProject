from django.urls import path
from . import views
urlpatterns = [
    path('', views.demo, name='demo'),
    path('branch_Thrissur/', views.Thrissur, name='Thrissur'),
    path('branch_Ernakulam/', views.Ernakulam, name='Ernakulam'),
    path('branch_Kozhikodu/', views.Kozhikodu, name='Kozhikodu'),
    path('branch_Kannur/', views.Kannur, name='Kannur'),
    path('branch_Pathanamthitta/', views.Pathanamthitta, name='Pathanamthitta'),

]