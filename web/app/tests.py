from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Category, City, Advert
from .serializers import AdvertSerializer


class AdvertAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='TestCategory')
        self.city = City.objects.create(name='TestCity')
        self.advert = Advert.objects.create(
            title='TestAdvert',
            description='Test description',
            city=self.city,
            views=0
        )
        self.advert.category.add(self.category)

    def test_get_advert_list(self):
        url = reverse('advert-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        adverts = Advert.objects.all()
        serializer = AdvertSerializer(adverts, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_advert_detail(self):
        url = reverse('advert-detail', args=[self.advert.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        advert = Advert.objects.get(pk=self.advert.pk)
        serializer = AdvertSerializer(advert)
        self.assertEqual(response.data, serializer.data)

    def test_increment_views(self):
        initial_views = self.advert.views
        url = reverse('advert-detail', args=[self.advert.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.advert.refresh_from_db()
        self.assertEqual(self.advert.views, initial_views + 1)
