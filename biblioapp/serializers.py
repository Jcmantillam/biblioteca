from .models import Editor, Category, Author, Book
from .constants import SERVICE_CHOICES
from rest_framework import serializers

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
         model = Editor
         fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
         model = Category
         fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
         model = Author
         fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
         model = Book
         fields = '__all__'


class SearchSerializer(serializers.Serializer):
    search_term = serializers.CharField(max_length=200)
    alternative_service = serializers.ChoiceField(choices=SERVICE_CHOICES)


class DeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
