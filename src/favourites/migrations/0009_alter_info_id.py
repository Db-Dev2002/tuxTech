# Generated by Django 4.2.1 on 2023-05-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("favourites", "0008_alter_info_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="id",
            field=models.UUIDField(
                default="44b334a6e3844f6bbeb8f4bf50d6a0bf",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]