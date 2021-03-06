from django.utils.timezone import now
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Association, Event
from .serializers import AssoSerializer, UserSerializer, EventReadSerializer, EventWriteSerializer


# Create your views here.

class AssoViewset(viewsets.ModelViewSet):
    """
    Donne toutes les associations
    """
    queryset = Association.objects.all().order_by('name')
    serializer_class = AssoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    def perform_create(self, serializer):
        return serializer.save(admin=self.request.user)

    @action(methods=('get',), detail=False, permission_classes=[IsAuthenticatedOrReadOnly])
    def mine(self, request: Request):
        """
        Montre directement l'association de l'utilisateur. Cet endpoint ne permet pas de modifier l'objet
        """
        instance = self.request.user.association
        if instance is not None:
            if request.method == 'GET':
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            else:
                request.parser_context['kwargs']['pk'] = instance.pk
                return self.update(request)
        else:
            # Translators: This error should not arise, usually
            raise APIException(detail=_("You have no association"), code=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=False, permission_classes=[IsAuthenticated])
    def mod(self, request):
        instance = self.request.user.association
        request.parser_context['kwargs']['pk'] = instance.pk
        if instance is not None:
            return self.update(request)
        else:
            raise APIException(detail=_("You have no association"), code=status.HTTP_404_NOT_FOUND)


class EventViewset(viewsets.ModelViewSet):
    """
    Renvoie tous les évènements
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'association__name')
    filterset_fields = ('organizer', 'ville')

    def get_queryset(self):
        queryset = Event.objects.all()
        if self.request.method == 'POST':
            if self.request.user.is_authenticated:
                queryset = queryset.filter(organizer__admin=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return EventReadSerializer
        else:
            return EventWriteSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            if self.request.user.association is not None:
                return serializer.save(organizer=self.request.user.association)
        return super().perform_create(serializer)

    @action(methods=['get'], detail=False)
    def open(self, request):
        """
        Renvoie les évènements à venir et en cours (début avant maintenant et actif=oui)
        """
        queryset = self.get_queryset().filter(active=True, start_datetime__lte=now())
        return Response(EventReadSerializer(queryset, many=True).data)


class TestAuthViewSet(viewsets.ViewSet):
    """
    Sert à vérifier le pseudo/mot de passe lors d'une connexion Http Basic pour Android
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response(UserSerializer(self.request.user).data)
