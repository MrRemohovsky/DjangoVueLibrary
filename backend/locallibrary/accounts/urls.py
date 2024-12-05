from django.urls import path
from .views import RegisterView, LogoutView, LoanedBooksView, UserInfoGroupView, AllLoanedBooksView, \
    ResetPasswordRequest, ResetPasswordConfirm
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('borrower/', LoanedBooksView.as_view(), name='borrower'),
    path('user_info/', UserInfoGroupView.as_view(), name='user_info'),
    path('all_borrower/', AllLoanedBooksView.as_view(), name='all_borrower'),
    path('reset_password_request/', ResetPasswordRequest.as_view(), name='reset_password_request'),
    path('reset_password_confirm/<str:token>/', ResetPasswordConfirm.as_view(), name='reset_password_confirm'),

]