from django.urls import path
from . import views

app_name = 'clientdb'
urlpatterns = [
    # path('', views.index, name='index'),
    path('add', views.ClientCreate.as_view(), name='ClientAdd'),
    path('search/', views.SearchResults.as_view(), name='SearchResults'),
    path('<int:pk>/delete', views.ClientDelete.as_view(), name='ClientDelete'),
    path('<int:pk>/', views.ClientUpdate.as_view(), name='ClientDetail'),
    # path('<int:pk>/', views.ClientDetail.as_view(), name='ClientDetail'),
    path('', views.ClientList.as_view(), name='ClientList'),
]