from django.urls import path
from . import views


app_name = 'school_app'

urlpatterns = [
    path('',views.base,name='home'),
    path('register/',views.register_req,name='register'),
    path('home/',views.HomeView.as_view(),name='home'),
    path('<slug:slug>/',views.HomeDetailView.as_view(),name='detail'),
]
