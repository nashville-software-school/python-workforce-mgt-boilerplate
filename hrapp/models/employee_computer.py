from django.db import models

class EmployeeComputer(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    Author: Joe Shep
    methods: none
    """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    computer = models.ForeignKey("Computer", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("EmployeeComputer")
        verbose_name_plural = ("EmployeeComputers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EmployeeComputer_detail", kwargs={"pk": self.pk})
