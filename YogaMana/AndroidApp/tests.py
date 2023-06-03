from rest_framework import status
from django.test import TestCase, Client
from .models import Member, Category, Address
from .serializers import MemberSerializers, CategorySerializers
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.datetime_safe import datetime
client = Client()


class CategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cat1 = Category.objects.create(category_title='cat1')
        self.cat2 = Category.objects.create(category_title='cat2')

    def test_my_api_endpoint(self):
        url = reverse('category_list_info', )
        data = {'category_title': 'test'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category_list(self):
        url = reverse('category_list_info')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_new_category(self):
        url = reverse('category_list_info')
        data = {'category_title': 'New', }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)
        self.assertEqual(Category.objects.get(pk=3).category_title, 'New')

    def test_update_existing_category(self):
        url = reverse('category_detail_info', kwargs={'pk': self.cat1.pk})
        data = {'category_title': 'Updated', }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(pk=self.cat1.pk).category_title, 'Updated')

    def test_delete_existing_category(self):
        url = reverse('category_detail_info', kwargs={'pk': self.cat2.pk})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 1)


class AddressAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        mem1 = Member.objects.create(first_name='m1',last_name='l1',username='u1',password='11',
                                     email='manf@lrkj.com',created_date=datetime.now())
        self.adr1 = Address.objects.create(country='co1', city='ci1', address='add1', address_phone='09554446666', member_id=mem1)
        self.adr2 = Address.objects.create(country='co2', city='ci2', address='add2', address_phone='09553336666',member_id=mem1 )

    def test_create_new_address(self):
        url = reverse('address_list_info')
        data = {'country':'new1', 'city':'new1', 'address':'new1', 'address_phone':'09554446666', }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 3)
        self.assertEqual(Address.objects.get(pk=3).country, 'new1')

    def test_update_existing_address(self):
        url = reverse('address_detail_info', kwargs={'pk': self.adr1.pk})
        data = {'country': 'Updated', }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Address.objects.get(pk=self.adr1.pk).country, 'Updated')

    def test_delete_existing_address(self):
        url = reverse('address_detail_info', kwargs={'pk': self.adr2.pk})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Address.objects.count(), 1)
