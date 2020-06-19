# Generated by Django 3.0.6 on 2020-06-13 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('isin_no', models.CharField(max_length=50)),
                ('is_listed_nse', models.BooleanField(default=False)),
                ('nse_ticker', models.CharField(max_length=50, null=True)),
                ('nse_tracker', models.BooleanField(default=False)),
                ('nse_price_update_db_date', models.DateField(null=True)),
                ('nse_return_update_date', models.DateField(null=True)),
                ('finance_update_date', models.DateField(null=True)),
                ('sentiment_update_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('exchange_name', models.CharField(db_index=True, max_length=100)),
                ('exchange_code', models.CharField(db_index=True, max_length=50)),
                ('exchange_country', models.CharField(max_length=50)),
                ('exchange_timezone', models.CharField(max_length=50)),
                ('exchange_timezone_short', models.CharField(max_length=50)),
                ('exchange_currency', models.CharField(max_length=20)),
                ('timezone_gmt_off_milliseconds', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('ticker', models.CharField(max_length=50, null=True)),
                ('price_update_date', models.DateField(null=True)),
                ('return_update_date', models.DateField(null=True)),
                ('exchange', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datascrape.Exchange')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndustrySector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('industry', models.CharField(db_index=True, max_length=300)),
                ('sector', models.CharField(max_length=300)),
                ('details', models.CharField(max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TickerHistoricDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(db_index=True)),
                ('price_high', models.FloatField(null=True)),
                ('price_low', models.FloatField(null=True)),
                ('price_close', models.FloatField(null=True)),
                ('price_open', models.FloatField(null=True)),
                ('price_close_adjusted', models.FloatField(null=True)),
                ('volume', models.FloatField(null=True)),
                ('dividends', models.FloatField(default=0, null=True)),
                ('stock_split', models.FloatField(default=0, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datascrape.Company')),
                ('exchange', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datascrape.Exchange')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndexHistoricDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(db_index=True)),
                ('price_high', models.FloatField(null=True)),
                ('price_low', models.FloatField(null=True)),
                ('price_close', models.FloatField(null=True)),
                ('price_open', models.FloatField(null=True)),
                ('price_close_adjusted', models.FloatField(null=True)),
                ('volume', models.FloatField(null=True)),
                ('exchange', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datascrape.Exchange')),
                ('index', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datascrape.Index')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='company',
            name='industry_sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='datascrape.IndustrySector'),
        ),
    ]
