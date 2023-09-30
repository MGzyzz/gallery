from django.urls import path
from api.views import PhotoListView, PhotosDetailView, PhotosUpdateView, PhotosDeleteView, PhotosCreateView, PhotoViewsSet

urlpatterns = [
    path('list/', PhotoListView.as_view(), name='list-json'),
    path('create/', PhotosCreateView.as_view(), name='CREATE-json'),
    path('detail/<int:pk>', PhotosDetailView.as_view(), name='detail-json'),
    path('update/<int:pk>', PhotosUpdateView.as_view(), name='update-json'),
    path('delete/<int:pk>', PhotosDeleteView.as_view(), name='delete-json'),
    path('<int:id>/favorite/', PhotoViewsSet.as_view({'post': 'favorite'}), name='photo-favorite'),
    path('<int:id>/un_favorite/', PhotoViewsSet.as_view({'delete': 'un_favorite'}), name='photo-un_favorite'),

]
