from rest_framework import serializers
from .models import Person, Vehicle, RecordVisit, Blacklist


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ['plate', 'model', 'brand', 'color']


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['identification', 'name', 'first_lastname', 'second_lastname', 'role']


class RecordVisitSerializer(serializers.ModelSerializer):

    visit_identification = PersonSerializer(read_only=True)

    class Meta:
        model = RecordVisit
        fields = ['visit_id', 'incoming_date', 'outgoing_date', 'visit_identification', 'reason', 'plate']


class BlacklistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blacklist
        fields = ['visit_identification', 'plate', 'reason']