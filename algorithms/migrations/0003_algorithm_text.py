# Generated by Django 2.1 on 2018-09-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0002_auto_20180908_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
