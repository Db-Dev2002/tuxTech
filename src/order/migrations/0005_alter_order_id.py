# Generated by Django 4.2.1 on 2023-05-13 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0004_alter_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.UUIDField(
                default="fecefb442ceb4f92a4e0d4ea31b89340",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]