# Generated by Django 3.0.6 on 2020-06-30 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0017_auto_20200630_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='clss',
            new_name='class_id',
        ),
    ]
