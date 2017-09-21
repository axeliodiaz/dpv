from rest_framework import serializers
from core.models import TipoDivisa


class TipoDivisaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoDivisa
        fields = '__all__'
