# Generated by Django 5.0 on 2024-02-15 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
