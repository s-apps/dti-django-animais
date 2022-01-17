from django.shortcuts import render
from animais.models import Animal

# Create your views here.


def home(request):
    animais = Animal.objects.all()
    data = {'animais': animais}
    return render(request, 'home.html', data)
