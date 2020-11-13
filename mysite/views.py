from django.shortcuts import render


def HomePage(request):
    return render(request, "home/homePage.html")


def TestBase(request):
    return render(request, "home/NavBarBase.html")


def AboutAndCredits(request):
    return render(request, "home/AboutAndCredits.html")
