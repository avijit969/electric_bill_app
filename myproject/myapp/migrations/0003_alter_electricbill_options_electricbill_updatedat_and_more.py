# Generated by Django 5.0.6 on 2024-06-16 10:02

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_electricbill_comment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electricbill',
            options={'ordering': ['-createdAt'], 'verbose_name': 'Electric Bill', 'verbose_name_plural': 'Electric Bills'},
        ),
        migrations.AddField(
            model_name='electricbill',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='electricbill',
            name='BLSStaffNo',
            field=models.PositiveIntegerField(verbose_name='BLS Staff Number'),
        ),
        migrations.AlterField(
            model_name='electricbill',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='electricbill',
            name='image',
            field=models.ImageField(upload_to='bills/', verbose_name='Bill Image'),
        ),
        migrations.AlterField(
            model_name='electricbill',
            name='meterReading',
            field=models.PositiveIntegerField(verbose_name='Meter Reading'),
        ),
        migrations.AlterField(
            model_name='electricbill',
            name='quatreNO',
            field=models.PositiveIntegerField(verbose_name='Quarter Number'),
        ),
        migrations.AlterField(
            model_name='electricbill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
