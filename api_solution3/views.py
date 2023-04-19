from rest_framework.views import APIView
from api_solution3.models import Entity, Property
from api_solution3.serializers import EntitySerializer, PropertySerializer
from rest_framework.response import Response

# Create your views here.


class EntityView(APIView):
    """
    List of entities
    """

    def get(self, request, *args, **kwargs):
        entity_list = Entity.objects.all()
        serializer = EntitySerializer(entity_list, many=True)
        return Response(serializer.data)
