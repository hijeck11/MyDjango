from django.urls import path
from . import views
urlpatterns = [
	path('events/', views.event_list, name='event_list'),
	path('form/', views.create_item, name='create_item'),
	path('', views.user_list, name='user_list'),
	path("w/", views.index),
]