from django.db import models
from django.conf import settings
from django.utils import timezone

class Poll(models.Model):
    """
    Modello principale per i sondaggi.
    RELAZIONE: User -> Poll (ForeignKey to created_by)
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_polls'
    )

    class Meta:
        db_table = 'polls'

    def __str__(self):
        return self.title


    @property
    def total_votes(self):
        """
        Conteggia tutti i voti associati a questo sondaggio via Vote.related_name='votes'.
        """
        return self.votes.count()

class Choice(models.Model):
    """
    Opzioni di scelta per ogni sondaggio.
    RELAZIONE: Poll -> Choice (ForeignKey)
    """
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='choices'
    )
    text = models.CharField(max_length=200)


    class Meta:
        ordering = ['id']
        db_table = 'choices'

    def __str__(self):
        return f"{self.poll.title} - {self.text}"

    @property
    def votes_count(self):
        """
        Numero di voti per questa scelta.
        È un attributo read-only, non va mai assegnato direttamente.
        """
        return self.votes.count()

class Vote(models.Model):
    """
    Voti degli utenti per le scelte dei sondaggi.
    RELAZIONI:
      - User -> Vote (ForeignKey)
      - Poll -> Vote (ForeignKey)
      - Choice -> Vote (ForeignKey)
    Unica restrizione: l'utente può votare un solo voto per sondaggio.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='votes'
    )  # Aggiunta relazione a Poll per vincolo unique_together e query facili
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    voted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'poll')  # Garantisce un solo voto per utente/sondaggio
        ordering = ['-voted_at']
        db_table = 'votes'

    def __str__(self):
        return f"{self.user.username} voted for {self.choice.text}"  # Descrizione readability
