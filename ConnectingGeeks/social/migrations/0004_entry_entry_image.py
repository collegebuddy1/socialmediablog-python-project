# Generated by Django 2.2.7 on 2019-11-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20191111_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entry_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]