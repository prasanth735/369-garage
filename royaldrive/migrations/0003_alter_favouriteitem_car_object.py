# Generated by Django 5.0.1 on 2024-03-20 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royaldrive', '0002_remove_favouriteitem_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteitem',
            name='car_object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='royaldrive.car'),
        ),
    ]
