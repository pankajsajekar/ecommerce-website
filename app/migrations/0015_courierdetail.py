# Generated by Django 3.2.5 on 2021-08-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_orders_total_order_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourierDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_delivery_date', models.DateTimeField()),
                ('end_delivery_date', models.DateTimeField()),
                ('company_name', models.CharField(max_length=100)),
                ('contact_no', models.BigIntegerField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('tracking_id', models.CharField(max_length=200)),
            ],
        ),
    ]