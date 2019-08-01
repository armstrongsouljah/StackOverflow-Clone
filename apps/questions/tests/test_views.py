from django.test import TestCase
from apps.authentication.models import User
from ..models import Question
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        User.objects.create_user(email='main@mail.com', password='pheonix9q')
        User.objects.create_user(email='main2@mail.com', password='#pho3nix9q')
        self.user1 = User.objects.get(email='main@mail.com')
        self.user2 = User.objects.get(email='main2@mail.com')

        self.question_one = Question.objects.create(title='some title', question='blah', author=self.user1)
        self.question_two = Question.objects.create(title='some title', question='new data', author=self.user1)

    def test_redirects_to_login_if_not_logged_in_when_creating_aquestion(self):
        response = self.client.get(reverse(f'questions:add'))
        self.assertRedirects(response, f'/accounts/login/?next=/questions/new/')

    def test_single_question_renders(self):
        response = self.client.get(reverse(f'questions:detail', kwargs={'question_slug': self.question_one.question_slug}))
        self.assertEqual(200, response.status_code)

    def test_listing_question_view_renders(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)

