from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
import os

from .models import Profile


def BASE(request):
    src = request.GET.get('src')
    if src:
        allProfile = Profile.objects.filter(Q(Name__icontains = src) | Q(email__icontains = src))
    elif src == 'None' :
        allProfile = Profile.objects.all()    
    else:
        allProfile = Profile.objects.all()

    context = {
        'Prof': allProfile,
        'src' : src
    }
    return render(request, 'Home.html', context)


def profile(request, id):
    prof = Profile.objects.get(id=id)
    return render(request, 'Profile.html', locals())


def Create(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        img = request.FILES.get('img')
        if img:
            if name:
                a = Profile.objects.create(Name=name, email=email, age=age, gender=gender, image=img, phone=phone,
                                    address=address)
                a.save()
                return redirect ('Create')  
            else:
                messages.success(request, 'Please Fill All Field.')  
                return redirect ('base')                     
        else:
            a = Profile.objects.create(Name=name, email=email, age=age, gender=gender, phone=phone,
                                    address=address)
            a.save()
            return redirect ('Create') 

        
            

        

    return render(request, 'createProfile.html')


def login(request):
    return render(request, 'log_in.html')


def registration(request):
    return render(request, 'reg.html')


def DeleteProfile(request, id):
    delete_prof = Profile.objects.get(id = id)
    if pro.image != "default/default.png":
        os.remove(pro.image.path)
    delete_prof.delete()
    messages.success(request, 'Profile Has been deleted.')
    return redirect('base')


def update(r, id):
    pro = Profile.objects.get(id = id)
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        phone = r.POST['phone']
        age = r.POST['age']    
        address = r.POST['address']    
        gender = r.POST['gender']    
        image = r.FILES.get('image') 
        
        if pro.image != "default/default.png":
            os.remove(pro.image.path)
        pro.image = image
        pro.Name = name      
        pro.email = email
        pro.phone = phone   
        pro.age = age 
        pro.address = address   
        pro.gender = gender
        pro.save()
        return redirect('base')

    return render(r, 'Update.html', locals())