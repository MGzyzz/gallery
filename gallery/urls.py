from django.contrib import admin
from django.urls import path, include
from gallery.views import Home, CreatePhotos, DetailPhotos, FavoritePhotosListView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create', CreatePhotos.as_view(), name='create'),
    path('detail/<int:pk>', DetailPhotos.as_view(), name='detail'),
    path('favorite', FavoritePhotosListView.as_view(), name='favorite'),
]