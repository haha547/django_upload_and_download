# Generated by Django 4.1 on 2022-09-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileModel",
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
                ("doc", models.FileField(upload_to="media/")),
            ],
        ),
    ]