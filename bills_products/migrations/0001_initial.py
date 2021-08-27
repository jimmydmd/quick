# Generated by Django 3.2.6 on 2021-08-27 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bills', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillsProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_bills_billsproducts', to='bills.bills')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_products_billsproducts', to='products.products')),
            ],
        ),
    ]