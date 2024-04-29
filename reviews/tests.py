"""
from .models import Review
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

class ReviewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='reviewer', password='password123')
        self.review = Review.objects.create(
            owner=self.user, 
            title='Sample Review', 
            content='This is a review.', 
            github_repo='http://github.com/example',
            live_website='http://example.com'
        )

    def test_create_review(self):
        self.client.login(username='reviewer', password='password123')
        response = self.client.post('/reviews/', {
            'title': 'New Review',
            'content': 'Detailed review content.',
            'github_repo': 'http://github.com/newexample',
            'live_website': 'http://newexample.com'
        }, format='json')
        print("Response Data:", response.data)  # Print response data
        print("Response Status Code:", response.status_code)  # Print status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)
        print("Number of Reviews After Creation:", Review.objects.count())  # Print count of reviews

    def test_review_listing(self):
        response = self.client.get('/reviews/')
        print("List Response Data:", response.data)  # Print list of reviews
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(review['title'] == 'Sample Review' for review in response.data))

    def test_unauthorized_creation(self):
        response = self.client.post('/reviews/', {'title': 'Attempt'}, format='json')
        print("Unauthorized Creation Attempt Status Code:", response.status_code)  # Print status code for unauthorized creation
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ReviewUpdateTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='reviewer', password='password123')
        self.client.login(username='reviewer', password='password123')
        self.review = Review.objects.create(
            owner=self.user,
            title='Original Title',
            content='Original content.',
            github_repo='http://github.com/original',
            live_website='http://original.com'
        )

    def test_update_review(self):
        updated_data = {
            'title': 'Updated Title',
            'content': 'Updated content.',
            'github_repo': 'http://github.com/updated',
            'live_website': 'http://updated.com'
        }
        url = f'/reviews/{self.review.id}/'
        response = self.client.patch(url, updated_data, format='json')
        print(f'Testing URL: {url}')
        print("Response Status Code:", response.status_code)

        if response.status_code == status.HTTP_200_OK:
            print("Response Data:", response.data)

        # Fetch the updated review from the database
        self.review.refresh_from_db()

        # Assertions to verify the review was updated correctly
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.review.title, 'Updated Title')
        self.assertEqual(self.review.content, 'Updated content.')
        self.assertEqual(self.review.github_repo, 'http://github.com/updated')
        self.assertEqual(self.review.live_website, 'http://updated.com')

# Correct URL patterns with trailing slashes:
from django.urls import path
from reviews import views

urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view())
]
"""