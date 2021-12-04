# Generated by Django 3.2.9 on 2021-12-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('treats', 'treats'), ('drinks', 'drinks'), ('entrees', 'entrees')], max_length=60),
        ),
    ]