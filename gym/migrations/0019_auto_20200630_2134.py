# Generated by Django 3.0.6 on 2020-06-30 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0018_auto_20200630_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.Classes'),
        ),
    ]
