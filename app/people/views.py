from django_filters.rest_framework import DjangoFilterBackend
from people.helpers import get_age_from_dob
from people.models import People
from people.serializers import PeopleSerializer
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView


class PeopleViewSet(viewsets.ModelViewSet):
    """
    People ViewSet
    """

    queryset = People.objects.all().order_by("years_of_experience")
    serializer_class = PeopleSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = "__all__"


class AverageSalariesStatistics(APIView):
    """
    Average salaries per industry and years of experience
    """

    def get(self, *args, **kwargs):
        df = People.get_dataframe()
        avg_salary_per_industry = df.groupby("industry").salary.mean().to_dict()
        avg_salary_per_experience = df.groupby("years_of_experience").salary.mean().to_dict()

        data = {
            "avg_salary_per_industry": avg_salary_per_industry,
            "avg_salary_per_experience": avg_salary_per_experience,
        }

        return Response(data=data, status=status.HTTP_200_OK)


class AverageAgeStatistics(APIView):
    """
    Average age per industry and years of experience
    """

    def get(self, *args, **kwargs):
        df = People.get_dataframe()

        df["age"] = df["date_of_birth"].apply(get_age_from_dob)
        avg_age_per_industry = df.groupby("industry").age.mean().to_dict()
        avg_age_per_experience = df.groupby("years_of_experience").age.mean().to_dict()

        data = {
            "avg_age_per_industry": avg_age_per_industry,
            "avg_age_per_experience": avg_age_per_experience,
        }

        return Response(data=data, status=status.HTTP_200_OK)
