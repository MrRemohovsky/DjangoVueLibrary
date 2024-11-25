from asyncio import AbstractEventLoopPolicy

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoanedBooksSerializer
from catalog.models import BookInstance


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Пользователь был успешно создан!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out"}, status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Invalid token or already blacklisted"}, status.HTTP_400_BAD_REQUEST)

class LoanedBooksView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        borrowed_books = BookInstance.objects.filter(borrower=user)
        serializer = LoanedBooksSerializer(borrowed_books, many=True)
        return Response(serializer.data)

class UserInfoGroupView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        groups = user.groups.values_list('name', flat=True)
        return Response(
            {
                "user": user.username,
                "groups":list(groups)
            }
        )
class AllLoanedBooksView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        borrowed_books = BookInstance.objects.filter(status__exact='o')
        serializer = LoanedBooksSerializer(borrowed_books, many=True)
        return Response(serializer.data)



















