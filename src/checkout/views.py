# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# import stripe 



from django.template.context_processors import csrf
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render,render_to_response
from django.contrib import messages
from django.views.generic import RedirectView, TemplateView
from django.forms import modelformset_factory
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from checkout.models import CartItem
from catalog.models import Product
from .models import CartItem, Order
import stripe
class CreateCartItemView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if(self.request.user.is_authenticated):
            product = get_object_or_404(Product,slug=self.kwargs['slug'])
            if self.request.session.session_key is None:
                self.request.session.save()
                print image_url
            cart_item, created = CartItem.objects.add_item(
                self.request.session.session_key , product
            )
        else:

            return reverse('login')
        if created:
            messages.success(self.request,'Product added successfully')
        else:
            messages.success(self.request, 'Product updated successfully')
        return reverse('checkout:cart_item')

class CartItemView(TemplateView):
    template_name = 'cart.html'

    def get_formset(self, clear=False):
        context = {}
        populateContext(self.request,context)
        session = self.request.session.session_key
        if session and CartItem.objects.filter(cart_key=session).exists():
            CartItemFormSet = modelformset_factory(
                CartItem,fields=('quantity',), can_delete=True, extra=0
            )
            session_key = self.request.session.session_key
            if session_key:
                if clear:
                    formset = CartItemFormSet(queryset=CartItem.objects.filter(cart_key=session_key))
                else:
                    formset = CartItemFormSet(
                        queryset=CartItem.objects.filter(cart_key=session_key),
                        data=self.request.POST or None
                    )
            else:
                formset = CartItemFormSet(queryset=CartItem.objects.none(), data=self.request.POST or None)
            

            return formset
        else:
            messages.info(self.request,'There are no items in your cart')
            return redirect('catalog:product_list')
    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        populateContext(self.request,context)
        populateCart(self.request, context)
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        populateContext(request,context)
        if formset.is_valid():
            formset.save()
            messages.success(request,'Cart updated successfully')
            context['formset'] = self.get_formset(clear=True)


        return self.render_to_response(context)


def finish(request):
    template = "finish.html"
    context = {}
    if request.method == "POST" and request.is_ajax():
        context['email'] = request.POST.get('email')
        context['last4'] = request.POST.get('last4')
        context['ip'] = request.POST.get('ip')
        context['cart_id'] = request.POST.get('cart_id')

        c = CartItem.objects.filter(cart_key=request.session.session_key)
        print c
        o = Order.objects.create_order(request.user, c)
        print o
        o.save()
        for cart_item in c:
            id = cart_item.id
            CartItem.objects.get(id=id).delete()
        # context['card_last_4'] = data.card.last4
        # context['email'] = data.card.name
        # context['ip'] = data.client_ip
    return render(request,template,context)

create_cartitem = CreateCartItemView.as_view()
cart_item       = CartItemView.as_view()
        
def remove_item(request,id):
    u = CartItem.objects.get(id=id).delete()
    return redirect('/checkout/cart')
def minus(request,id):
    i = CartItem.objects.get(id=id)
    i.quantity -= 1
    print i.quantity
    i.save()
    return redirect('/checkout/cart')
def plus(request,id):
    print id
    i = CartItem.objects.get(id=id)
    i.quantity += 1;
    print i.quantity
    i.save()
    return redirect('/checkout/cart')

def populateContext(request, context):
    context['authenticated'] = request.user.is_authenticated()
    if context['authenticated'] == True:
        print('authenticated')
        context['username'] = request.user.username
def populateCart(request, context):
    session = request.session.session_key
    if session and CartItem.objects.filter(cart_key=session).exists():
        context['cart'] = CartItem.objects.filter(cart_key=session)
        print context['cart']
        print context['cart'].count()
        context['cart_count'] = context['cart'].count()
    else:
        print "cart is empty"
stripe.api_key = "sk_test_6noC0mT4dyaQZlKCMEtqPvJZ"
# Create your views here.


