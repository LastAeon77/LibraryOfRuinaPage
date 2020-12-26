from rest_framework import serializers
from LoR.models import Deck, Card, Rank


class CardDeckSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["Name", "ImgPath"]


class DeckSerializers(serializers.ModelSerializer):
    cards = CardDeckSerializers(many=True, read_only=True)
    effect = serializers.StringRelatedField(many=True, read_only=True)
    Recc_Floor = serializers.StringRelatedField(read_only=True)
    Recc_Page = serializers.StringRelatedField(read_only=True)
    Recc_Rank = serializers.StringRelatedField(read_only=True)
    creator = serializers.StringRelatedField(read_only=True)
    cardImage = serializers.SerializerMethodField

    class Meta:
        model = Deck
        fields = ("__all__")


class CardSerializers(serializers.ModelSerializer):
    Office = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Card
        fields = "__all__"


class RankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = "__all__"
