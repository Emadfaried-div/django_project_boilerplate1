# Generated by Django 3.1.7 on 2021-03-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20210313_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear'), ('E', 'Electronics'), ('HA', 'Home accessories'), ('HD', 'Home electric devices'), ('L', 'Laptop')], max_length=2),
        ),
    ]