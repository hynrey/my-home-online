from rest_framework import serializers

from api_solution2.models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    key = serializers.CharField()
    value = serializers.CharField()

    class Meta:
        model = Property
        fields = "__all__"


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()
    properties = PropertySerializer(many=True, read_only=True)

    def is_valid(self, *, raise_exception=False):
        if self.initial_data.get("data[value]", None) is not None:
            data_value = self.initial_data.get("data[value]")
            if isinstance(data_value, int):
                return True
            else:
                return False
        return super().is_valid(raise_exception=raise_exception)

    def save(self, modified_by):
        data_value = self.initial_data.get(
            "data[value]")
        e = Entity(value=data_value, modified_by=modified_by)
        e.save()

    class Meta:
        model = Entity
        fields = "__all__"
