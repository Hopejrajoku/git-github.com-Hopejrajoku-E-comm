# Generated by Django 4.2.4 on 2023-09-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suggestion',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]