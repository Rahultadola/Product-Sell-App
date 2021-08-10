from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product

from datetime import datetime
from django.utils import timezone

class ProductUploadView(LoginRequiredMixin, CreateView):
	model = Product
	template_name = 'products/upload.html'
	value_name = 'Add Product'
	fields = [
		'title', 'description', 'descrip_image', 'price', 'sold', 'featured'
	]

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.date_register = timezone.now()
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['value_name'] = self.value_name
		return context


class ProductDetailView(DetailView):
	model = Product
	template_name = 'products/detail.html'

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Product, id=id_)

class ProductListView(ListView):
	queryset = Product.objects.all()
	paginate_by = 10
	template_name = 'products/product_list.html'
