# Generated by Django 2.2.1 on 2019-07-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_remove_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.CharField(max_length=200, null=True),
        ),
    ]