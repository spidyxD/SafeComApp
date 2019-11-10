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

    def create(self, validated_data):
        identification = self._kwargs['data']['owner']
        plate = validated_data.pop('plate')
        model = validated_data.pop('model')
        color = validated_data.pop('color')
        brand = validated_data.pop('brand')
        person = Person.objects.get(identification=identification)
        vehicle_created = Vehicle.objects.create(owner=person, plate=plate, model=model, brand=brand, color=color)

        return vehicle_created
"""
   def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
"""


class RecordVisitSerializer(serializers.ModelSerializer):

    #visit_identification = PersonSerializer(read_only=True)
    plate = VehicleSerializer(read_only=True)

    class Meta:
        model = RecordVisit
        fields = ['visit_id', 'incoming_date', 'outgoing_date', 'reason', 'plate'] # , 'visit_identification' ]

    def create(self, validated_data):

        plate = self._kwargs['data']['plate']
        #incoming_date = self._kwargs['data']['incoming_date']
        reason = validated_data.pop('reason')

        vehicle = Vehicle.objects.get(plate=plate)
        record_visit_created = RecordVisit.objects.create(plate=vehicle, reason=reason)

        return record_visit_created


class BlacklistSerializer(serializers.ModelSerializer):
    visitor = PersonSerializer(read_only=True)

    class Meta:
        model = Blacklist
        fields = ['blacklist_id', 'visitor', 'reason']

    def create(self, validated_data):
        identification = self._kwargs['data']['visit_identification']
        reason = validated_data.pop('reason')
        person = Person.objects.get(identification=identification)
        blk_Obj = Blacklist.objects.create(visitor=person, reason=reason)
        return blk_Obj