# Generated by Django 3.2.9 on 2021-12-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='days_present',
            field=models.CharField(default=6, max_length=2),
        ),
    ]