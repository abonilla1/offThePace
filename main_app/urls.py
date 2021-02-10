from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),
    path("horses/", views.HorseList.as_view(), name="horses_index"),
    path("horses/<int:horse_id>/", views.horses_detail, name="detail"),
    path("horses/<int:horse_id>/add_horse_outcome/", views.add_horse_outcome, name="add_horse_outcome"),
    path("horses/<int:pk>/delete", views.HorseDelete.as_view(), name="horses_delete"),
    path("delete_horse_outcome/<int:outcome_id>/", views.delete_horse_outcome, name="delete_horse_outcome"),
    path("jockeys/<int:jockey_id>/assoc_horse/<int:horse_id>/", views.assoc_horse, name="assoc_horse"
    ),
    path("jockeys/<int:jockey_id>/", views.jockeys_detail, name="jdetail"),
    path("jockeys/<int:pk>/delete", views.JockeyDelete.as_view(), name="jockeys_delete"),
    path("jockeys/<int:jockey_id>/unassoc_horse/<int:horse_id>/", views.unassoc_horse, name="unassoc_horse"),
    path("jockeys/", views.JockeyList.as_view(), name="jockeys_index"),
   
    path('jockeys/<int:jockey_id>/add_jockey_experience/', views.add_jockey_experience, name="add_jockey_experience"),
    path("delete_jockey_experience/<int:experience_id>/", views.delete_jockey_experience, name="delete_jockey_experience"),
    path("horses/create/", views.HorseCreate.as_view(), name="horses_create"),
    path("jockeys/create/", views.JockeyCreate.as_view(), name="jockeys_create"),
    path("horses/<int:pk>/update", views.HorseUpdate.as_view(), name="horses_update"),
    path("jockeys/<int:pk>/update", views.JockeyUpdate.as_view(), name="jockeys_update"),
]