# Generated by Django 5.1.1 on 2024-10-12 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartitem_product_alter_cart_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
    ]