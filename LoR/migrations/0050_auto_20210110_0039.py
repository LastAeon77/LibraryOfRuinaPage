# Generated by Django 3.1.2 on 2021-01-10 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoR', '0049_abnocards_emotion_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abnocards',
            old_name='Office',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Office',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='Office',
            new_name='office',
        ),
    ]
