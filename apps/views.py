from .models import Company, Property
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from math import ceil
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    Companys = Company.objects.all()
    n = len(Companys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        1, nSlides), 'Company': Companys}
    return render(request, 'index.html', params)


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if len(username) < 6:
            messages.error(
                request, " Your user name must be under 6 characters")
            return redirect('apps')
        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('apps')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('apps')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, " Your account has been successfully created")

        subject = "Thanks for register your site"
        message = "Hello " + myuser.username + "!! \n" + \
            "Thank you for visiting our website"
        from_email = 'imking3110@gmail.com'
        to_list = [myuser.email]
        send_mail(
            subject,
            message,
            from_email,
            to_list,
        )
        return redirect('apps')
    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            return render(request, 'Login.html')
    return render(request, 'Login.html')


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')


def propsell(request):
    prop = Property.objects.all()
    context = {'prop': prop}
    return render(request, 'propsell.html', context)


def buy(request):
    return render(request, 'buy.html')


def cdata(request):
    if request.method == "POST":
        Company_name = request.POST['Company_name']
        Location = request.POST['Location']
        value = request.POST['value']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        Company_detail = request.POST['Company_detail']
        image = request.POST['image']

        if len(Company_name) < 5 or len(Location) < 4 or len(Phone) < 10 or len(Email) < 5:
            messages.error(request, "Please fill the form correctly")
        else:
            cdata = Company(Company_name=Company_name, Location=Location, value=value,
                            Phone=Phone, Email=Email, Company_detail=Company_detail, image=image)
            cdata.save()
            messages.success(request, "Your Data has been successfully add")
    return render(request, 'cdata.html')


def pdata(request):
    if request.method == "POST":
        image = request.POST['image']
        Name = request.POST['Name']
        location = request.POST['location']
        type = request.POST['type']
        Relation = request.POST['Relation']
        value = request.POST['value']
        detail = request.POST['detail']
        Phone = request.POST['Phone']
        if len(Name) < 5 or len(location) < 4 or len(Phone) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            pdata = Property(image=image, Name=Name, location=location,
                             type=type, Relation=Relation, value=value, detail=detail, Phone=Phone)
            pdata.save()
            messages.success(request, "Your Data has been successfully add")
    return render(request, 'pdata.html')


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Property.objects.none()
    else:
        allPostsName = Property.objects.filter(Name__icontains=query)
        allPoststype = Property.objects.filter(type__icontains=query)
        allPosts = allPostsName.union(allPoststype)

    if allPosts.count() == 0:
        messages.warning(
            request, "No search results found. Please refine your query")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)


def Contact(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        message = request.POST['message']
# send mail
        send_mail(
            Name,
            Email,
            message,
            ['imking3110@gmail.com']
        )
        return render(request, 'Contact.html', {'Name': Name, 'Email': Email, 'message': message})
    else:
        return render(request, 'Contact.html')
