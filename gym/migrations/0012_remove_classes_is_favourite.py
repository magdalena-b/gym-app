# Generated by Django 3.0.6 on 2020-06-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0011_auto_20200625_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='is_favourite',
        ),
    ]