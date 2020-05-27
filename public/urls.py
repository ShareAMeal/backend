from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    AssoEventListView,
    AssoListView,
)
from . import views

urlpatterns = [
    path('', EventListView.as_view(), name='public-home'),
    path('associations/', AssoListView.as_view(), name='public-asso'),
    path('asso/<str:name>', AssoEventListView.as_view(), name='asso-events'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='event-delete'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('calendar/', views.calendar, name='public-calendar'),
    path('about/', views.about, name='public-about'),
]