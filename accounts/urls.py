from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('detail/<int:id>/', views.Detail.as_view(), name='detail-auth')
]
