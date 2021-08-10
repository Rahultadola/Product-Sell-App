from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProductUploadView, ProductDetailView, ProductListView


app_name = 'products'

urlpatterns = [    
    path('detail/<int:id>', ProductDetailView.as_view(), name='product-detail'),
    path('add/', ProductUploadView.as_view(), name='upload'),
    path('list/', ProductListView.as_view(), name="list")
]
