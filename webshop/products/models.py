from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(help_text='in US dolars')
    description = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products', default='no_picture.png')

    def __str__(self):
        return f"{self.id}. {self.name} - {self.created.strftime('%d/%m/%y')}"
