# Generated by Django 2.2.1 on 2019-07-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20190713_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
