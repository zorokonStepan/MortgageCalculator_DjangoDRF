from rest_framework import serializers

from .models import MortgageOffers


class MortgageOffersSerializer(serializers.ModelSerializer):
    """Serialization of data during CRUD operations with data from a database MortgageOffers"""
    class Meta:
        model = MortgageOffers
        fields = ('id', 'bank_name', 'term_min', 'term_max', 'rate_min', 'rate_max', 'payment_min', 'payment_max')


class MortgageOffersReceiveProcessSerializer(serializers.Serializer):
    """Serialization of data during GET operations with parameters with data from the database MortgageOffers"""
    id = serializers.IntegerField()
    payment = serializers.IntegerField()
    bank_name = serializers.CharField(max_length=255)
    term_min = serializers.IntegerField()
    term_max = serializers.IntegerField()
    rate_min = serializers.FloatField()
    rate_max = serializers.FloatField()
    payment_min = serializers.IntegerField()
    payment_max = serializers.IntegerField()
