from django.contrib import admin
from django.urls import path
from votingapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('index/', views.index,name='index'),
    path('registration/', views.registration,name='registration'),
    path('user_action/', views.user_action,name='user_action'),
    path('login_action/', views.login_action,name='login_action'),
    path('admin_home/', views.admin_home,name='admin_home'),
    path('admin_logout/', views.admin_logout,name='admin_logout'),
    path('user_login/', views.user_login,name='user_login'),
    path('user_home/', views.user_home,name='user_home'),
    
    path('user_home/', views.user_home,name="user_home"),
    path('user_profile/',views.user_profile,name="user_profile"),
    path('profile/', views.profile, name='profile'),
    path('user_logout/', views.user_logout,name="user_logout"),
    path('batch/', views.batch,name="batch"),
    path('add_batch/', views.add_batch,name="add_batch"),
    path('course/', views.course,name="course"),
    path('add_course/', views.add_course,name="add_course"),
    path('department/', views.department,name="department"),
    path('add_department/', views.add_department,name="add_department"),
    path('position/', views.position,name="position"),
    path('add_position/', views.add_position,name="add_position"),
    path('notification/', views.notification,name="notification"),
    path('add_notification/', views.add_notification,name="add_notification"),
   

    

]
