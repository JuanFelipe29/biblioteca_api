from rest_framework import serializers
from .models import Book
from authors.models import Author
from authors.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True,read_only=True)
    authorId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Author.objects.all(), source='authors',many=True)
    class Meta:
        model = Book
        fields = ['id','title','authorId','authors']
        
    def create(self, validated_data):
        author_data = validated_data.pop('authors',[])
        book = Book.objects.create(**validated_data)
        book.authors.set(author_data)
        return book