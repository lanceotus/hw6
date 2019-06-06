from django.urls import path
from . import views


app_name = 'django_shop'
urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('products/', views.ProductsPageView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductPageView.as_view(), name='product'),
]
