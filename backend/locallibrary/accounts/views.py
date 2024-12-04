from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoanedBooksSerializer
from catalog.models import BookInstance
from accounts.tasks import send_reset_mail
from rest_framework_simplejwt.tokens import AccessToken

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

class ResetPasswordRequest(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({"detail": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)

        reset_link = f'http://localhost:8000/api/accounts/reset-password-confirm/{token}/'

        send_reset_mail(
            'Password Reset Request',
            f'You can reset your password using this link: {reset_link}',
            'from@example.com',
            [email],
        )

        return Response({"detail": "Password reset email sent."}, status=status.HTTP_200_OK)


class ResetPasswordConfirm(APIView):
    def post(self, request, token):
        try:
            access_token = AccessToken(token)
            user = User.objects.get(id=access_token['user_id'])
        except Exception as e:
            raise AuthenticationFailed("Invalid token or token expired.")

        new_password = request.data.get('new_password')

        if not new_password:
            return Response({"detail": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password has been successfully reset."}, status=status.HTTP_200_OK)















