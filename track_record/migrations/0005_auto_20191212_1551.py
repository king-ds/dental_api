# Generated by Django 2.2.7 on 2019-12-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track_record', '0004_auto_20191212_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentalchart',
            name='kind',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dentalchart',
            name='teeth_number',
            field=models.IntegerField(null=True),
        ),
    ]
