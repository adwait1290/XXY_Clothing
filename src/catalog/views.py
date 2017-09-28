from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category

class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 9
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        populateContext(self.request,context)
        return context

product_list = ProductListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'category.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category,slug=self.kwargs['slug'])
        populateContext(request,context)
        return context

category = CategoryListView.as_view()


def product(request,slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    populateContext(request,context)
    return render(request,'product.html',context)
def populateContext(request, context):
    context['authenticated'] = request.user.is_authenticated()
    if context['authenticated'] == True:
        print('authenticated')
        context['username'] = request.user.username