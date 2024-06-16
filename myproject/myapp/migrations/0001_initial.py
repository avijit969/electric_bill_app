# Generated by Django 5.0.6 on 2024-06-16 06:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('meterReading', models.IntegerField()),
                ('BLSStaffNo', models.IntegerField()),
                ('quatreNO', models.IntegerField()),
                ('image', models.ImageField(upload_to='bills/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
