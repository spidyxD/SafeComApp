from rest_framework import serializers
from .models import Person, Vehicle, RecordVisit, Blacklist


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['identification', 'name', 'first_lastname', 'second_lastname', 'role']


class VehicleSerializer(serializers.ModelSerializer):

    owner = PersonSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = ['plate', 'model', 'brand', 'color', 'owner']


class RecordVisitSerializer(serializers.ModelSerializer):

    #visit_identification = PersonSerializer(read_only=True)
    plate = VehicleSerializer(read_only=True)

    class Meta:
        model = RecordVisit
        fields = ['visit_id', 'incoming_date', 'outgoing_date', 'reason', 'plate'] # , 'visit_identification' ]


class BlacklistSerializer(serializers.ModelSerializer):
    visitor = PersonSerializer(read_only=True)
    #visitor = serializers.CharField(read_only=True, source='visitor.identification')
    #visitor = serializers.PrimaryKeyRelatedField()


    class Meta:
        model = Blacklist
        fields = ['visitor', 'reason']

    def create(self, validated_data):
        identification = self._kwargs['data']['visitor']
        reason = validated_data.pop('reason')
        person = Person.objects.get(identification=identification)
        blk_Obj = Blacklist.objects.create(visitor=person, reason=reason)
        return blk_Obj