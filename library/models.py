from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField()
    available = models.BooleanField(default=True)

    def _str_(self):
        return self.title

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_on = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.user.username} - {self.book.title}"