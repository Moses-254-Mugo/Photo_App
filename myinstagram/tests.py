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

class ImagesTestClass(TestCase):
    def setUp(self):
        # Creating an new Image and saving it
        self.moses = Profile(name = "moses")

        # Creating a new image and saving it
        self.new_image  = Images(name = 'game')
        self.new_image.save()

    def test_save_image(self):
        self.image_test.save_image()
        image = Images.objects.all()
        self.assertTrue(len(image) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
        Images.objects.all().delete()