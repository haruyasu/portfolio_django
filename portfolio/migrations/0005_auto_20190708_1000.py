# Generated by Django 2.2.1 on 2019-07-08 14:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20190708_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 8, 14, 0, 58, 970817, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 8, 14, 0, 58, 970817, tzinfo=utc)),
        ),
    ]
