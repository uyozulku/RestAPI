from rest_framework import serializers
from .models import Industry, SubIndustry, Company, Index


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['industry_name', 'symbol']


class SubIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubIndustry
        fields = ['name', 'industry']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['symbol', 'name', 'industry', 'sub_industry']


class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ['symbol', 'name']

