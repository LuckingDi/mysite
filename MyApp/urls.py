from django.urls import path

from . import views

app_name = 'MyApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/album/', views.album_get, name='album_get')
]