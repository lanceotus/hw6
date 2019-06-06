from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django_shop.models import Product


class IndexPageView(TemplateView):
    template_name = 'django_shop/index.html'

    # не особо нужно делать это так, но для разнообразия пусть будет
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'greet': 'Добро пожаловать!'
        })
        return context


class ProductsPageView(ListView):
    template_name = 'django_shop/products.html'
    model = Product


class ProductPageView(DetailView):
    template_name = 'django_shop/product.html'
    model = Product


def handler404(request, exception):
    return render(request, 'django_shop/404.html', status=404)
