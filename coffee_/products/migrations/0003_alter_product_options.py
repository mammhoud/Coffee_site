# Generated by Django 3.2.19 on 2023-05-21 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_ptoduct_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['publish_date']},
        ),
    ]