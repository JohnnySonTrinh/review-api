from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Note
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'review', 'created_on', 'updated_on', 'content'
        ]


class NoteDetailSerializer(NoteSerializer):
    """
    Serializer for the Note model used in Detail view
    Note is a read only field so that we dont have to set it on each update
    """
    review = serializers.ReadOnlyField(source='review.id')
