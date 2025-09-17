from django.contrib import admin
from django.urls import path , include
from .views import add_product , get_all_product
urlpatterns = [
    path('add_product/', add_product , name="add_product"),
    path('get_product_list/', get_all_product , name="list_product"),
    
]