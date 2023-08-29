from .import views
from django.urls import path

urlpatterns = [
    path('', views.MovieList.as_view(),name='movie-list'),
    path('<int:pk>/', views.MovieDetail.as_view(),name='movie-detail'),
]
