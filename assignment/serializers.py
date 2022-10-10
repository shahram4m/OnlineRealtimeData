from rest_framework import serializers

# class Serializer for InformationSerializer
class InformationSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=None)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=None)
    image = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=2048)

# class Serializer for CreatFileInformation
class CreatFileInformationSerializer(serializers.Serializer):
    url = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)

# class Serializer for FileInformation
class FileInformationSerializer(serializers.Serializer):
    url = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    created_at = serializers.DateField(required=False, allow_null=True)
