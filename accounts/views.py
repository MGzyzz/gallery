from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import views, login, get_user_model
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect
from accounts.forms import LoginForm, RegisterForm
from accounts.models import User, Profile
from gallery.models import Photo
from gallery.models.favorites import Favorites


# Create your views here.

class AuthSuccessUrlMixin:
    def get_success_url(self):

        next_url = self.request.GET.get('next')

        if not next_url:
            next_url = self.request.POST.get('next')

        if not next_url:
            next_url = reverse('home')

        return next_url


class LoginView(views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('home')


class Logout(views.LogoutView):
    def get_next_page(self):
        return self.request.META.get('HTTP_REFERER')


class RegisterView(AuthSuccessUrlMixin, CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(self.get_success_url())

    def form_invalid(self, form):
        avatar_file = self.request.FILES.get('avatar')
        print(avatar_file)
        return render(self.request, 'register.html', {'form': form})


class Detail(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'detail.html'
    context_object_name = 'user'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        user_two = self.request.user
        photo = Photo.objects.filter(user=user)
        context['photos'] = photo
        favorites = Favorites.objects.filter(favorites=user_two, followed_user=user)
        context['favorites'] = favorites.exists()
        return context
