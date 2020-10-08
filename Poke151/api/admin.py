from django.contrib import admin
from api.models import Ability, Pokemon, PokemonProfile

class AbilityInline(admin.StackedInline):
    """
    Allows Ability model to be viewed on other pages
    """

    model = PokemonProfile.ability.through

class AbilityAdmin(admin.ModelAdmin):
    """
    Ability model site view settings
    """
    pass

class PokemonAdmin(admin.ModelAdmin):
    """
    Pokemon model site view settings
    """
    pass

class PokemonProfileAdmin(admin.ModelAdmin):
    """
    PokemonProfile model site view settings
    """
    inlines = [AbilityInline,]
    exclude = ['ability']

admin.site.register(Ability)
admin.site.register(Pokemon)
admin.site.register(PokemonProfile, PokemonProfileAdmin)
