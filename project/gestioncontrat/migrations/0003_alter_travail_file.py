# Generated by Django 4.1.2 on 2022-10-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestioncontrat", "0002_remove_travail_date_resiliation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="travail",
            name="file",
            field=models.FileField(blank=True, upload_to="uploads_files/"),
        ),
    ]
