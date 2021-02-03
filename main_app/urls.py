from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home,  name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('horses/', views.HorseList.as_view(), name='horses_index'),
    path('jockeys/', views.JockeyList.as_view(), name='jockeys_index'),
    path('horses/create/', views.HorseCreate.as_view(), name='horses_create'),
    path('jockeys/create/', views.JockeyCreate.as_view(), name='jockeys_create'),

]