from rest_framework import serializers
from .models import Person, Vehicle, RecordVisit, Blacklist


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['identification', 'name', 'first_lastname', 'second_lastname', 'role']


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ['plate', 'model', 'brand', 'color']


class RecordVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecordVisit
        fields = ['incoming_date', 'outgoing', 'plate', 'visit_identification', 'reason']


class BlacklistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blacklist
        fields = ['visit_identification', 'plate', 'reason']