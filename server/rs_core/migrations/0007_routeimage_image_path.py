# Generated by Django 3.1.1 on 2021-01-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rs_core', '0006_auto_20201204_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeimage',
            name='image_path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
