# Generated by Django 4.1.3 on 2022-11-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gifs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gifs",
            name="likes",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
