from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model providing:
    A read-only 'owner' field sourced from the username.
    A list field for 'pokemon'.
    A custom string representation for the 'created' field.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    pokemon = serializers.ListField(required=False, allow_empty=True)
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        return obj.created.strftime("%dth %B %Y")

    class Meta:
        model = Profile
        fields = ["id", "owner", "created", "avatar", "about", "favorite", "pokemon"]