# Generated by Django 3.1.7 on 2021-03-09 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210305_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='discout_price',
            new_name='discount_price',
        ),
    ]
