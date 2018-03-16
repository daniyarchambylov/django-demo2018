from django.db import models


class Colors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brands(models.Model):
    name = models.CharField(max_length=100)

    def get_cars_by_brand_name(self, name):
        return self.cars.filter(brand__icontains=name)
    
    def count_cars(self):
        return self.cars.all().count()

    def __str__(self):
        return self.name

    # def get_brands(self):
    #     return self.brands.all()
    

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=30, blank=True)
    brand = models.CharField(max_length=30)
    brnd = models.ForeignKey(
        Brands,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    col = models.ManyToManyField(
        Colors,
        related_name='cars'
    )

    year = models.IntegerField()

    def __str__(self):
        return f'{self.brand} {self.name} {self.year}'

    @classmethod
    def get_last_three_and_brands(cls, length = 3):
        cars = cls.objects.order_by('-name')[:length]
        cars = cls.objects.select_related().order_by('-name')[:length]
        return cars
    
