# Generated by Django 3.1.7 on 2021-10-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='no_picture.png', upload_to='products')),
            ],
        ),
    ]
