# Generated by Django 5.1.7 on 2025-05-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite', models.PositiveIntegerField()),
            ],
        ),
    ]
