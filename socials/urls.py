from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
app_name ='socials'

urlpatterns = [  
    path('register',views.registerPage,name='sign_up'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),

    path("",views.dashboard,name='dashboard'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path("profile/<int:pk>/", views.profile, name="profile"), 
   # path('sign_out', views.backPage, name='back'),

    
path('reset_password/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),

    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='change_password'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_confirm'),

    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name ='reset_password_done'),
    
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name='reset_complete'),
]