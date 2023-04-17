# Generated by Django 4.2 on 2023-04-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventman", "0003_formsubmission_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="formsubmission",
            name="slug",
        ),
        migrations.AlterField(
            model_name="formsubmission",
            name="page_url",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
