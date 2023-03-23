# Generated by Django 4.1.7 on 2023-03-23 20:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0004_remove_client_is_staff_client_receive_news_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="first_name",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="client",
            name="gender",
            field=models.CharField(
                choices=[
                    ("M", "Male"),
                    ("F", "Female"),
                    ("O", "Other"),
                    ("N", "Prefer not to say"),
                ],
                default="N",
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="last_name",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=30)),
                ("last_name", models.CharField(blank=True, max_length=30)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("O", "Other"),
                            ("N", "Prefer not to say"),
                        ],
                        default="O",
                        max_length=1,
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=150, null=True, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="admin_set",
                        related_query_name="admin",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="admin_set",
                        related_query_name="admin",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
