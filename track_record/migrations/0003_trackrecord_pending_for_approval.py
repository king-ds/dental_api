# Generated by Django 2.2.7 on 2019-12-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track_record', '0002_trackrecord_clinical_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackrecord',
            name='pending_for_approval',
            field=models.BooleanField(default=False),
        ),
    ]
