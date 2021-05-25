from django.test import TestCase
from .models import Category,Image,Location

# Create your tests here.
class LocationTestClass(TestCase):
    pass
class LocationTestClass(TestCase):
    '''
    test for Location class
    '''
    # Set up method

    def setUp(self):
        self.location = Location(place='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_update(self):
        self.location.save_location()
        location = Location.objects.filter(place="Kisumu").first()
        update = Location.objects.filter(id=id).update(place="Mombasa")
        self.assertTrue(Location.place, update.place)


class CategoryTestClass(TestCase):
    '''
    test for category class
    '''
    # Set up method

    def setUp(self):
        self.cat = Category(category='Love')

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_update(self):
        self.cat.save_category()
        category = Category.objects.filter(category='Lover').first()
        update = Category.objects.filter(id=id).update(category='nature')
        self.assertTrue(Category.category, update.category)


class ImageTestClass(TestCase):
    '''
    test for Image class
    '''

    def setUp(self):
        self.location = Location(place='Nairobi')
        self.location.save()
        self.cat = Category(category='Love')
        self.cat.save()
        self.new_image = Image(image='', name='lover', description='Love is the most previous gift i a human life.',
                               location=self.location, category=self.cat)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        self.new_image.save()
        new_image = Image.objects.all()
        self.assertTrue(len(new_image) > 0)
    # testing update method

    def test_search_image(self):
        images = Image.search_by_category('image')
        self.assertFalse(len(images) > 0)

    def test_get_all_images(self):
        images = Image.objects.all()
        self.Image(Image.name)
    # testing delete method

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()
    # testing get images by id Method

    def test_get_image_by_id(self):
        self.new_image.save_image()
        image = Image.get_image_by_id(1)
        self.assertEqual(image.id, 1)
