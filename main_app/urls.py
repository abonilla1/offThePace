from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home,  name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('horses/create/', views.HorseCreate.as_view(), name='horses_create'),

]