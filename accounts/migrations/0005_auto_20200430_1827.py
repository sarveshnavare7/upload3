# Generated by Django 3.0.4 on 2020-04-30 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200428_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='Price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        
    ]