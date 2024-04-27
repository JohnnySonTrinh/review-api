from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewSerializer

class ReviewList(APIView):
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(
        reviews, many=True, context={'request': request}
    )
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )