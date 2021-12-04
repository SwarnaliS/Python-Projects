# Generated by Django 3.2.9 on 2021-12-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('treats', 'treats')], max_length=60),
        ),
    ]
