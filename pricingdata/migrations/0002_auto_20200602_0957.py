# Generated by Django 3.0.6 on 2020-06-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricingdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='exchange_country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='exchange_name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='exchange_timezone_short',
            field=models.CharField(max_length=20),
        ),
    ]