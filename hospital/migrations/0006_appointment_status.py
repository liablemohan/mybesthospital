# Generated by Django 3.0.5 on 2022-05-20 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
