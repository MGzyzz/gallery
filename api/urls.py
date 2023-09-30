from django.urls import path
from api.views import PhotoListView, PhotosDetailView, PhotosUpdateView, PhotosDeleteView

urlpatterns = [
    path('list/', PhotoListView.as_view(), name='list-json'),
    path('detail/<int:pk>', PhotosDetailView.as_view(), name='detail-json'),
    path('update/<int:pk>', PhotosUpdateView.as_view(), name='update-json'),
    path('delete/<int:pk>', PhotosDeleteView.as_view(), name='delete-json')
]
