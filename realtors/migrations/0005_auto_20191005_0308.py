# Generated by Django 2.2.6 on 2019-10-05 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_auto_20191005_0302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='owner',
            new_name='owner_name',
        ),
    ]
