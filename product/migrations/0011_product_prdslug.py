# Generated by Django 3.1.6 on 2021-02-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_prdimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]