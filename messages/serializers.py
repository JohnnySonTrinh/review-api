from rest_framework serializer
from .model import Message


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Message
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'review', 'created_on', 'updated_on', 'content'
        ]


class MessageDetailSerializer(MessageCerializer):
    """
    Serializer for the Message model used in Detail view
    Message is a read only field so that we dont have to set it on each update
    """
    review = serializers.ReadOnlyField(source='review.id')
