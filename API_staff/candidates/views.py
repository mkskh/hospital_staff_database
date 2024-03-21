from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Candidate
from rest_framework import generics
from .serializers import CandidateSerializer


def redirect_home(request):
    return redirect('candidates/')


class CandidateList(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateDetail(generics.RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateCreate(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateDelete(generics.RetrieveDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
