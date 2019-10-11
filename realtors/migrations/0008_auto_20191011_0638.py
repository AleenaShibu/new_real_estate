# Generated by Django 2.2.6 on 2019-10-11 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0007_remove_comment_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realtor',
            name='price',
            field=models.PositiveIntegerField(default=100000),
        ),
    ]
