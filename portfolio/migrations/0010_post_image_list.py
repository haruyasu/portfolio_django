# Generated by Django 2.2.1 on 2019-07-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20190711_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_list',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
