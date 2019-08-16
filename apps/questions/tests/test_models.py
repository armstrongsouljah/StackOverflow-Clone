from django.test import TestCase
from ..models import Question, Tag
from apps.authentication.models import User
from django.db.utils import IntegrityError


class TestQuestionModels(TestCase):
    def setUp(self):
        self.model  = Question()
        self.tagModel = Tag()

    def test_get_absolute_url(self):
        User.objects.create_user(email='user@mail.com', password='#pho3nix9q')
        user_qs = User.objects.get(email='user@mail.com')
        Question.objects.create(title='here is a title', question='some description', author=user_qs)
        qs = Question.objects.get(id=1)

        self.assertEqual(qs.get_absolute_url(), f"/questions/{qs.question_slug}/view/")
        self.assertEqual(qs.__str__(), qs.title)

    def test_creating_an_existing_tag_fails(self):
        with self.assertRaises(IntegrityError) : 
            Tag.objects.create(name="angular")
            Tag.objects.create(name="angular")

    def test_creating_tag_without_name_fails(self):
        with self.assertRaises(IntegrityError):
            Tag.objects.create(name=None)



    

