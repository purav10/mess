# Generated by Django 4.1.2 on 2023-01-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_cafeteria_image_alter_contact_occupation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carousel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="static/images", verbose_name="Carousel Images"
                    ),
                ),
            ],
            options={
                "verbose_name": "Carousel",
                "verbose_name_plural": "Carousel",
            },
        ),
        migrations.CreateModel(
            name="Photos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="static/images",
                        verbose_name="Photographs on Home page",
                    ),
                ),
            ],
            options={
                "verbose_name": " general photographs",
                "verbose_name_plural": " general photographs",
            },
        ),
    ]
