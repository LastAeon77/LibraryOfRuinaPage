# Generated by Django 3.1.2 on 2020-12-22 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoR', '0043_auto_20201213_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='Type1',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block'), ('CB', 'Block Counter'), ('CP', 'Pierce Counter'), ('CS', 'Slash Counter'), ('CE', 'Evade Counter'), ('CC', 'Blunt Counter')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='Type2',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block'), ('CB', 'Block Counter'), ('CP', 'Pierce Counter'), ('CS', 'Slash Counter'), ('CE', 'Evade Counter'), ('CC', 'Blunt Counter')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='Type3',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block'), ('CB', 'Block Counter'), ('CP', 'Pierce Counter'), ('CS', 'Slash Counter'), ('CE', 'Evade Counter'), ('CC', 'Blunt Counter')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='Type4',
            field=models.CharField(blank=True, choices=[('BL', 'Blunt'), ('PI', 'Pierce'), ('SL', 'Slash'), ('EV', 'Evade'), ('BO', 'Block'), ('CB', 'Block Counter'), ('CP', 'Pierce Counter'), ('CS', 'Slash Counter'), ('CE', 'Evade Counter'), ('CC', 'Blunt Counter')], default=None, max_length=2, null=True),
        ),
    ]