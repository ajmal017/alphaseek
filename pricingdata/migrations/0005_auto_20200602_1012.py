# Generated by Django 3.0.6 on 2020-06-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricingdata', '0004_auto_20200602_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='isin_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(db_index=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='company',
            name='nse_ticker',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
