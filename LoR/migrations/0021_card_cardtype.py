# Generated by Django 3.1.2 on 2020-11-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoR', '0020_auto_20201106_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='CardType',
            field=models.CharField(blank=True, choices=[('M', 'Melee'), ('R', 'Ranged')], default='M', max_length=1, null=True),
        ),
    ]