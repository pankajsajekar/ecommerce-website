# Generated by Django 3.2.5 on 2021-07-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210727_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
    ]
