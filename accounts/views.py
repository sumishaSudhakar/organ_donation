from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts.models import UserDetails, BloodGroup,Organ
from doctor.models import DoctorDetails
from donor.models import Donor
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        place = request.POST['place']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        phone = request.POST['phone']
        blood_group_id = request.POST['blood_group']
        organ_id = request.POST['organ']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        blood_group = BloodGroup.objects.get(id=blood_group_id)
        organ = Organ.objects.get(id=organ_id)
        user_details = UserDetails.objects.create(
            name=name,
            email=email,
            place=place,
            district=district,
            state=state,
            pin=pin,
            phone=phone,
            blood_group=blood_group,
            organ_name=organ  
        )
        user.save()
        messages.success(request, "Registration successful! You can log in now.")
        return redirect('login')

    blood_groups = BloodGroup.objects.all()
    organs = Organ.objects.all() 
    return render(request, "register.html", {
        "blood_groups": blood_groups,
        "organs": organs})  



def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('userhome')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')

@login_required
def view_profile(request):
    user_details = UserDetails.objects.get(email=request.user.email)
    organs_donated = Organ.objects.filter(userdetails=user_details)  # Ensure this matches your relationships
    return render(request, "profile.html", {
        "user_details": user_details,
        "organs_donated": organs_donated
    })

@login_required
def edit_profile(request):
    user_details = UserDetails.objects.get(email=request.user.email)

    if request.method == "POST":
        user_details.name = request.POST['name']
        user_details.place = request.POST['place']
        user_details.district = request.POST['district']
        user_details.state = request.POST['state']
        user_details.pin = request.POST['pin']
        user_details.phone = request.POST['phone']
        blood_group_id = request.POST['blood_group']
        user_details.blood_group = BloodGroup.objects.get(id=blood_group_id)
        organ_id = request.POST['organ']
        user_details.organ_name = Organ.objects.get(id=organ_id)
        
        user_details.save()
        messages.success(request, "Profile updated successfully")
        return redirect('profile')

    blood_groups = BloodGroup.objects.all()
    organ = Organ.objects.all()
    return render(request, "edit_profile.html", {"user_details": user_details, "blood_groups": blood_groups, "organs": organ})  # ✅ Renamed "organ" to "organs"

@login_required
def delete_profile(request):
    if request.method == "POST":
        user = request.user
        user_details = UserDetails.objects.get(email=user.email)
        user_details.delete()
        user.delete()
        messages.success(request, "Profile deleted successfully")
        return redirect('register')

    return render(request, "delete_profile.html")

def doctor_list(request):
    doctors = DoctorDetails.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'donor_list.html', {'donors': donors})

    
def donated_organs_list(request):
    donors = UserDetails.objects.filter(organ_name__isnull=False)
    return render(request, "donated_organs.html", {"donors": donors})