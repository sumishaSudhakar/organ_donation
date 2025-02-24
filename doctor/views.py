from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import BloodGroup, Organ
from doctor.models import DoctorDonor

def dochome(request):
    return render(request,'dochome.html')


def add_donor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        blood_group_id = request.POST.get("blood_group")
        organ_id = request.POST.get("organ")

        try:
            blood_group = BloodGroup.objects.get(id=blood_group_id)
            organ = Organ.objects.get(id=organ_id)

            donor = DoctorDonor.objects.create(
                name=name,
                blood_group=blood_group,
                organ=organ,
            )
            donor.save()  # Ensure it's saved
            return redirect("viewdonor_list")  # Redirect to donor list after adding
        except BloodGroup.DoesNotExist:
            return HttpResponse("Invalid Blood Group selected")
        except Organ.DoesNotExist:
            return HttpResponse("Invalid Organ selected")

    blood_groups = BloodGroup.objects.all()
    organs = Organ.objects.all()
    return render(request, "add_donor.html", {"blood_groups": blood_groups, "organs": organs})

def donor_list(request):
    donors = DoctorDonor.objects.all()  # Ensure correct model reference
    return render(request, "viewdonor_list.html", {"donors": donors})
