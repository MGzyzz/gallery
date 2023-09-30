from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from gallery.models import Photo
from django.http import JsonResponse
from api.serializers import PhotoDetailSerializers, PhotoListSerializers
# Create your views here.


class PhotoListView(APIView):
    def get(self, request):
        try:
            photo = Photo.objects.all()
            serializer = PhotoListSerializers(photo, many=True)
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
    pass



class PhotosUpdateView(APIView):
    def put(self, request, pk):
        try:
            task = Photo.objects.get(id=pk)
        except Photo.DoesNotExist:
            return JsonResponse({'success': 'Not Work'}, status=404)
        serializer = PhotoDetailSerializers(task, data=request.data)

        if serializer.is_valid():
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

