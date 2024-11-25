from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from catalog.models import BookInstance, Book


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoanedBooksSerializer(ModelSerializer):
    title = serializers.StringRelatedField(source='book.title')
    is_overdue = serializers.BooleanField(read_only=True)
    class Meta:
        model = BookInstance
        fields = ['title', 'book', 'due_back', 'is_overdue']



