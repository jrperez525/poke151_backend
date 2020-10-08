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

    ability = graphene.Field(AbilityType, pk=graphene.String())
    pokemon = graphene.Field(PokemonType, pk=graphene.String())
    pokemon_profile = graphene.Field(PokemonProfileType, pk=graphene.String())
    abilities = graphene.List(AbilityType)
    pokemons = graphene.List(PokemonType)
    pokemon_profiles = graphene.List(PokemonProfileType)

    def resolve_ability(self, info, **kwargs):
        pk = kwargs.get('pk')

        if pk is not None:
            return Ability.objects.get(pk=pk)

        return None

schema = graphene.Schema(query=Query)
