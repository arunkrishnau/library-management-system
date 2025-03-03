from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book, Loan

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            isbn="1234567890123",
            page_count=200,
            available=True
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "John Doe")
        self.assertTrue(self.book.available)

class LoanModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.book = Book.objects.create(
            title="Another Book",
            author="Jane Doe",
            isbn="9876543210987",
            page_count=150,
            available=True
        )
        self.loan = Loan.objects.create(user=self.user, book=self.book)

    def test_loan_creation(self):
        self.assertEqual(self.loan.user.username, "testuser")
        self.assertEqual(self.loan.book.title, "Another Book")
