from django.contrib import admin
from django.urls import path , include
from .views import add_product 
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'product/' , ProductViewSet)

urlpatterns = [
     path('', include(router.urls)),
    path('add_product/', add_product , name="add_product"),
    # path('get_product_list/', get_all_product , name="list_product"),
    # path('update_product_list/', update_product , name="update_product"),   
]