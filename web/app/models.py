from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Advert(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='adverts')
    category = models.ManyToManyField(Category, related_name='adverts')
    views = models.IntegerField(default=0)

    def __str__(self):
        categories = ", ".join([category.name for category in self.category.all()])
        return f'категории: {categories}, наименование: {self.title}, город: {self.city}, просмотры: {self.views}'
