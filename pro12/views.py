from django.shortcuts import render


def login(request, email, password):
    return render(request, 'login.html', {'email':email, 'pass':password})


def home(request):
    return render(request, "home.html", {'home':"welcome"})


def aboutus(request):
    return render(request, "aboutus.html")
