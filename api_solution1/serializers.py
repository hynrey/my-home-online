from rest_framework import serializers

from api_solution1.models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    key = serializers.CharField()
    value = serializers.CharField()

    class Meta:
        model = Property
        fields = "__all__"


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()
    properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = Entity
        fields = "__all__"
