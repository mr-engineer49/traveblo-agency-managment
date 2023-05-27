from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm



app_name = 'main'


urlpatterns = [
    path('', views.home, name="home"),
    path('places/', views.places, name='places'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('vacations/', views.vacations, name='vacations'),
    path('activities/', views.activities, name='activities'),
    path('trips/', views.trips, name='trips'),
    path('logout', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
]
