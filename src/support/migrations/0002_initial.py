# Generated by Django 4.2.1 on 2023-05-15 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("support", "0001_initial"),
        ("order", "0003_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="support",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.client"
            ),
        ),
        migrations.AddField(
            model_name="support",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="order.order"
            ),
        ),
    ]
