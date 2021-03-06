from django.db import (
    models,
)
from django.core.validators import (
    MinValueValidator,
)
from decimal import (
    Decimal,
)
from datetime import (
    date,
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
    name = models.CharField(max_length=90)
    occupation = models.CharField(max_length=90)
    hired_date = models.DateField(null=True)
    salary = models.DecimalField(
        max_digits=8, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    vacation_days = models.PositiveIntegerField()

    workgroup = models.ForeignKey(
        to=Workgroup, on_delete=models.SET_NULL, null=True
    )

    @property
    def experience(self):
        if not self.hired_date:
            return None

        today = date.today()
        # this and hire year difference  - 1 if hired-day hasn't come this year
        return today.year - self.hired_date.year - (
            (today.month, today.day)
            < (self.hired_date.month, self.hired_date.day)
        )

    def __str__(self):
        return f'{self.name} the {self.occupation}'
