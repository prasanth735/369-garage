# Generated by Django 5.0.1 on 2024-03-21 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royaldrive', '0007_alter_favouriteitem_car_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteitem',
            name='car_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='royaldrive.car'),
        ),
    ]
