from rest_framework import serializers
from LoR.models import Deck, Card, Rank


class DeckSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class RankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'
