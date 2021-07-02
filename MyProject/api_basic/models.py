from django.db import models

class Industry(models.Model):
    industry_name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=3, primary_key=True)

    class Meta:
        ordering = ['industry_name']

    def __str__(self):
        return self.industry_name


class SubIndustry(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Company(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    sub_industry = models.ForeignKey(SubIndustry, on_delete=models.CASCADE)

    # aslinda her sub_industry icin bir industry var

    class Meta:
        ordering = ['symbol']

    def __str__(self):
        return self.symbol


class Index(models.Model):
    companies = models.ManyToManyField(Company)
    symbol = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['symbol']

    def __str__(self):
        return self.symbol