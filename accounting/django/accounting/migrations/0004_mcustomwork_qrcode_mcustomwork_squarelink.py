# Generated by Django 4.0.3 on 2022-04-05 10:08

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_auto_20211222_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcustomwork',
            name='qrcode',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='custom/qrcodes/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mcustomwork',
            name='squareLink',
            field=models.CharField(default=datetime.datetime(2022, 4, 5, 10, 8, 36, 467012, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
