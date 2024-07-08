from django.db import models
from django.urls import reverse
# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    


    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Book_detail", kwargs={"pk": self.pk})
