# Generated by Django 5.2.3 on 2025-06-17 19:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('products', '0002_productvariant'),
        ('warehouses', '0002_location'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_number', models.CharField(max_length=50)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('manufacture_date', models.DateField(blank=True, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='warehouses.location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_type', models.CharField(choices=[('in', 'Entrada'), ('out', 'Salida'), ('transfer', 'Traslado'), ('adjustment', 'Ajuste')], max_length=20)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=12)),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_movements', to='warehouses.location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('to_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_movements', to='warehouses.location')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
