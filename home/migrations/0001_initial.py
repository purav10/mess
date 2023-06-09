# Generated by Django 4.1.4 on 2022-12-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("description", models.TextField(verbose_name="Description")),
            ],
            options={
                "verbose_name": "About Us",
                "verbose_name_plural": "About Us",
            },
        ),
        migrations.CreateModel(
            name="Cafeteria",
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
                    "name",
                    models.CharField(max_length=30, verbose_name="Name of Cafeteria"),
                ),
                (
                    "poc",
                    models.CharField(max_length=30, verbose_name="Point of Contact"),
                ),
                (
                    "contact",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Phone Number",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cafeteria",
                "verbose_name_plural": "Cafeterias",
            },
        ),
        migrations.CreateModel(
            name="Caterer",
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
                ("name", models.CharField(max_length=50, verbose_name="Caterer Name")),
                (
                    "upper_description",
                    models.TextField(verbose_name="Upper Description"),
                ),
                ("sheet_url", models.URLField(verbose_name="Menu URL")),
                (
                    "lower_description",
                    models.TextField(verbose_name="Lower Discription"),
                ),
            ],
            options={
                "verbose_name": "Caterer",
                "verbose_name_plural": "Caterers",
            },
        ),
        migrations.CreateModel(
            name="Contact",
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
                    "occupation",
                    models.CharField(max_length=5, verbose_name="Occupation"),
                ),
                ("hostel_sec", models.BooleanField(verbose_name="Dining Secretary")),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Name"
                    ),
                ),
                (
                    "contact",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Phone Number",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
            },
        ),
        migrations.CreateModel(
            name="Form",
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
                    "heading",
                    models.CharField(max_length=30, verbose_name="From Heading"),
                ),
                (
                    "description",
                    models.CharField(max_length=120, verbose_name="Form Description"),
                ),
                ("url", models.URLField(verbose_name="Form URL")),
            ],
            options={
                "verbose_name": "Form",
                "verbose_name_plural": "Forms",
            },
        ),
        migrations.CreateModel(
            name="LongRebate",
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
                ("rule", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Penalty",
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
                ("penalty", models.TextField(verbose_name="Penalty")),
            ],
            options={
                "verbose_name": "Penalty",
                "verbose_name_plural": "Penalties",
            },
        ),
        migrations.CreateModel(
            name="Rule",
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
                ("rule", models.TextField(verbose_name="Rule")),
            ],
            options={
                "verbose_name": "Rule",
                "verbose_name_plural": "Rules",
            },
        ),
        migrations.CreateModel(
            name="ShortRebate",
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
                ("desc", models.TextField()),
                ("link", models.URLField()),
                ("policy", models.TextField()),
                ("circulation", models.TextField()),
                ("infoToCaterer", models.TextField()),
                ("note", models.TextField()),
                ("Memebers", models.TextField()),
                ("biling", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Update",
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
                ("update", models.CharField(max_length=120, verbose_name="update")),
                ("time_stamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Update",
                "verbose_name_plural": "Updates",
            },
        ),
    ]
