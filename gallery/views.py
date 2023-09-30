from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from gallery.models import Photo
from gallery.forms import PhotoForm

# Create your views here.


class Home(ListView):
    template_name = 'home.html'
    context_object_name = 'photos'
    model = Photo
    ordering = ['-created_at']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        if self.request.user.is_authenticated:
            user = self.request.user
            favorited_photos = Photo.objects.filter(user_favorite=user)
            favorited_ids = favorited_photos.values_list('id', flat=True)
            context['favorited_ids'] = favorited_ids

        return context


class CreatePhotos(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Photo
    form_class = PhotoForm
    permission_required = 'gallery.add_photo'
    permission_denied_message = 'You have no rights'


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('home')

class DetailPhotos(DetailView):
    template_name = 'detailPhotos.html'
    model = Photo
    context_object_name = 'photo'


from django.views.generic import ListView
from .models import Photo

class FavoritePhotosListView(ListView):
    model = Photo
    template_name = 'favorite.html'
    context_object_name = 'favorite_photos'

    def get_queryset(self):
        return Photo.objects.filter(user_favorite=self.request.user)