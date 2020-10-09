import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Ability, Pokemon, PokemonProfile

class AbilityType(DjangoObjectType):
    """
    GraphQL type for the Ability model
    """

    class Meta:
        model = Ability

class PokemonType(DjangoObjectType):
    """
    GraphQL type for the Pokemon model
    """

    class Meta:
        model = Pokemon

class PokemonProfileType(DjangoObjectType):
    """
    GraphQL type for the PokemonProfile model
    """

    class Meta:
        model = PokemonProfile

class Query(ObjectType):
    """
    GraphQL Query type
    """

    ability = graphene.Field(AbilityType, id=graphene.String())
    pokemon = graphene.Field(PokemonType, id=graphene.String())
    pokemon_profile = graphene.Field(PokemonProfileType, id=graphene.String())

    abilities = graphene.List(AbilityType)
    pokemons = graphene.List(PokemonType)
    pokemon_profiles = graphene.List(PokemonProfileType)

    def resolve_ability(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Ability.objects.get(pk=id)

        return None

    def resolve_pokemon(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Pokemon.objects.get(pk=id)
        
        return None

    def resolve_pokemon_profile(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return PokemonProfile.objects.get(pk=id)
        
        return None

    def resolve_abilities(self, info, **kwargs):
            return Ability.objects.all()

    def resolve_pokemons(self, info, **kwargs):
            return Pokemon.objects.all()
    
    def resolve_pokemon_profiles(self, info, **kwargs):
            return PokemonProfile.objects.all()


schema = graphene.Schema(query=Query)
