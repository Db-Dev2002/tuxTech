# Generated by Django 4.2.1 on 2023-05-25 23:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_alter_variant_mediafiles_hash_alter_variant_sku"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variant",
            name="sku",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
