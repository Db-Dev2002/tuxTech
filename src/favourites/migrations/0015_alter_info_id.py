# Generated by Django 4.2.1 on 2023-05-25 23:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("favourites", "0014_alter_info_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="id",
            field=models.UUIDField(
                default="6e8751b71a7b4b5aa169dd2fa8096809",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]