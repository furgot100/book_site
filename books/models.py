from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length =100 )

    def __str__(self):
        return self.name 

class Author(models.Model):
    name = models.CharField(max_length = 100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    num_pages = models.IntegerField()
    date_published = models.DateField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title