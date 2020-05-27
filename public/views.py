from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import get_user_model
from django.contrib import messages
from api.models import Event, Association
from django.http import HttpResponse
from django.shortcuts import redirect



def home(request):
    return render(request, 'public/home.html', {'title': 'Home'})


def calendar(request):
    # il faut lui donner le liste des events
    return render(request, 'public/calendar.html', {'title': 'Calendar'})


"""
class ResetPasswordView(PasswordResetView):
    user = get_object_or_404(Association, email=form.email)
    def form_valid(self, form):
        messages.error(PasswordResetView, f'This email is not registered as an User!')
        return redirect('ResetPasswordView')
"""


# this is actually replacing home view
class EventListView(ListView):
    model = Event
    template_name = 'public/home.html'
    context_object_name = 'events'
    ordering = ['-start_datetime']
    paginate_by = 5


class AssoEventListView(ListView):
    model = Event
    template_name = 'asso/page_asso.html'
    context_object_name = 'events'
    paginate_by = 5

    def get_queryset(self):
        asso = get_object_or_404(Association, name=self.kwargs.get('name'))
        return Event.objects.filter(organizer=asso).order_by('-start_datetime')


class AssoListView(ListView):
    model = Association
    template_name = 'public/assos.html'
    context_object_name = 'associations'
    paginate_by = 7


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    context_object_name = 'event'
    fields = ['name', 'description', 'start_datetime', 'end_datetime', 'location']

    def form_valid(self, form):
        form.instance.organizer = self.request.user.association
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    context_object_name = 'event'
    fields = ['name', 'description', 'start_datetime', 'end_datetime', 'active', 'location']

    def form_valid(self, form):
        form.instance.organizer = self.request.user.association
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer.user


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    context_object_name = 'event'
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer.user


def about(request):
    return render(request, 'public/about.html', {'title': 'About'})
