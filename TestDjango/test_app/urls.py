#url паттернс
# три ссылки

from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='about-club'),
	path('adress/', views.adress, name='adress-club'),
	path('help/', views.help, name='help-club'),
]