from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-home'),
	path('events/', views.event_list, name='event_list'),
	path('form/', views.create_item, name='create_item'),
]