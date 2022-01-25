from django.urls import path
from .import views

app_name ='socials'

urlpatterns = [
    path("",views.dashboard,name='dashboard'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path("profile/<int:pk>/", views.profile, name="profile"), 
    path('user_account/', views.userAccount,name='user_account')   
]