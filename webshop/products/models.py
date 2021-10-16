from django.db import models
from django.db.models.deletion import CASCADE


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(help_text='in US dolars')
    description = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    sku = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}. {self.name} - {self.created.strftime('%d/%m/%y')}"


class ProductImage(models.Model):
    link = models.TextField()
    product_image = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')

    def __str__(self):
        return f"{self.id}. {self.link}; {self.product_image}"