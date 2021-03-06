# Generated by Django 3.1.6 on 2021-02-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_prddiscountprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDISBestSeller',
            field=models.BooleanField(default=False, verbose_name='Best Seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True, verbose_name='New Product '),
        ),
    ]
