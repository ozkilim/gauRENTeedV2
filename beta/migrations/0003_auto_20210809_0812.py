# Generated by Django 3.1.6 on 2021-08-09 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0002_property_redlandscore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='send_daily_emails',
            new_name='happyToBeContacted',
        ),
    ]