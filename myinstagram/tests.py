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

    # Testing the save method
    def test_save_method(self):
        self.moses.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0 )

