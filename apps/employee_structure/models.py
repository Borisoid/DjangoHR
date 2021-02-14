from django.db import (
    models,
)


class Department(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)


class Workgroup(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE)


class Employee(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    ocupation = models.CharField(max_length=90, null=False, blank=False)
    experience = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    vacation_days = models.PositiveIntegerField()

    workgroup = models.ForeignKey(
        to=Workgroup, on_delete=models.SET_NULL, null=True
    )
