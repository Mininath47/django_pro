# app1/serializers.py
from rest_framework import serializers
from app1.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # include all fields from the model
