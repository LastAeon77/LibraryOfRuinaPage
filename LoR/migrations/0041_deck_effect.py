# Generated by Django 3.1.2 on 2020-11-21 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoR', '0040_auto_20201117_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='effect',
            field=models.ManyToManyField(to='LoR.Effects'),
        ),
    ]