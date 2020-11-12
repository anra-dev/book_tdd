from django.http import HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
	"""домашняя страница"""
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/odin-edinstvennyi-spisok-v-mire/')
	items = Item.objects.all()		
	return render(request, 'home.html')

def view_list(request):
	"""новы список"""
	items = Item.objects.all()		
	return render(request, 'list.html', {'items': items})