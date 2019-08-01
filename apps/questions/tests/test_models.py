from django.test import TestCase
from ..models import Question
from apps.authentication.models import User


class TestQuestionModels(TestCase):
    def setUp(self):
        self.model  = Question()

    def test_get_absolute_url(self):
        User.objects.create_user(email='user@mail.com', password='#pho3nix9q')
        user_qs = User.objects.get(email='user@mail.com')
        Question.objects.create(title='here is a title', question='some description', author=user_qs)
        qs = Question.objects.get(id=1)

        self.assertEqual(qs.get_absolute_url(), f"/questions/{qs.question_slug}/view/")
        self.assertEqual(qs.__str__(), qs.title)

    

