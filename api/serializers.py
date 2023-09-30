from rest_framework import serializers, permissions
from gallery.models import Photo


class PhotoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['summary', 'description', 'status', 'type']



class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsAuthenticatedAndOwnerOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_object_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
