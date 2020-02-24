from django.urls import path
from . import views

app_name = 'clientdb'
urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.ProfileList.as_view(), name='ProfileList'),
    path('add', views.ProfileCreateView.as_view(), name='ProfileAdd'),
    path('<int:profile_id>/', views.detail, name='detail'),
]