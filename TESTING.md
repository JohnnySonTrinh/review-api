![alt text](image.png)
got 400 response even review was posted
fix: return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )