from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    image_url = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of book"""
        return f"{self.title} by {self.author}, {self.date.year}."