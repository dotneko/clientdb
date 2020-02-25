from django.urls import path
from . import views

app_name = 'clientdb'
urlpatterns = [
    # path('', views.index, name='index'),
    path('add', views.ClientCreateView.as_view(), name='ClientAdd'),
    path('<int:pk>/', views.ClientDetailView.as_view(), name='ClientDetail'),
    path('', views.ClientList.as_view(), name='ClientList'),
]