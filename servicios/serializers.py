from rest_framework import serializers
from .models import Area, Servicio

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
