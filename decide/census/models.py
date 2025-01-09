from django.db import models


class Census(models.Model):
    nombre = models.CharField()
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (('voting_id', 'voter_id'),)
