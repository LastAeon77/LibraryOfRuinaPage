# Generated by Django 3.1.2 on 2020-11-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoR', '0041_deck_effect'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='BluntResist',
            field=models.CharField(default='Normal', max_length=100),
        ),
        migrations.AddField(
            model_name='page',
            name='BluntStaggerResist',
            field=models.CharField(default='Normal', max_length=100),
        ),
        migrations.AddField(
            model_name='page',
            name='HP',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='PierceResist',
            field=models.CharField(default='Normal', max_length=100),
        ),
        migrations.AddField(
            model_name='page',
            name='PierceStaggerResist',
            field=models.CharField(default='Normal', max_length=100),
        ),
        migrations.AddField(
            model_name='page',
            name='RangeType',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='SlashResist',
            field=models.CharField(default='Normal', max_length=100),
        ),
        migrations.AddField(
            model_name='page',
            name='SlashStaggerResist',
            field=models.CharField(default='Normal', max_length=100),
        ),
        migrations.AddField(
            model_name='page',
            name='Speed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='SpeedDiceNum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='SpeedMin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='Stagger',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
