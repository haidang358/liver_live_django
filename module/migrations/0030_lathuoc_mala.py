# Generated by Django 4.1.2 on 2023-01-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0029_remove_lathuoc_mala'),
    ]

    operations = [
        migrations.AddField(
            model_name='lathuoc',
            name='maLa',
            field=models.CharField(default='', max_length=255),
        ),
    ]