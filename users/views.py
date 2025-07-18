# users/views.py

from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .serializers import UserSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """
    API endpoint per la registrazione di un nuovo utente.

    - Chiunque (anonimo) può registrarsi (AllowAny).
    - Il nuovo utente viene creato senza privilegi di amministratore.
    - Viene aggiunto al gruppo "standard_user" per gestire i permessi.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Crea l'utente senza privilegi di staff o superuser
        user = serializer.save()
        user.is_staff = False
        user.is_superuser = False
        user.save()

        # Aggiunge l'utente al gruppo standard
        group, _ = Group.objects.get_or_create(name='standard_user')
        user.groups.add(group)

        return user


class UserDetailView(generics.RetrieveAPIView):
    """
    API endpoint per ottenere i dati dell'utente autenticato.
    Utile al client per abilitare o meno il pulsante "Area Admin".
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Restituisce l'istanza dell'utente loggato
        return self.request.user


class CurrentUserView(generics.RetrieveAPIView):
    """
    Restituisce i dati di request.user solo se autenticato.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
