from django import forms
from django.forms import TextInput, EmailInput, Textarea, Select, FileInput
from app.models import Contact, Orders, Cart, CustomePaymentMethod


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control"
                }),
            "email": EmailInput(
                attrs={
                    "class": "form-control"
                }),
            "query": TextInput(
                attrs={
                    "class": "form-control"
                }),
            "desc": Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }),
        }


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["customer_name","customer_address","customer_contry","customer_state","customer_city","city_zip","customer_email","customer_mobile_number"]

        widgets = {
            "customer_name": TextInput(
                attrs={
                    "class": "form-control"
                }),
            "customer_address": Textarea(
                attrs={
                    "class": "form-control",
                             "rows": 2,
                }),
            "customer_contry": Select(
                attrs={
                    "class": "custom-select d-block"
                }),
            "customer_state": TextInput(
                attrs={
                    "class": "form-control d-block"
                }),
            "customer_city": TextInput(
                attrs={
                    "class": "form-control d-block"
                }),
            "city_zip": TextInput(
                attrs={
                    "class": "form-control d-block"
                }),
            "customer_email": EmailInput(
                attrs={
                    "class": "form-control",
                    'placeholder': 'you@example.com'
                }),
            "customer_mobile_number": TextInput(
                attrs={
                    "class": "form-control",
                    'type':'number'
                }),
        }

class AddCustomePaymentMethodForm(forms.ModelForm):
    class Meta:
        model = CustomePaymentMethod
        fields = ["upi_transaction_id","upi_id","payment_proof"]

        widgets = {
            "upi_transaction_id": TextInput(
                attrs={
                    "class": "form-control"
                }),
            "upi_id": TextInput(
                attrs={
                    "class": "form-control"
                }),
            "payment_proof": FileInput(
                attrs={
                    "class": "file-field"
                }),

        }

class CartFrom(forms.Form):
    products_cart = forms.CharField(max_length=1000, widget=forms.HiddenInput())
