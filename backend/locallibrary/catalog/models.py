import uuid
import isbnlib
import random
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
    author = models.ManyToManyField('Author')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField(verbose_name="ISBN",max_length=17,
                            help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
                            unique=True, blank=True)

    genre = models.ManyToManyField('Genre', help_text='Select a genre')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, help_text='Select a language')

    def __str__(self):
        return self.title

    def generate_isbn(self):
        prefix = "978"
        group = str(random.randint(1000, 9999))
        publisher = str(random.randint(100000, 999999))
        check_digit = str(random.randint(0, 9))
        return f"{prefix}-{group}-{publisher}-{check_digit}"

    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = self.generate_isbn()
        super().save(*args, **kwargs)

    def display_author(self):
        return ', '.join([f'{author.first_name} {author.last_name}' for author in self.author.all()])
    display_author.short_description = 'Author'

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])
    display_genre.short_description = 'Genre'

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
