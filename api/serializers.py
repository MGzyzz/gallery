from rest_framework import serializers, permissions
from gallery.models import Photo
from rest_framework.permissions import IsAuthenticated


class PhotoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['signature', 'image']


class PhotoDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['signature']



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
