from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views

# django admin header customization
admin.site.site_header = "login in Dhaage-Dore"
admin.site.site_title = " Welcome to admin panel "
admin.site.index_title = " Welcome to this portal "

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('singleproduct/<slug:slug>', views.singleproduct, name='singleproduct'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/<int:cartid>', views.checkout, name='checkout'),
    path('ordertracking/', views.ordertracking, name='ordertracking'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
