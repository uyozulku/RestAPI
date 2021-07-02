from django.shortcuts import render
from rest_framework import generics
from .models import Industry, SubIndustry, Company, Index
from .serializer import IndustrySerializer, SubIndustrySerializer, CompanySerializer, IndexSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

class ListIndustry(generics.ListCreateAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

class ListSubIndustry(generics.ListCreateAPIView):
    queryset = SubIndustry.objects.all()
    serializer_class = SubIndustrySerializer

class ListCompany(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ListIndex(generics.ListCreateAPIView):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer


