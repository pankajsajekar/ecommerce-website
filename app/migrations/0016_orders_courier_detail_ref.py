# Generated by Django 3.2.5 on 2021-08-08 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_courierdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='courier_detail_ref',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.courierdetail'),
        ),
    ]