from django.db import models
from django.contrib.auth.models import User

from base_game.constants import RESULT_CHOICES


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExhibitionGame(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    against_other_user = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='exhibition_games')
    results = models.CharField(max_length=10, choices=RESULT_CHOICES)
