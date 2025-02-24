from django.db import models



class BloodGroup(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, unique=True)

    def __str__(self):
        return self.blood_group
    
class Organ(models.Model):
    organ_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.organ_name

class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    place = models.CharField(max_length=50,default=1)
    district = models.CharField(max_length=50,default=1)
    state = models.CharField(max_length=50,default=1)
    pin = models.CharField(max_length=20,default=1)
    phone = models.CharField(max_length=15)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    organ_name = models.ForeignKey(Organ, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

