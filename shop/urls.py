from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('product/<int:product_id>', views.show_product, name='show_product'),
    path('', views.home, name='home'),
    path('all_products', views.all_products, name='all_products'),
]
