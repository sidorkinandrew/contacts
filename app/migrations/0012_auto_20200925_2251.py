# Generated by Django 3.1.1 on 2020-09-25 22:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200925_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 22, 51, 15, 972107, tzinfo=utc)),
        ),
    ]
