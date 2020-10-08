from django.db import models

class Ability(models.Model):
    """
    Ability Model
    """

    name = models.CharField(primary_key=True, max_length=25)
    description = models.CharField(max_length=550)
    is_hidden_ability = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'abilities'

    def __str__(self):
        return f'{self.name}'

class Pokemon(models.Model):
    """
    Pokemon Model

    Contains basic details about a Pokemon
    """

    name = models.CharField(primary_key=True, max_length=25)
    dex_number = models.CharField(max_length=3)
    type_one = models.CharField(max_length=10)
    type_two = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'pokemon'

    def __str__(self):
        return f'{self.name}'

class PokemonProfile(models.Model):
    """
    Pokemon Profile

    Contains advanced details about a Pokemoon
    """

    pokemon = models.OneToOneField(Pokemon, primary_key=True, on_delete=models.CASCADE)
    ability = models.ManyToManyField(Ability)

    pokedex_entry = models.CharField(max_length=450)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    classification = models.CharField(max_length=25)
    male_ratio = models.CharField(max_length=10)
    female_ratio = models.CharField(max_length=10)
    base_egg_steps = models.CharField(max_length=10)
    base_happiness = models.PositiveSmallIntegerField()
    capture_rate = models.PositiveSmallIntegerField()
    effort_values = models.CharField(max_length=35)

    weakness_normal = models.CharField(max_length=10)
    weakness_fire = models.CharField(max_length=10)
    weakness_water = models.CharField(max_length=10)
    weakness_electric = models.CharField(max_length=10)
    weakness_grass = models.CharField(max_length=10)
    weakness_ice = models.CharField(max_length=10)
    weakness_fight = models.CharField(max_length=10)
    weakness_poison = models.CharField(max_length=10)
    weakness_ground = models.CharField(max_length=10)
    weakness_flying = models.CharField(max_length=10)
    weakness_psychc = models.CharField(max_length=10)
    weakness_bug = models.CharField(max_length=10)
    weakness_rock = models.CharField(max_length=10)
    weakness_ghost = models.CharField(max_length=10)
    weakness_dragon = models.CharField(max_length=10)
    weakness_dark = models.CharField(max_length=10)
    weakness_steel = models.CharField(max_length=10)
    weakness_fairy = models.CharField(max_length=10)

    base_stat_hp = models.PositiveSmallIntegerField()
    base_stat_attack = models.PositiveSmallIntegerField()
    base_stat_defense = models.PositiveSmallIntegerField()
    base_stat_special_attack = models.PositiveSmallIntegerField()
    base_stat_special_defense = models.PositiveSmallIntegerField()
    base_stat_speed = models.PositiveSmallIntegerField()
    base_stat_total = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['pokemon']

    def __str__(self):
        return f'{self.pokemon.name} Profile'
