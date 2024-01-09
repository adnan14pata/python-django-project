from django.urls import  path
from .import views
urlpatterns = [
    path('',views.lognsign, name='lognsign'),
    path('login.html/', views.loginpage, name='login_view'),
    path('signup.html/', views.signuppage, name='signup'),
]