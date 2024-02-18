from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonalInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    is_submitted = models.BooleanField(default=True)
    #undergraduate
    name_of_degree = models.CharField(max_length=100)
    admission_session = models.CharField(max_length=100)
    reg_id_no = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    year_of_passing = models.CharField(max_length=100)
    graduating_session = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=100)
    
    #graduate
    name_of_degree = models.CharField(max_length=100)
    admission_session = models.CharField(max_length=100)
    reg_id_no = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    year_of_passing = models.CharField(max_length=100)
    graduating_session = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=100)

    def __str__(self):
        return self.name
