from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

def demo(request):
    return render(request,'index.html')




def Thrissur(request):
    response1 = redirect('https://en.wikipedia.org/wiki/Thrissur')
    return response1

def Ernakulam(request):
    response2 = redirect('https://en.wikipedia.org/wiki/Ernakulam')
    return response2

def Kozhikodu(request):
    response3 = redirect('https://en.wikipedia.org/wiki/Kozhikodu')
    return response3

def Kannur(request):
    response4 = redirect('https://en.wikipedia.org/wiki/Kannur')
    return response4

def Pathanamthitta(request):
    response5 = redirect('https://en.wikipedia.org/wiki/Pathanamthitta')
    return response5
