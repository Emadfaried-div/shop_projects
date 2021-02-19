# Generated by Django 3.1.6 on 2021-02-19 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210219_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCAlternatives', models.ManyToManyField(related_name='accessories_products', to='product.Product')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_product', to='product.product')),
            ],
            options={
                'verbose_name': ' Product_Accessory',
                'verbose_name_plural': ' Product_Accessories',
            },
        ),
    ]
