# Generated by Django 4.2.1 on 2023-05-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0006_alter_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.UUIDField(
                default="43421d16817c4603a55908dd2a4cf1ee",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]