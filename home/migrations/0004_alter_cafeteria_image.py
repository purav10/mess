# Generated by Django 4.1.2 on 2023-01-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cafeteria_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafeteria',
            name='image',
            field=models.ImageField(upload_to='home/static/images', verbose_name='Image of Cafeteria'),
        ),
    ]
