from django.urls import path
from . import views

app_name = 'clientdb'
urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.ClientList.as_view(), name='ClientList'),
    path('add', views.ClientCreateView.as_view(), name='ClientAdd'),
    path('<int:client_id>/', views.detail, name='detail'),
]