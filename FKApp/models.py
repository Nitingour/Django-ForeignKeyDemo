from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:#to resolve plural spell mistake in admin panel
        verbose_name_plural='categories'


# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=30)
    starrating=models.IntegerField()
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    #if we delete category. all moovie related to that category
    #autometically deleted
    def __str__(self):
        return self.name
