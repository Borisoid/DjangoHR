from django.db import (
    models,
)


class Department(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)

    def __str__(self):
        return self.name


class Workgroup(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    occupation = models.CharField(max_length=90, null=False, blank=False)
    experience = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    vacation_days = models.PositiveIntegerField()

    workgroup = models.ForeignKey(
        to=Workgroup, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f'{self.name} the {self.occupation}'
