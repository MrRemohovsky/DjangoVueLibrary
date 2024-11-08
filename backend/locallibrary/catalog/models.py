import uuid
import isbnlib
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre (e.g. Science Fiction, Poetry etc.)')
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(verbose_name='Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            help_text="Enter a book's natural language (e.g. Russian, English, Japanese etc.)")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField(verbose_name="ISBN",
                            help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
                            default=isbnlib.ISBN13,
                            unique=True,
                            editable=False)

    genre = models.ManyToManyField('Genre', on_delete=models.SET_NULL, null=True, help_text='Select a genre')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, help_text='Select a language')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '{} {}'.format(self.id, self.book.title)
