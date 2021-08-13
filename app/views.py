import json
from decimal import Decimal

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.form import AddContactForm, CartFrom, AddOrderForm, AddCustomePaymentMethodForm
from app.models import Products, ProductImage, Orders, Cart, CartProductInfo, CustomePaymentMethod, OrderProductInfo


def index(request):
    product = Products.objects.all().order_by('-time')[:4]
    context = {"products": product}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def products(request):
    product = Products.objects.all()
    newproduct = request.GET.get('new', 1)
    if 'new' in request.GET:
        print("new product")
        product = Products.objects.all().order_by('-time')
    elif 'lowtohigh' in request.GET:
        product = Products.objects.all().order_by('product_price')
    elif 'hightolow' in request.GET:
        product = Products.objects.all().order_by('-product_price')

    page = request.GET.get('page', 1)

    paginator = Paginator(product, 6)  # 3 show product per page
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    context = {"products": product}
    return render(request, 'products.html', context)


def singleproduct(request, slug):
    sproduct = Products.objects.get(product_slug=slug)
    product_imgs = ProductImage.objects.filter(product=sproduct)
    context = {"sproduct": sproduct, "product_images": product_imgs}
    return render(request, "singleproduct.html", context)


def contact(request):
    form = AddContactForm()
    if request.method == 'POST':
        form = AddContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')

    context = {"form": form}
    return render(request, 'contact.html', context)


def cart(request):
    if request.method == 'POST':
        products_cart = request.POST.get('product_cart')
        products_cart = json.loads(products_cart)
        if products_cart:
            cart_obj = Cart.objects.create()
            final_total = Decimal('0.0')
            for c_product in products_cart:
                product_id = c_product
                product = Products.objects.get(id=product_id)
                product_qtty = products_cart[c_product][0]
                single_price = product.product_price
                total_price = single_price * int(product_qtty)
                cpi_obj = CartProductInfo.objects.create(product=product, product_quantity=product_qtty,
                                                         single_product_price=single_price,
                                                         total_product_price=total_price)
                cpi_obj.save()
                cart_obj.products_cart.add(cpi_obj)
                final_total = final_total + Decimal(total_price)
            print("okay")
            cart_obj.cart_total = Decimal(final_total)
            cart_obj.save()
            return redirect('checkout', cart_obj.id)
        else:
            return redirect('cart')
    return render(request, 'mycart.html')


def checkout(request, cartid):
    cart_obj = Cart.objects.get(id=cartid)
    form = AddOrderForm()
    payment_form = AddCustomePaymentMethodForm()
    if request.method == 'POST':
        form = AddOrderForm(request.POST, request.FILES)
        payment_form = AddCustomePaymentMethodForm(request.POST, request.FILES)
        if form.is_valid() and payment_form.is_valid():
            newform = form.save(commit=False)
            newpaymentform = payment_form.save(commit=False)

            order_obj = Orders.objects.create(customer_name=newform.customer_name,
                                              customer_address=newform.customer_address,
                                              customer_contry=newform.customer_contry,
                                              customer_state=newform.customer_state,
                                              customer_city=newform.customer_city,
                                              city_zip=newform.city_zip,
                                              customer_email=newform.customer_email,
                                              customer_mobile_number=newform.customer_mobile_number)

            final_total = Decimal('0.0')
            for c_product in cart_obj.products_cart.all():
                product_id = c_product.product.id
                product = Products.objects.get(id=product_id)
                oder_prod_info_obj = OrderProductInfo.objects.create(product=product,
                                                                     product_quantity=c_product.product_quantity,
                                                                     single_product_price=c_product.single_product_price,
                                                                     total_product_price=c_product.total_product_price)
                oder_prod_info_obj.save()
                order_obj.products.add(oder_prod_info_obj)
                final_total = final_total + c_product.total_product_price

            order_obj.order_status = "1"
            order_obj.order_payment_type = "3"
            order_obj.order_payment_status = "2"
            order_obj.total_order_price = final_total

            order_payment = CustomePaymentMethod.objects.create(upi_transaction_id=newpaymentform.upi_transaction_id,
                                                                upi_id=newpaymentform.upi_id,
                                                                payment_proof=newpaymentform.payment_proof)
            order_payment.save()
            order_obj.custom_payment_ref = order_payment
            order_obj.save()

            context = {"ordersuccess": True, "orderid": order_obj.id}
            return render(request, 'checkout.html', context)

    context = {"cart_obj": cart_obj, "form": form, "payment_form": payment_form}
    return render(request, 'checkout.html', context)


def ordertracking(request):

    if request.method == 'POST':
        orderid = request.POST.get('orderid')
        emailid = request.POST.get('emailid')
        context = {}
        if orderid and emailid :
            order_obj = Orders.objects.filter(id=orderid, customer_email=emailid)
            if order_obj:
                for order_obj in order_obj:
                    order_obj = order_obj
                context = {"orderstatus": True, 'order_obj': order_obj}
            else:
                context = {"orderstatus": False}
        else:
            context = {"orderstatus": False}

        return render(request, 'ordertrackingdetails.html', context)

    return render(request, 'ordertracking.html')

