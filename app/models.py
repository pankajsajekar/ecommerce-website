from django.db import models
from django_resized import ResizedImageField
# Create your models here.
from django.utils.text import slugify


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    query = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.name + " - " + self.query


class Products(models.Model):
    product_img = models.ImageField(upload_to="blogimages/", blank=False)
    product_title = models.CharField(max_length=30, unique=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_desc = models.TextField()
    product_count = models.CharField(max_length=10)
    product_slug = models.SlugField(blank=True, null=True, unique=True)
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.product_title)
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_title


class ProductImage(models.Model):
    product = models.ForeignKey(Products, verbose_name='Product Title', default=None, on_delete=models.CASCADE)
    product_images = models.ImageField(verbose_name='Image', upload_to='blogimages/')

    class Meta:
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.product_title


class OrderProductInfo(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Products, models.SET_NULL, blank=True, null=True)
    product_quantity = models.IntegerField()
    single_product_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.product_title


class CustomePaymentMethod(models.Model):
    made_on = models.DateTimeField(auto_now_add=True)
    upi_transaction_id = models.CharField(max_length=100)
    upi_id = models.CharField(max_length=200)
    payment_proof = models.FileField(upload_to="paymentproof/")

    def __str__(self):
        return str(self.id)


class CourierDetail(models.Model):
    start_delivery_date = models.DateTimeField()
    end_delivery_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    contact_no = models.BigIntegerField()
    contact_email = models.EmailField()
    tracking_id = models.CharField(max_length=200)



class Orders(models.Model):
    order_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    contry_choice = (('1', 'India'), ('2', 'USA'), ('3', 'Canada'), ('4', 'Bhutan'), ('5', 'Japan'))
    oderpayment_choice = (('1', 'Paytm'), ('2', 'Razorpay'), ('3', 'Custome'))
    orderstatus_choice = (('1', 'Placed'), ('2', 'Confirm'), ('3', 'Out for Delivery'), ('4', 'Complete'), ('5', 'Failed'))
    orderpaymentstatus_choice = (('1', 'Paid'), ('2', 'Pending'), ('3', 'Failed'))
    customer_name = models.CharField(max_length=200)
    customer_address = models.TextField()
    customer_contry = models.CharField(max_length=30, choices=contry_choice)
    customer_state = models.CharField(max_length=100)
    customer_city = models.CharField(max_length=100)
    city_zip = models.IntegerField()
    customer_email = models.EmailField()
    customer_mobile_number = models.BigIntegerField()
    products = models.ManyToManyField(OrderProductInfo)
    order_status = models.CharField(max_length=100, choices=orderstatus_choice)
    order_payment_type = models.CharField(max_length=100, choices=oderpayment_choice)
    order_payment_status = models.CharField(max_length=100, choices=orderpaymentstatus_choice)
    total_order_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    custom_payment_ref = models.OneToOneField(CustomePaymentMethod, models.SET_NULL, blank=True, null=True)
    courier_detail_ref = models.OneToOneField(CourierDetail, models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return str(self.id)


class CartProductInfo(models.Model):
    product = models.ForeignKey(Products, models.SET_NULL, blank=True, null=True)
    product_quantity = models.IntegerField()
    single_product_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.product_title


class Cart(models.Model):
    products_cart = models.ManyToManyField(CartProductInfo)
    cart_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)




