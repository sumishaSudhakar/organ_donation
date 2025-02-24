from django.db import models
from accounts.models import UserDetails,Organ,BloodGroup

# Create your models here.
class Donor(models.Model):
    donor_id = models.OneToOneField(UserDetails, on_delete=models.CASCADE, related_name='donor_record')
    donated_organ = models.ForeignKey(Organ, on_delete=models.CASCADE, related_name='donated_organs')
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, related_name='donor_blood_groups')