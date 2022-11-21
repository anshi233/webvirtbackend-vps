# Generated by Django 4.1.3 on 2022-11-21 19:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("region", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("custom", "Custom"),
                            ("backup", "Backup"),
                            ("snapshot", "Snapshot"),
                            ("application", "Application"),
                            ("distribution", "Distribution"),
                        ],
                        default="snapshot",
                        max_length=50,
                    ),
                ),
                ("md5sum", models.CharField(max_length=50)),
                (
                    "distribution",
                    models.CharField(
                        choices=[
                            ("custom", "Custom"),
                            ("backup", "Backup"),
                            ("snapshot", "Snapshot"),
                            ("application", "Application"),
                            ("distribution", "Distribution"),
                        ],
                        default="unknown",
                        max_length=50,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("file_name", models.CharField(max_length=100)),
                ("file_size", models.BigIntegerField(blank=True, null=True)),
                ("disk_size", models.BigIntegerField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                ("deleted", models.DateTimeField(blank=True, null=True)),
                ("regions", models.ManyToManyField(blank=True, to="region.region")),
            ],
            options={
                "verbose_name": "Image",
                "verbose_name_plural": "Images",
                "ordering": ["-id"],
            },
        ),
    ]
