from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=100, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    lang = models.ForeignKey('Language', on_delete=models.PROTECT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    def display_title(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return self.book.title

    display_title.short_description = 'Title'

    class Meta:
        ordering = ['due_back']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('lang-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'


class Language(models.Model):
    """MODEL FOR LANGUAGE SAMODELKA"""
    # lang_selector = (
    #     ('ru', 'Russian'),
    #     ('en', 'English'),
    #     ('fa', 'Farsi'),
    #     ('fr', 'French'),
    #     ('ua', 'Ukrainian'),
    # )
    # # https://meta.wikimedia.org/wiki/Template:List_of_language_names_ordered_by_code
    #
    # language_name = models.CharField(
    #     max_length=2,
    #     choices=lang_selector,
    #     blank=True,
    #     default='ru',
    #     help_text='Book language',
    # )
    name = models.CharField(max_length=20, help_text='Enter a book language')

    class Meta:
        ordering = ['id']

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


# class Books(models.Model):
#     """A typical class defining a model, derived from the Model class."""
#     # Fields
#     uid = models.AutoField(primary_key=True, default=True)
#     title = models.CharField(max_length=20, help_text='Enter book title')
#     pubdate = models.DateTimeField(auto_now_add=True)
#     book_file = models.FilePathField(help_text='Path to book file (needs testing)')
#
#     # …
#     # Metadata
#
#     class Meta:
#         ordering = ['title', '-pubdate']
#
#     # Methods
#     def get_absolute_url(self):
#         """Returns the URL to access a particular instance of MyModelName."""
#         return reverse('model-detail-view', args=[str(self.id)])
#
#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.title
