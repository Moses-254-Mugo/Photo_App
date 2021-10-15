from django.test import TestCase
from .models import Profile, Images

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.moses = Profile(name = "moses")

    # Testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.moses,Profile))


