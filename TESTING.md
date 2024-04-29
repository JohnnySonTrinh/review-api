## Bugs

| Bug | Screenshot | Fixed | Notes |
| --- | ---------- | ----- | ----- |
| 400 responses even though the review was posted | ![Screenshot](documentation/bug/bug-1.png) | ✅ | Add `return Response(serializer.data, status=status.HTTP_201_CREATED)` |
| Conflict with Django's built-in messages framework | ![Screenshot](documentation/bug/bug-2.png) | ✅ | Renaming app to "notes" instead of "messages" to avoid the conflict with Django's built-in messaging framework. |