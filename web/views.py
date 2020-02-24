from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Assocation, Event
from .serializers import AssoSerializer, EventSerializer


# Create your views here.

class AssoViewset(viewsets.ModelViewSet):
    """
    Donne toutes les associations
    """
    queryset = Assocation.objects.all().order_by('name')
    serializer_class = AssoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)

    @action(methods=('get',), detail=False)
    def mine(self, request: Request):
        instance = self.request.user.association
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class EventViewset(viewsets.ModelViewSet):
    """
    Renvoie les évènements à venir et en cours (début avant maintenant et actif=oui)
    """
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'association__name')
    filterset_fields = ('organizer',)

    def get_queryset(self):
        return self.queryset.filter(active=True, datetime__lte=now())
