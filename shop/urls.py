from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('product/<int:product_id>', views.show_product, name='show_product'),
    path('', views.home, name='home'),
]
