# Generated by Django 4.1.2 on 2023-01-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_carousel_photos"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="photos",
            options={
                "verbose_name": " General Photographs",
                "verbose_name_plural": " General Photographs",
            },
        ),
        migrations.AddField(
            model_name="photos",
            name="occupation",
            field=models.CharField(
                default="SOME STRING",
                help_text="This contains the occupation of the person in the photograph",
                max_length=50,
                verbose_name="Occupation",
            ),
        ),
        migrations.AddField(
            model_name="photos",
            name="poc",
            field=models.CharField(
                default="SOME STRING",
                help_text="This contains the name of the person in the photograph",
                max_length=30,
                verbose_name="Point of Contact",
            ),
        ),
    ]
