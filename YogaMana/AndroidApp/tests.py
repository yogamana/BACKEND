from rest_framework import status
from django.test import TestCase, Client
from .models import Member, Category, Address, Course, PhysicalInfo
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

    def test_my_api_address_endpoint(self):
        url = reverse('address_list_info', )
        data = {'country': 'test'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_address_list(self):
        url = reverse('address_list_info')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_new_address(self):
        url = reverse('address_list_info')
        data = {'country':'new1', 'city':'new1', 'address':'new1', 'address_phone':'09554446666', }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Address.objects.count(), 2)
        self.assertEqual(Address.objects.get(pk=2).country, 'co2')

    def test_update_existing_address(self):
        url = reverse('address_detail_info', kwargs={'pk': self.adr1.pk})
        data = {'country': 'Updated', }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Address.objects.get(pk=self.adr1.pk).country, 'co1')

    def test_delete_existing_address(self):
        url = reverse('address_detail_info', kwargs={'pk': self.adr2.pk})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Address.objects.count(), 1)


class PhysicalInfoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        mem1 = Member.objects.create(first_name='m1', last_name='l1', username='u1', password='11',
                                     email='manf@lrkj.com', created_date=datetime.now())
        self.pi1 = PhysicalInfo.objects.create(height=15.5, weight=65.6,birth_date=datetime.now(),member_id=mem1)
        self.pi2 = PhysicalInfo.objects.create(height=75.5, weight=656.6,birth_date=datetime.now(),member_id=mem1)

    def test_my_api_PhysicalInfo_endpoint(self):
        url = reverse('physicalinfo_list_info', )
        data = {'height': '15.5'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_physicalinfoinfo_list(self):
        url = reverse('physicalinfo_list_info')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_new_PhysicalInfo(self):
        url = reverse('physicalinfo_list_info')
        data = {'height':'15.5', 'weight':'65.6' ,}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PhysicalInfo.objects.count(), 2)
        self.assertEqual(PhysicalInfo.objects.get(pk=2).height, 75.5)

    def test_update_existing_PhysicalInfo(self):
        url = reverse('physical_detail_info', kwargs={'pk': self.pi1.pk})
        data = {'height': '47', }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PhysicalInfo.objects.get(pk=self.pi1.pk).height, 15.5)

    def test_delete_existing_PhysicalInfo(self):
        url = reverse('physical_detail_info', kwargs={'pk': self.pi2.pk})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PhysicalInfo.objects.count(), 1)


class MemberAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.mem1 = Member.objects.create(first_name='m1', last_name='l1', username='u1', password='11',
                                     email='manf@lrkj.com', created_date=datetime.now())
        self.mem2 = Member.objects.create(first_name='m2', last_name='l2', username='u2', password='11',
                                     email='m22anf@lsgsfdbrkj.com', created_date=datetime.now())

    def test_my_api_member_endpoint(self):
        url = reverse('members_list_info', )
        data = {'first_name': 'm4'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_member_list(self):
        url = reverse('members_list_info')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_new_member(self):
        url = reverse('members_list_info')
        data = {'first_name':'m5', 'last_name':'l5', 'username':'u5', 'password':'11',
                                     'email':'man55f@lrkj.com' ,}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 3)
        self.assertEqual(Member.objects.get(pk=3).first_name, 'm5')

    def test_update_existing_member(self):
        url = reverse('member_detail_info', kwargs={'pk': self.mem1.pk})
        data = {'first_name':'m8', 'last_name':'l8', 'username':'u1', 'password':'11',
                                     'email':'manf@lrkj.com' ,}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Member.objects.get(pk=self.mem1.pk).first_name, 'm8')

    def test_delete_existing_member(self):
        url = reverse('member_detail_info', kwargs={'pk': self.mem2.pk})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Member.objects.count(), 1)

