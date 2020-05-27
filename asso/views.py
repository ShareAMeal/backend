from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdminCreationForm, UserUpdateForm, AssoUpdateForm
from django.contrib.auth import get_user_model

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = AdminCreationForm()
    return render(request, 'asso/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        a_form = AssoUpdateForm(request.POST, request.FILES, instance=request.user.association)
        if u_form.is_valid() and a_form.is_valid():
            u_form.save()
            a_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        a_form = AssoUpdateForm(instance=request.user.association)
    context = {
        'u_form': u_form,
        'a_form': a_form,
        'user': request.user,
    }
    return render(request, 'asso/profile.html', context)


# edit for every association
def page_asso(request):
    return render(request, 'asso/page_asso.html')

