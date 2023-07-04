from rest_framework import serializers
from .models import JGdates

class JGdatesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JGdates
        fields = "__all__"