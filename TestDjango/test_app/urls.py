#url паттернс
# три ссылки
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings
from .views import library_list, AuthorListView, BookListView


urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='about-club'),
	path('adress/', views.adress, name='adress-club'),
	path('help/', views.help, name='help-club'),
	path('flowers/', views.flowers, name='flowers'),
	path('index/', views.index, name='index'),
	path('image_detail/<int:image_id>/', views.image_detail, name='image_detail'),
	path('libraries/', library_list, name='library_list'),
	path('authors/', AuthorListView.as_view(), name='author_list'),
	path('books/', BookListView.as_view(), name='book_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)