# Generated by Django 2.1.2 on 2019-01-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0003_auto_20181023_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='victim',
            name='rescued',
            field=models.BooleanField(default=False),
        ),
    ]
