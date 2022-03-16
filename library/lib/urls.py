from django.urls import path
from .views import BookViev

urlpatterns = [
    path('books/', BookViev.as_view()),
    path('book/<int:pk>/', BookViev.as_view()),
]