# Generated by Django 3.1.3 on 2020-12-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='order',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
    ]
