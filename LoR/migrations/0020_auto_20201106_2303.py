# Generated by Django 3.1.2 on 2020-11-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoR', '0019_auto_20201106_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='Type1',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='Type2',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='Type3',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='Type4',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block')], default=None, max_length=2, null=True),
        ),
    ]