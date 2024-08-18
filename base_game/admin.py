from django.contrib import admin
from base_game.models import ExhibitionGame


@admin.register(ExhibitionGame)
class ExhibitionGameAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "results", "created_at")
