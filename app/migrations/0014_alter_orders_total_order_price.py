# Generated by Django 3.2.5 on 2021-08-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_cart_cart_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='total_order_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]