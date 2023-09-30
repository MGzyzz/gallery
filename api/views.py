from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from gallery.models import Photo
from django.http import JsonResponse
from api.serializers import PhotoDetailSerializers, PhotoListSerializers, PhotoUpdateSerializers, PhotoSerializers
# Create your views here.


class PhotoListView(APIView):
    def get(self, request):
        try:
            photos = Photo.objects.all()
            serializer = PhotoListSerializers(photos, many=True)
            return JsonResponse(serializer.data, status=200)
        except Photo.DoesNotExist:
            return JsonResponse({'success': 'Not Work'}, status=404)

class PhotosDetailView(APIView):
    def get(self, request, pk):
        try:
            photo = Photo.objects.get(id=pk)
            serializer = PhotoDetailSerializers(photo)
            return JsonResponse(serializer.data, status=200)
        except Photo.DoesNotExist:
            return JsonResponse({'error': 'Photos not found'}, status=404)



class PhotosCreateView(APIView):
    def post(self, request):
        serializer = PhotoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



class PhotosUpdateView(APIView):
    def put(self, request, pk):
        try:
            photo = Photo.objects.get(id=pk)
        except Photo.DoesNotExist:
            return JsonResponse({'success': 'Not Work'}, status=404)
        serializer = PhotoUpdateSerializers(photo, data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            print('work')
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


class PhotosDeleteView(APIView):
    def delete(self, request, pk):
        try:
            task = Photo.objects.get(id=pk)
            task.delete()
            return JsonResponse({'message': 'Photo deleted successfully'}, status=204)
        except Photo.DoesNotExist:
            return JsonResponse({'error': 'Photo not found'}, status=404)


class PhotoViewsSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    @action(detail=True, methods=['post'])
    def favorite(self, request, id=None):
        photo = self.get_object()
        user = request.user
        if user in photo.user_favorite.all():
            return JsonResponse({'detail': 'You have already liked this publication'}, status=400)
        photo.user_favorite.add(user)
        photo.save()
        print('work')

        return JsonResponse({'work': 'work'}, status=200)

    @action(detail=True, methods=['delete'])
    def un_favorite(self, request, id=None):
        photo = self.get_object()
        user = request.user
        if user in photo.user_favorite.all():
            photo.user_favorite.remove(user)
            photo.save()

            return JsonResponse({'work': 'work'}, status=200)
        else:
            return JsonResponse({'detail': 'You have not liked this publication'}, status=400)