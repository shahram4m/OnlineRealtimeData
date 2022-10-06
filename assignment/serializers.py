from rest_framework import serializers

class InformationSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=None)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=None)
    image = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=2048)
