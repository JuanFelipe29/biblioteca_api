from rest_framework import serializers

from .models import Review
from books.models import Book
from users.models import User
from books.serializers import BookSerializer
from users.serializers import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    bookId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Book.objects.all(), source='book')
    user = UserSerializer(read_only=True)
    userId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')
    class Meta:
        model = Review
        fields = ['id','bookId','book','userId','user','comment','created_ad']