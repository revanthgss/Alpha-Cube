# Generated by Django 2.1.2 on 2018-10-23 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('reported_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
    ]
