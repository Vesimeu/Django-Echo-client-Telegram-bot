# Generated by Django 5.0.1 on 2024-03-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status_orders',
            field=models.BooleanField(default=False),
        ),
    ]
