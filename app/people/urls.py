from django.urls import include, path
from people import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"people", views.PeopleViewSet, basename="people")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("avg_salaries", views.AverageSalariesStatistics.as_view(), name="avg-salaries"),
    path("avg_age", views.AverageAgeStatistics.as_view(), name="avg-age"),
]
