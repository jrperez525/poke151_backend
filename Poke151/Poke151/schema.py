import graphene
import api.schema

class Query(api.schema.Query, graphene.ObjectType):
    """
    Inherits Query class from schema
    """
    pass

schema = graphene.Schema(query=Query)