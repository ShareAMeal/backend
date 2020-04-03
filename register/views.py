# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegisterForm,ConnexionForm,CreerAsso
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from.models import Association



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
            return redirect('ok')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

def ok(request):
    return render(request, 'ok.html')


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
                return redirect('connexion')
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', locals())

#Vu qui te deconnecte
def deconnexion(request):
    logout(request)
    return redirect(connexion)

@login_required
def creerasso(request):
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
            redirect('ok')
    else:
        form = CreerAsso()
    return render(request, 'creerasso.html',locals())
