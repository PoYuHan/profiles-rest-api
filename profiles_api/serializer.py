from rest_framework import serializers


#Serializers in Django REST Framework are responsible for converting objects into data types understandable by javascript and front-end frameworks and vice versa.
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length = 10)