from django.db import models
from django.conf import settings
from catalog.models import Product
class CartItemManager(models.Manager):
    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists():
            created   = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            
            p = Product.objects.get(id = product.id)
            cart_item.image = p.image
            cart_item.save()
        else:
            created   = True
            cart_item = CartItem.objects.create(
                cart_key=cart_key, product=product, price=product.price
            )
        return cart_item, created


class CartItem(models.Model):
    cart_key = models.CharField('Cart Key',max_length=40,db_index=True)
    product  = models.ForeignKey('catalog.Product',verbose_name='Product')
    quantity = models.PositiveIntegerField('Quantity',default=1)
    price    = models.DecimalField('Price',decimal_places=2,max_digits=8)
    image = models.ImageField("Image",max_length=100, null=True)
    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item in cart'
        verbose_name_plural = 'Items in cart'
        unique_together = (('cart_key','product'))

    def __str__(self):
        return '{} [{}]'.format(self.product,self.quantity)

        
class OrderManager(models.Manager):
    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order, quantity=cart_item.quantity, product=cart_item.product, price=cart_item.price
            )
        return order

class Order(models.Model):
    STATUS_CHOICES = (
        (0,'Awaiting Payment'),
        (1,'Concluded'),
        (2,'Cancelled'),
    )

    PAYMENT_OPTION_CHOICES = (
        ('deposit','Deposit'),
        ('Payment','Payment'),
        ('paypal','PayPal'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User')
    status = models.IntegerField('Status', choices=STATUS_CHOICES, default=0, blank=True)
    payment_option = models.CharField('Payment options', choices=PAYMENT_OPTION_CHOICES, max_length=20, default='deposit')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order #{}'.format(self.pk)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Order', related_name='items')
    product = models.ForeignKey('catalog.Product', verbose_name='Product')
    quantity = models.PositiveIntegerField('Quantity', default=1)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return '[{}] {}'.format(self.order, self.product)

def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()

models.signals.post_save.connect(post_save_cart_item,sender=CartItem,dispatch_uid='post_save_cart_item')