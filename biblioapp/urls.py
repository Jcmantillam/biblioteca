from django.urls import path, include
from .views import BookViewset, BookSearchView, SearchBook, SaveBook, DeleteBook
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewset)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/search_book_local/', BookSearchView.as_view()),
    path('api/v1/search_book/', SearchBook),
    path('api/v1/save_book/', SaveBook),
    path('api/v1/delete_book/', DeleteBook),
]
