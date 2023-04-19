from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, inline_serializer

from api_solution1.serializers import EntitySerializer
from api_solution1.models import Entity


# Create your views here.


class EntityView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    """
    List of entities
    """

    def get(self, request, *args, **kwargs):
        entity_list = Entity.objects.all()
        serializer = EntitySerializer(entity_list, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=inline_serializer(
            name="Solution1RequestInline",
            fields={
                "value": serializers.IntegerField(),
            },
        ),
    )
    def post(self, request, *args, **kwargs):
        # Сеарилизуем получаемые данные
        serializer = EntitySerializer(data=request.data)
        # Проверяем валидность данных сериализатора
        if serializer.is_valid():
            # Проверяем передан ли нам BasicAuth
            if request.user.is_authenticated:
                # Создаем Entity с пользователем обратившимся к API ресурсу
                serializer.save(modified_by=self.request.user)
                return Response({"message": "Entity Created"}, status=status.HTTP_201_CREATED)
            return Response({"message": "Authentication Failed"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "Bad request to API"}, status=status.HTTP_400_BAD_REQUEST)
