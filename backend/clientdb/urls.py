from django.urls import path
from . import views

app_name = 'clientdb'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:profile_id>/', views.detail, name='detail'),
]