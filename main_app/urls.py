from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home,  name='home'),
    path('search/', views.search,  name='search'),
    path('accounts/signup/', views.signup, name='signup'),
    path('horses/', views.HorseList.as_view(), name='horses_index'),
    path('horses/<int:horse_id>/add_outcome/', views.add_outcome, name="add_outcome"),
    path('horses/<int:horse_id>/assoc_jockey/<int:jockey_id>/', views.assoc_jockey, name='assoc_jockey'),
    path('jockeys/', views.JockeyList.as_view(), name='jockeys_index'),
    path('jockeys/<int:jockey_id>/add_jockey/', views.add_outcome, name="add_outcome"),
    path('horses/create/', views.HorseCreate.as_view(), name='horses_create'),
    path('jockeys/create/', views.JockeyCreate.as_view(), name='jockeys_create'),
    path('horses/<int:pk>/update', views.HorseUpdate.as_view(), name='horses_update'),
    path('jockeys/<int:pk>/update', views.JockeyUpdate.as_view(), name='jockeys_update'),

]