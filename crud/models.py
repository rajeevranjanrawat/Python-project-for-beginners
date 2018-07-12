from django.db import models

# Create your models here.


class Employee(models.Model):
    #emp_id = models.CharField(max_length=10, primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=250, default=None)
    phone = models.CharField(max_length=50, default=None)


    class Meta:

        db_table = 'employee'

    def __str__(self):
        return self.emp_email  # to overrite the whole table and will show only emp_nmae in other class
#############################################################

class Education(models.Model):
    #models.CASCADE
    #models.PROTECT

    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    edu_name = models.CharField(max_length=50)
    edu_type = models.CharField(max_length=50)
    edu_uni = models.CharField(max_length=50)

    def __str__(self):
        return self.edu_name