# Generated by Django 4.2.4 on 2023-08-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product-img'),
        ),
    ]