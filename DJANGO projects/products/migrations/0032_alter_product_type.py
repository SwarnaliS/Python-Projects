# Generated by Django 3.2.9 on 2021-12-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('drinks', 'drinks'), ('treats', 'treats'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
