from django.urls import path
from .views import ProfileAPIView, PublicProfileAPIView, RegisterAPIView

urlpatterns = [
    # private profile
    path('profile/', ProfileAPIView.as_view()),

    # public profile
    path('profile/<str:username>/', PublicProfileAPIView.as_view()),

    # register
    path('auth/register/', RegisterAPIView.as_view()),
]
