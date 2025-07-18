from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Poll, Choice, Vote
from .serializers import (
    PollListSerializer,
    PollDetailSerializer,
    PollCreateSerializer,
    VoteSerializer
)
from .permissions import IsOwnerOrReadOnly


class PollListCreateView(generics.ListCreateAPIView):
    """
    GET: lista tutti i sondaggi attivi.
    POST: crea un nuovo sondaggio (solo utenti autenticati).
    """
    queryset = Poll.objects.all()
    serializer_class = PollListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PollCreateSerializer
        return PollListSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    #def perform_create(self, serializer):
    #    poll = serializer.save(created_by=self.request.user)
    #    self.request.user.polls_created = self.request.user.polls_created + 1
    #    self.request.user.save(update_fields=['polls_created'])

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        # valida input
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # salva il sondaggio con created_by
        self.perform_create(serializer)
        # prepara la response con dettaglio completo
        detail_serializer = PollDetailSerializer(
            serializer.instance,
            context={'request': request}
        )
        headers = self.get_success_headers(detail_serializer.data)
        return Response(detail_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: dettaglio sondaggio.
    PUT/PATCH/DELETE: solo il creatore può modificarlo o cancellarlo.
    """
    queryset = Poll.objects.all()
    serializer_class = PollDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def vote_poll(request, poll_id):
    """
    Permette a un utente autenticato di votare un sondaggio una sola volta.
    """
    poll = get_object_or_404(Poll, id=poll_id)

    serializer = VoteSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()

    # Controllo voto singolo
    #if Vote.objects.filter(user=request.user, poll=poll).exists():
    #    return Response({'error': 'Hai già votato questo sondaggio.'}, status=status.HTTP_400_BAD_REQUEST)

    # Validazione scelta
    #choice_id = request.data.get('choice')
    #choice = get_object_or_404(Choice, id=choice_id, poll=poll)

    # Creazione voto
    #Vote.objects.create(
    #    user=request.user,
    #    poll=poll,
    #    choice=choice,
    #    ip_address=request.META.get('REMOTE_ADDR')
    #)

    return Response({'message': 'Voto registrato con successo.'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def poll_results(request, poll_id):
    """
    Recupera i risultati di un sondaggio con conteggi e percentuali.
    """
    poll = get_object_or_404(Poll, id=poll_id)
    total = poll.votes.count()
    results = []
    for choice in poll.choices.all():
        votes_count = choice.votes.count()
        percentage = round((votes_count / total) * 100, 1) if total > 0 else 0
        results.append({'choice': choice.text, 'votes': votes_count, 'percentage': percentage})

    return Response({'poll': poll.title, 'total_votes': total, 'results': results}, status=status.HTTP_200_OK)
