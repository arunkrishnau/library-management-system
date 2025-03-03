from rest_framework import generics, permissions
from .models import Book, Loan
from .serializers import BookSerializer, LoanSerializer

# View available books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(available=True)
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can see books

# Borrow a book
class BorrowBookView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can borrow

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.available:  # Check if book is available
            book.available = False  # Mark as borrowed
            book.save()
            serializer.save(user=self.request.user)  # Save loan under user
        else:
            raise serializers.ValidationError("This book is not available for borrowing.")
