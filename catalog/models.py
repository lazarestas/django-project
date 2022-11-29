from django.db import models
from django.urls import reverse


class Books(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    uid = models.AutoField(primary_key=True, default=True)
    title = models.CharField(max_length=20, help_text='Enter book title')
    pubdate = models.DateTimeField(auto_now_add=True)
    book_file = models.FilePathField(help_text='Path to book file (needs testing)')
    # …
    # Metadata

    class Meta:
        ordering = ['title', '-pubdate']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title
