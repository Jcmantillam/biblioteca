import json

from django.shortcuts import render
from .serializers import BookSerializer, SearchSerializer, DeleteSerializer
from .models import Book
from .utils import API_request, get_book_by_id, save_book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics, filters, status


# Create your views here.
class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        books = Book.objects.all()

        title = self.request.GET.get('title')

        if title:
            books = books.filter(nombre__contains=title)

        return books


class BookSearchView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'subtitle', 'authors__name']
    data = serializer_class.data


@api_view(['GET'])
def SearchBook(request):
    if request.method == 'GET':
        response = {}
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            to_search = serializer.data['search_term']
            service = 'local'
            data = API_request(to_search, service)
            if len(data) == 0:
                service = serializer.data['alternative_service']
                data = API_request(to_search, service)
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def SaveBook(request):
    if request.method == 'POST':
        google_book_id = request.GET.get('book_id_g')
        orelly_book_id = request.GET.get('book_id_o')

        if google_book_id:
            data = get_book_by_id(google_book_id, 'G')
            save_book(data, 'G')
        elif orelly_book_id:
            data = get_book_by_id(orelly_book_id, 'O')
            save_book(data, 'O')

        return Response(data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def DeleteBook(request):
    serializer = DeleteSerializer(data=request.data)
    if serializer.is_valid():
            book_id = serializer.data['id']
            Book.objects.get(id=book_id).delete()
    return Response()
