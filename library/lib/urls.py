from django.urls import path
from .views import BookViev
from .views import PageOfBookViev

urlpatterns = [
    path('books/', BookViev.as_view()),
    path('book/<int:id>', BookViev.as_view()),
    path('book/<int:book_id>/page/<int:page_number>', PageOfBookViev.as_view())
]