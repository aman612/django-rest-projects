from django.db import models
from django.urls import reverse
# Create your models here.


class Todo(models.Model):

    title = models.CharField(max_length=250)
    body = models.TextField()

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Todo_detail", kwargs={"pk": self.pk})
