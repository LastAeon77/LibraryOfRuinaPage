# Generated by Django 3.1.2 on 2020-11-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoR', '0035_auto_20201114_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='Description',
            field=models.TextField(),
        ),
    ]
