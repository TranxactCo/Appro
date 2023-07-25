# Generated by Django 4.2.3 on 2023-07-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_product_name_order_size_order_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('en_attente', 'En attente'), ('en_cours', 'En cours'), ('terminee', 'Terminée')], default='En_attente', max_length=20),
        ),
    ]