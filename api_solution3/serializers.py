from rest_framework import serializers

from api_solution3.models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    key = serializers.CharField()
    value = serializers.CharField()

    class Meta:
        model = Property
        fields = "__all__"


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()
    properties = serializers.SerializerMethodField(read_only=True)

    def get_properties(self, obj):
        properties = {}
        for property in obj.properties.all():
            properties.update({property.key: property.value})
        return properties

    class Meta:
        model = Entity
        fields = "__all__"
