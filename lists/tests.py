from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item


class HomePageTest(TestCase):
	"""тест домашней страницы"""

	def test_uses_home_temlates(self):
		"""тест: используется домашний шаблон"""
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
		"""тест: может сохранить POST запрос"""
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
	"""тест модели элемента списка"""

	def test_saving_and_retrieving_items(self):
		"""тест сохранения и получения элементов списка"""
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()

		saved_item = Item.objects.all()
		self.assertEqual(saved_item.count(), 2)

		first_saved_item = saved_item[0]
		second_saved_item = saved_item[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'Item the second')