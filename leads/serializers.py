from rest_framework import serializers
from leads.models import Lead

#Making a class for serializing data
class LeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
