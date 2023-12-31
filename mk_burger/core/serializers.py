from rest_framework import serializers

from mk_burger.core.models import Bread, Burger, Meat, Optional, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            "id",
            "tipo",
        )


class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = (
            "id",
            "tipo",
        )


class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meat
        fields = (
            "id",
            "tipo",
        )


class OptionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Optional
        fields = (
            "id",
            "tipo",
        )


class IngredientSerializer(serializers.Serializer):
    paes = BreadSerializer(many=True)
    carnes = BreadSerializer(many=True)
    opcionais = OptionalSerializer(many=True)


class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = (
            "id",
            "nome",
            "carne",
            "pao",
            "status",
            "opcionais",
        )

    def to_representation(self, instance):
        return {
            "id": instance.pk,
            "nome": instance.nome,
            "pao": instance.pao.tipo,
            "carne": instance.carne.tipo,
            "status": instance.status.tipo,
            "opcionais": instance.opcionais.all().values_list("tipo", flat=True),
        }
