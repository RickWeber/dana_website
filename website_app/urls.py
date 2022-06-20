from django.urls import path
import .views

urlpatterns = [
    path('', views.HomeView(), name="home"),
]
