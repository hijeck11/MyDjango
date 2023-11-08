from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .forms import UserForm



from django.shortcuts import render
from .models import Event, Registration

def event_list(request):
    events = Event.objects.all()
    registrations = Registration.objects.select_related('event').all()

    context = {
        'events': events,
        'registrations': registrations,
    }

    return render(request, 'event_list.html', context)

def home(request):
    return HttpResponse('<h1>Главная</h1>')

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

def user_list(request):
    registrations = Registration.objects.all()
    return render(request, 'user_list.html', {'registrations': registrations})

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})