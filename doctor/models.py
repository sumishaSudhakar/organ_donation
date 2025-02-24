from django.db import models
from accounts.models import Organ,BloodGroup

# Create your models here.

class DoctorDetails(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Organ,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)

class DoctorDonor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.blood_group.blood_group} - {self.organ.organ_name}"