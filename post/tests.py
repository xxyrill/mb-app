from django.test import TestCase # IMPORT STMNT
from django.urls import reverse

# nag import kas ug TestCase which is a class from django framework to
# test djano applications

from .models import Post # IMPORT STMNT

# gi import nmu ang models.py from Post. Ang '.' pasabot ani kay si test module
# or si (test.py) kay located in the same package with models.py.
# Nganong si models.py ang gi import? Because dhaa located ang imohang database.
# which is mao ang purpose sa imohang test.

class PostModelsTest(TestCase): # THIS IS A TEST CASE CLASS DEFINITION

    # PostModelTest that inherits from django.test.TestCase.
    # This class will contain the individual tests for the Post model.

    def setUp(self): # SETUP METHOD
        Post.objects.create(text='just a test') # TEST METHOD

    # def setUp(self):: This method is executed before each test method in
    # the test case. It is used to set up any necessary data or conditions for the tests.

    # Post.objects.create(text='just a test'): Creates an instance of the Post model
    # with the specified text ('just a test') and saves it to the database.

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')

    # def test_text_content(self):: Defines a test method named test_text_content.
    # Test methods in Django test cases must start with the word "test" to be recognized as test methods.

    # post = Post.objects.get(id=1): Retrieves the Post instance with the ID of 1 from the database.
    # This assumes that the setUp method has already created an instance with ID 1.

    # 'expected_object_name = f'{post.text}': Builds a string containing the text of the retrieved
    # Post instance. This is done using an f-string to format the string.

    # self.assertEqual(expected_object_name, 'just a test'): Asserts that the expected_object_
    # name is equal to the string 'just a test'. If they are not equal, the test will fail.

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another text')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

# if you run the test in cmd, you will see Ran 4 test kay 4 ra ka test instance ang
# gi test (all the test_ are the ones being counted)