# Generated by Django 3.2.13 on 2022-12-02 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_runtime',
            field=models.CharField(default=2, max_length=15),
            preserve_default=False,
        ),
    ]
