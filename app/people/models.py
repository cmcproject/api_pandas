from django.db import models
from pandas import DataFrame


class GenderChoices(models.TextChoices):
    M = "M", "Male"
    F = "F", "Female"


class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=200)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True)
    date_of_birth = models.DateField(max_length=10, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True)
    salary = models.FloatField(blank=True)
    years_of_experience = models.FloatField(blank=True)

    def get_dataframe() -> DataFrame:

        return DataFrame.from_records(People.objects.all().values())
