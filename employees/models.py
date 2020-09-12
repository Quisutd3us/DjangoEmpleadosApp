from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES=[
        ('m','HOMBRE'),
        ('f','FEMENINO'),
    ]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField(max_length=255)
    phone_num=models.CharField(max_length=35)
    employee_gender=models.CharField(choices=GENDER_CHOICES, max_length=1)
    employee_address=models.TextField()
    #funcitonal relation with AvailableJobs
    employee_job=models.ManyToManyField('AvailableJobs', blank=True)
    date_of_birth= models.DateField()

class AvailableJobs(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

