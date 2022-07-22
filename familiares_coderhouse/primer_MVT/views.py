from django.shortcuts import render
from .models import Familiar

# Create your views here.
def home(request):
    familiares = Familiar.objects.all()
    context = {'familiares': familiares}
    return render(request, 'home.html', context=context)