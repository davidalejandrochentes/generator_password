from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'generator/index.html', {})

def about(request):
    return render(request, 'generator/about.html', {})

def password(request):
    
    caracter = list('qwertyuiopasdfghjklzxcvbnm')
    password_generada = ''

    largo =  int(request.GET.get('largo'))

    if request.GET.get('uppercase'):
        caracter.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('especiales'):
        caracter.extend(list('~!@#$%^&*_+='))

    if request.GET.get('numero'):
        caracter.extend(list('1234567890'))        

    for x in range(largo):
        password_generada += random.choice(caracter)

    contex = {
       'password': password_generada
    }

    return render(request, 'generator/password.html', contex)
