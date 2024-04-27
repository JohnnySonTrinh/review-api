![alt text](documentation/bug/bug-1.png)
got 400 responses even though the review was posted
fix: return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )