from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
    
class Collection(models.Model):
    title = models.CharField(max_length=255)
    # Resolving Circular relationships
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(default='-')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    Collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER ='S'
    MEMBERSHIP_GOLD = 'G'
    
    #Model Choice
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'BRONZE'),
        (MEMBERSHIP_SILVER, 'SILVER'),
        (MEMBERSHIP_GOLD, 'GOLD')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
     
    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['last_name','first_name'])
        ]
    
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICE = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICE, default=PAYMENT_STATUS_PENDING )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    
    
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10,default='0000')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField() 