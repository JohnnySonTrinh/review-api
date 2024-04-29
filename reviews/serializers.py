from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    # Serializer for the Review model
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                "Image size larger than 2MB"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width larger than 4096 pixels!"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height larger than 4096 pixels!"
            )
        return value

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return obj.owner == request.user

    class Meta:
        model = Review
        fields = [
            'id',
            'owner',
            'is_owner',
            'created_on',
            'updated_on',
            'title',
            'content',
            'github_repo',
            'live_website',
            'image',
            'profile_id',
            'profile_image',
        ]
