from django.urls import path
from .views import ProfileAPIView,PublicProfileAPIView

urlpatterns = [
    # private profile
    path('profile/', ProfileAPIView.as_view()),

    # public profile
    path('profile/<str:username>/', PublicProfileAPIView.as_view()),
]
