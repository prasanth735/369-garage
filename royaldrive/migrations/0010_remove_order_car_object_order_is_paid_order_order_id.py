# Generated by Django 5.0.1 on 2024-03-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royaldrive', '0009_order_orderitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='car_object',
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
