# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegisterForm,ConnexionForm,CreerAsso,CreerEvent,AfficheEvent
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from.models import Association, Event
from django.utils import timezone


# Create your views here.

#Vue qui sert pour s enregistrer
#Cree un utilisateur
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(index)
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

#Vue qui sert a se connecter
def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect(index)
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', locals())

#Vu qui te deconnecte
def deconnexion(request):
    logout(request)
    return redirect(index)

@login_required
def creerasso(request):
    existe = Association.objects.filter(admin_id=request.user.id).exists()
    if not existe:
        if request.method == "POST":
            form = CreerAsso(request.POST)
            if form.is_valid():
                asso = Association()
                asso.contact_email = form.cleaned_data.get('contact_email')
                asso.name = form.cleaned_data.get('name')
                asso.location = form.cleaned_data.get('location')
                asso.description = form.cleaned_data.get('description')
                asso.phone = form.cleaned_data.get('phone')
                asso.admin = request.user
                asso.save()
                return redirect(index)
        else:
            form = CreerAsso()
        return render(request, 'creerasso.html',locals())
    else:
        return render(request, 'creerasso.html',locals())

@login_required
def afficheasso(request):
    if Association.objects.filter(admin_id=request.user.id).exists():
        asso = Association.objects.get(admin_id = request.user.id)
    else:
        asso = None
    if asso != None:
        if request.method == "POST":
            form = CreerAsso(request.POST)
            if form.is_valid():
                asso.contact_email = form.cleaned_data.get('contact_email')
                asso.name = form.cleaned_data.get('name')
                asso.location = form.cleaned_data.get('location')
                asso.description = form.cleaned_data.get('description')
                asso.phone = form.cleaned_data.get('phone')
                asso.admin = request.user
                asso.save()
        else:
            form = CreerAsso()
            form.fields.get('contact_email').initial = asso.contact_email
            form.fields.get('name').initial = asso.name
            form.fields.get('location').initial = asso.location
            form.fields.get('description').initial = asso.description
            form.fields.get('phone').initial = asso.phone
        return render(request, 'afficheasso.html',locals())
    else:
        return render(request, 'afficheasso.html',locals())

@login_required
def creerevent(request):
    if Association.objects.filter(admin_id=request.user.id).exists():
        asso = Association.objects.get(admin_id = request.user.id)
    else:
        asso = None
    if asso != None:
        if request.method == "POST":
            form = CreerEvent(request.POST)
            if form.is_valid():
                event = Event()
                event.organizer = asso
                event.name = form.cleaned_data.get('name')
                event.start_datetime = form.cleaned_data.get('start_datetime')
                event.active = form.cleaned_data.get('active')
                event.description = form.cleaned_data.get('description')
                event.save()
                return redirect(index)
        else:
            form = CreerEvent()
        return render(request, 'creerevent.html',locals())
    else:
        return render(request, 'creerevent.html',locals())

def afficherevent(request):
    #Filtres
    if Association.objects.filter(admin_id=request.user.id).exists():
        asso = Association.objects.get(admin_id = request.user.id)
    else:
        asso = None
    actif = False
    avant = False
    moi = False
    now = timezone.now
    all = Event.objects.order_by('start_datetime')
    if request.method == "POST":
        form = AfficheEvent(request.POST)
        if form.is_valid():
            avant = form.cleaned_data.get('avant')
            actif = form.cleaned_data.get('actif')
            moi = form.cleaned_data.get('moi')
            if not actif:
                all=all.filter(active=True)
            if not moi:
                all=all.filter(organizer=asso)
            return render(request, 'afficherevent.html', locals())
    else:
        form = AfficheEvent()
    return render(request, 'afficherevent.html',locals())

@login_required
def modifevent(request, event_id=1):
    if Association.objects.filter(admin_id=request.user.id).exists():
        asso = Association.objects.get(admin_id = request.user.id)
    else:
        asso = None
    if asso != None:
        event = Event.objects.get(id = event_id)
        if event.organizer != asso :
            return redirect(afficherevent)
        if request.method == "POST":
            form = CreerEvent(request.POST)
            if form.is_valid():
                event.name = form.cleaned_data.get('name')
                event.start_datetime = form.cleaned_data.get('start_datetime')
                event.active = form.cleaned_data.get('active')
                event.description = form.cleaned_data.get('description')
                event.save()
                return redirect(index)
        else:
            form = CreerEvent()
            form.fields.get('name').initial = event.name
            form.fields.get('start_datetime').initial = event.start_datetime
            form.fields.get('active').initial = event.active
            form.fields.get('description').initial = event.description
        return render(request, 'modifevent.html',locals())
    else:
        return render(request, 'modifevent.html',locals())


def index(request):
    return render(request, 'index.html',locals())