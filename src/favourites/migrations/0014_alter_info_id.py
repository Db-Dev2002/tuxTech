# Generated by Django 4.2.1 on 2023-05-25 22:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("favourites", "0013_alter_info_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="id",
            field=models.UUIDField(
                default="5a966c8edc0348bba008db46e679aded",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
