# Generated by Django 3.2.9 on 2021-12-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0004_remove_user_days_present'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='days_present',
            field=models.CharField(default=10, max_length=2),
        ),
    ]
