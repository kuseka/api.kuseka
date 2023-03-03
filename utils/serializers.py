from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
    location_choices = [
        ('profile', 'Profile Images'),
        ('assets', 'Website assets')
    ]
    location = serializers.ChoiceField(choices=location_choices)