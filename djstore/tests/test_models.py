from django.test import TestCase
from djstore import models


class MainModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category_name = 'Test category'
        models.Categorie.objects.create(category_name=cls.category_name)

        cls.product_obj = models.Product.objects.create(name='Test prod',
                                                        description='test descr',
                                                        price=1,
                                                        image='images/some.jpg',
                                                        quantity=1,
                                                        discount=1,
                                                        author='Alex')

        models.Review.objects.create(product=cls.product_obj, text='lol', rating=2)
        models.Review.objects.create(product=cls.product_obj, text='lol2', rating=4)

    def test_category_slug(self):
        category = models.Categorie.objects.get(category_name=self.category_name)
        slug = category.slug
        self.assertEqual(slug, 'test-category')

    @classmethod
    def tearDownClass(cls):
        models.Categorie.objects.get(category_name=cls.category_name).delete()