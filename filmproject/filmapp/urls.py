from . import views
from django.urls import path

app_name = 'filmapp'
urlpatterns = [

    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movies, name='add_movies'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('add_film/', views.add_film, name='add_film'),
]
