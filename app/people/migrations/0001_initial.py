# Generated by Django 4.2.6 on 2023-10-31 08:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="People",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=200, unique=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(blank=True, max_length=10, null=True),
                ),
                ("industry", models.CharField(blank=True, max_length=200)),
                ("salary", models.FloatField(blank=True)),
                ("years_of_experience", models.FloatField(blank=True)),
            ],
        ),
    ]
