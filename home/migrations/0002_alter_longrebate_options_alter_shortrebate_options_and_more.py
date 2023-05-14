# Generated by Django 4.1.2 on 2022-12-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="longrebate",
            options={
                "verbose_name": "Long Rebate",
                "verbose_name_plural": "Long Rebates",
            },
        ),
        migrations.AlterModelOptions(
            name="shortrebate",
            options={
                "verbose_name": "Short Rebate",
                "verbose_name_plural": "Short Rebate",
            },
        ),
        migrations.RemoveField(
            model_name="rule",
            name="id",
        ),
        migrations.AddField(
            model_name="rule",
            name="sno",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="about",
            name="description",
            field=models.TextField(
                help_text="The text added in this text field will show up in the about section of the home page.",
                verbose_name="Description",
            ),
        ),
        migrations.AlterField(
            model_name="cafeteria",
            name="contact",
            field=models.CharField(
                blank=True,
                help_text="This contains the contact(phone number) of the POC",
                max_length=10,
                null=True,
                verbose_name="Phone Number",
            ),
        ),
        migrations.AlterField(
            model_name="cafeteria",
            name="name",
            field=models.CharField(
                help_text="This contains the name of the cafeteria",
                max_length=30,
                verbose_name="Name of Cafeteria",
            ),
        ),
        migrations.AlterField(
            model_name="cafeteria",
            name="poc",
            field=models.CharField(
                help_text="This contains the name of the point of contact of the respective cafeteria",
                max_length=30,
                verbose_name="Point of Contact",
            ),
        ),
        migrations.AlterField(
            model_name="caterer",
            name="lower_description",
            field=models.TextField(
                help_text="This contains the description of the respective caterer that will show on the lower side.",
                verbose_name="Lower Discription",
            ),
        ),
        migrations.AlterField(
            model_name="caterer",
            name="name",
            field=models.CharField(
                help_text="The text in this text field contains the caterer name.",
                max_length=50,
                verbose_name="Caterer Name",
            ),
        ),
        migrations.AlterField(
            model_name="caterer",
            name="sheet_url",
            field=models.URLField(
                help_text="This contains the google sheets url link for the respective caterers menu.",
                verbose_name="Menu URL",
            ),
        ),
        migrations.AlterField(
            model_name="caterer",
            name="upper_description",
            field=models.TextField(
                help_text="This contains the description of the respective caterer that will show on the upper side.",
                verbose_name="Upper Description",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="contact",
            field=models.CharField(
                blank=True,
                help_text="This contains phone number of the contact to be added",
                max_length=10,
                null=True,
                verbose_name="Phone Number",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(
                help_text="This contains email of the contact to be added",
                max_length=254,
                verbose_name="Email",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="This contains the name of the contact to be added",
                max_length=30,
                null=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="occupation",
            field=models.CharField(
                help_text="This contains the occupation of the contact to be added",
                max_length=5,
                verbose_name="Occupation",
            ),
        ),
        migrations.AlterField(
            model_name="form",
            name="description",
            field=models.CharField(
                help_text="This contains the description of the form to be added.",
                max_length=120,
                verbose_name="Form Description",
            ),
        ),
        migrations.AlterField(
            model_name="form",
            name="heading",
            field=models.CharField(
                help_text="This contains the heading of the form to be added.",
                max_length=30,
                verbose_name="Form Heading",
            ),
        ),
        migrations.AlterField(
            model_name="form",
            name="url",
            field=models.URLField(
                help_text="This contains the URL link of the form.",
                verbose_name="Form URL",
            ),
        ),
        migrations.AlterField(
            model_name="longrebate",
            name="rule",
            field=models.TextField(
                help_text="The text in the text field contains the rule that will show as one of the long rebate rules of the rule page.",
                verbose_name="Rule",
            ),
        ),
        migrations.AlterField(
            model_name="penalty",
            name="penalty",
            field=models.TextField(
                help_text="The text in the text field contains the penalty that will show as one of the penalties of the rule page.",
                verbose_name="Penalty",
            ),
        ),
        migrations.AlterField(
            model_name="rule",
            name="rule",
            field=models.TextField(
                help_text="The text in the text field contains the rule that will show as one of the rules of the rule page.",
                verbose_name="Rule",
            ),
        ),
        migrations.AlterField(
            model_name="shortrebate",
            name="Memebers",
            field=models.TextField(
                help_text="The text in the text field contains the names of the members that will handle the short rebate.",
                verbose_name="Members",
            ),
        ),
        migrations.AlterField(
            model_name="shortrebate",
            name="biling",
            field=models.TextField(
                help_text="The text in the text field contains the billing description for the short rebate.",
                verbose_name="bilings",
            ),
        ),
        migrations.AlterField(
            model_name="shortrebate",
            name="circulation",
            field=models.TextField(
                help_text="The text in the text field contains the circulation text of the short rebate form.",
                verbose_name="Circulation",
            ),
        ),
        migrations.AlterField(
            model_name="shortrebate",
            name="desc",
            field=models.TextField(
                help_text="The text in the text field contains the description of the short rebate.",
                verbose_name="Description",
            ),
        ),
        migrations.AlterField(
            model_name="shortrebate",
            name="infoToCaterer",
            field=models.TextField(
                help_text="The text in the text field contains the information to the caterers for the short rebate form.",
                verbose_name="Info to the Caterer",
            ),
        ),
        migrations.AlterField(
            model_name="shortrebate",
            name="link",
            field=models.URLField(
                help_text="The link in this field contains the link of the short rebate google form.",
                verbose_name="Link",
            ),
        ),
        migrations.AlterField(
            model_name="shortrebate",
            name="note",
            field=models.TextField(
                help_text="The text in the text field contains the note for the short rebate form.",
                verbose_name="Note",
            ),
        ),
        migrations.AlterField(
            model_name="shortrebate",
            name="policy",
            field=models.TextField(
                help_text="The text in the text field contains the policies of the short rebate.",
                verbose_name="Policy",
            ),
        ),
        migrations.AlterField(
            model_name="update",
            name="time_stamp",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="time stamp of the update will also show up on the page and this also decides the order of the updates that show up",
            ),
        ),
        migrations.AlterField(
            model_name="update",
            name="update",
            field=models.CharField(
                help_text="The text added in this text field will show as one of the update in the update section",
                max_length=120,
                verbose_name="update",
            ),
        ),
    ]
