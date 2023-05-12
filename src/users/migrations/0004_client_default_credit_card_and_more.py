# Generated by Django 4.2 on 2023-05-12 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_address_id_alter_address_postal_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="default_credit_card",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clients_credit_card",
                to="users.creditcard",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="default_invoice_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clients_invoice_address",
                to="users.address",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="default_shipping_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clients_shipping_address",
                to="users.address",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="is_enterprise",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="address",
            name="id",
            field=models.UUIDField(
                default="60817a2b86a24a639bc30687045cba5f",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
