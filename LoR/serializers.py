from rest_framework import serializers
from LoR.models import Deck, Card


class DeckSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
