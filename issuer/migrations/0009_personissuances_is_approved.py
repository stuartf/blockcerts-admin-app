# Generated by Django 2.2.5 on 2019-09-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0008_personissuances_last_reminded_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='personissuances',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]