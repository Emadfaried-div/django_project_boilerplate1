# Generated by Django 3.1.7 on 2021-03-09 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_remove_orderitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]