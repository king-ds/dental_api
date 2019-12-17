# Generated by Django 2.2.7 on 2019-12-17 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('track_record', '0007_treatmentrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentrecord',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Patient'),
        ),
    ]
