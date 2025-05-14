from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plany/grupowe/', views.plany_grupowe, name='plany_grupowe'),
    path("plany/dwoje/", views.plany_dwoje, name="plany_dwoje"),
    path("plany/indywidualne/", views.plany_indywidualne, name="plany_indywidualne"),


]
