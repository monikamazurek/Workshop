# Generated by Django 2.2.6 on 2020-02-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConferenceRooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
