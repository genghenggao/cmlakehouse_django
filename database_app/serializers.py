from rest_framework import serializers
from .models import MetaData, ChunkData

class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = '__all__'

class ChunkDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChunkData
        fields = '__all__'
