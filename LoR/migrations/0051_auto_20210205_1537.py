# Generated by Django 3.1.2 on 2021-02-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoR', '0050_auto_20210110_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='Eff5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='Roll5',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='Type5',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block'), ('CB', 'Block Counter'), ('CP', 'Pierce Counter'), ('CS', 'Slash Counter'), ('CE', 'Evade Counter'), ('CC', 'Blunt Counter')], default=None, max_length=2, null=True),
        ),
    ]
