from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('signin/',views.signin_view,name='signin'),
    path('logout/',views.logout_view,name='logout'),
    path('users/',views.user_list,name='user_list'),
]