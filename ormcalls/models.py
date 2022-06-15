from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class BlogEntry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline =  models.CharField(max_length=200)
    published_data = models.DateField()
    authors = models.ManyToManyField(Author)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.headline

