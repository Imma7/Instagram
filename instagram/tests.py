from django.test import TestCase
from .models import Profile, Image

# Create your tests here.

class ProfileTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.imma = Profile(bio = 'student', username = 'imma')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.imma,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.imma.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
