# Generated by Django 5.0.1 on 2024-01-12 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pembayaran', '0005_pembayaran_sudah_dicetak'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembayaran',
            name='sudah_dicetak',
        ),
    ]