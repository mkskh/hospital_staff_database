from django.urls import path
from . import views


app_name = "candidates"

urlpatterns = [
    path("", views.CandidateList.as_view()),
    path("create/", views.CandidateCreate.as_view(), name="create"),
    path("delete/<int:pk>/", views.CandidateDelete.as_view(), name="delete"),
    path("<int:pk>/", views.CandidateDetail.as_view(), name="detail"),
]