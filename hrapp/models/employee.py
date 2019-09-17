from django.db import models

class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField()
    is_supervisor = models.BooleanField()
    # foreign key for dept?

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
