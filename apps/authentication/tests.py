from django.test import TestCase
from .models import User

class TestModels(TestCase):
    def setUp(self):
        self.user_data = dict(
            email='soultech22@gmail.com',
            password='#pho3jffjjfjfjf'
        )

    def test_creating_a_user_with_valid_data_passes(self):
        User.objects.create_user(**self.user_data)
        user_qs = User.objects.count()
        self.assertEqual(1, user_qs)

    def test_creating_a_superuser_with_valid_data_passes(self):
        User.objects.create_superuser(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        self.assertTrue(user_qs.admin)
        self.assertTrue(user_qs.is_admin)

    def test_creating_a_staffuser_with_valid_data_passes(self):
        User.objects.create_staffuser(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        self.assertTrue(user_qs.staff)
        self.assertTrue(user_qs.is_staff)

    def test_string_representation_of_user_model(self):
        User.objects.create_user(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        self.assertEqual(self.user_data.get('email'), user_qs.email)

    def test_creating_a_user_without_email_fails(self):
        self.user_data['email'] = None
        with self.assertRaises(TypeError) : 
            User.objects.create_user(**self.user_data)

    def test_creating_a_user_without_password_fails(self):
        self.user_data['password'] = None
        with self.assertRaises(TypeError) : 
            User.objects.create_user(**self.user_data)

    def test_created_user_has_module_perms(self):
        User.objects.create_user(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        self.assertTrue(user_qs.has_module_perms('authentication.User'))

    def test_user_has_object_level_permissions(self):
        User.objects.create_user(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        self.assertTrue(user_qs.has_perm(User))

    def test_get_shortname_returns_shortname(self):
        User.objects.create_user(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        email_to_compare = self.user_data.get('email').split('@')[0]
        self.assertEqual(user_qs.get_shortname(), email_to_compare)

    def test_get_fulltname_returns_fullname(self):
        User.objects.create_user(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        email_to_compare = self.user_data.get('email')
        self.assertEqual(user_qs.get_fullname(), email_to_compare)

    def test_get_username_returns_username(self):
        User.objects.create_user(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        email_ = self.user_data.get('email')
        self.assertEqual(user_qs.get_username(), email_)

    def test_str__returns_string_representation(self):
        User.objects.create_user(**self.user_data)
        user_qs = User.objects.get(email=self.user_data.get('email'))
        email_ = self.user_data.get('email')
        self.assertEqual(user_qs.__str__(), email_)
