from rest_framework import serializers
from LoR.models import Deck, Card, Rank, RelDeck


class CardCountSerializers(serializers.ModelSerializer):
    card_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RelDeck
        fields = ["card_count", "card_id"]


class CardDeckSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["Name", "ImgPath"]


class DeckSerializers(serializers.ModelSerializer):
    card_count = serializers.SerializerMethodField("get_card_set")
    cards = CardDeckSerializers(many=True, read_only=True)
    effect = serializers.StringRelatedField(many=True, read_only=True)
    Recc_Floor = serializers.StringRelatedField(read_only=True)
    Recc_Page = serializers.StringRelatedField(read_only=True)
    Recc_Rank = serializers.StringRelatedField(read_only=True)
    creator = serializers.StringRelatedField(read_only=True)
    cardImage = serializers.SerializerMethodField

    class Meta:
        model = Deck
        fields = "__all__"

    def get_card_set(self, instance):
        reldecks = instance.reldeck_set.all().order_by("card_id")
        return CardCountSerializers(reldecks, many=True).data


class CardSerializers(serializers.ModelSerializer):
    Office = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Card
        fields = "__all__"


class RankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = "__all__"
