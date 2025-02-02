# Generated by Django 5.1.4 on 2025-01-12 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='Model')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release date')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the supplier', max_length=255, verbose_name='Supplier name')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Debt')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='ChainUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('house_number', models.CharField(max_length=10, verbose_name='House number')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Debt to supplier')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('level', models.IntegerField(choices=[(0, 'Factory'), (1, 'Retail chain'), (2, 'Individual entrepreneur')])),
                ('products', models.ManyToManyField(related_name='chain_units', to='market.product', verbose_name='Products')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
    ]
