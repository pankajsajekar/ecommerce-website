# Generated by Django 3.2.5 on 2021-08-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_products_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_img',
            field=models.ImageField(upload_to='blogimages/'),
        ),
    ]