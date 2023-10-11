from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('list/', views.product_list, name='product_list'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]