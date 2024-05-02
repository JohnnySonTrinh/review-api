from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('reviews.urls')),
    path('', include('comments.urls')),
    path('', include('notes.urls')),
    path('', include('likes.urls')),
]
