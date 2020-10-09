import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from graphene.test import Client

from ..models import Ability
from ..schema import schema

ability_list_query = """
    query {
        abilities {
            name
            description
            isHiddenAbility
        }
    }
"""

ability_query = """
    query($id: String!) {
        ability(id: $id) {
            name
            description
            isHiddenAbility
        }
    }
"""

@pytest.mark.django_db
class TestAbilityModel(TestCase):
    """
    GraphQL test suite for Ability model
    """

    def setUp(self):
        self.client = Client(schema)
        self.ability = mixer.blend(Ability)

    def test_ability_query(self):
        response = self.client.execute(ability_query, variables={"id": self.ability.name})
        response_ability = response.get("data").get("ability")
        
        self.assertEqual(response_ability["name"], self.ability.name)

    def test_ability_list_query(self):
        mixer.blend(Ability)
        mixer.blend(Ability)
        ABILITIES_LIST_LENGTH = 3

        response = self.client.execute(ability_list_query)
        abilities = response.get("data").get("abilities")

        self.assertEqual(len(abilities), ABILITIES_LIST_LENGTH)