from rest_framework import serializers

from patients.models import Patient


class ListCreatePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.get('email')
        existing_patient = Patient.objects.filter(email=email).first()

        if existing_patient:
            return existing_patient

        patient = Patient.objects.create(**validated_data)
        return patient
