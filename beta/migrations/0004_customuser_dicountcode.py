# Generated by Django 3.1.6 on 2021-08-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0003_auto_20210809_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dicountcode',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
