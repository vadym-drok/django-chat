# Generated by Django 3.2.6 on 2021-08-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='roomname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
