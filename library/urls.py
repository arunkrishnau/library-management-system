from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BookListView, BorrowBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),

    # JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]