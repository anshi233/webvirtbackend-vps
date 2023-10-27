# Generated by Django 4.2.3 on 2023-10-27 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("network", "0002_ipaddress_is_float_ipaddress_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FloatIP",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "event",
                    models.CharField(
                        blank=True,
                        choices=[("delete", "Deleting"), ("assign", "Assigning"), ("unassign", "Unassigning")],
                        max_length=40,
                        null=True,
                    ),
                ),
                ("cidr", models.CharField(blank=True, max_length=20, null=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField()),
                ("deleted", models.DateTimeField(blank=True, null=True)),
                (
                    "ipaddress",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="network.ipaddress"
                    ),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "FloatingIP",
                "verbose_name_plural": "FloatingIPs",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="FloatIPCounter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.DecimalField(decimal_places=6, default=0.0, max_digits=12)),
                ("started", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("stopped", models.TextField(blank=True, null=True)),
                ("floatip", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="floating_ip.floatip")),
            ],
            options={
                "verbose_name": "FloatingIP Counter",
                "verbose_name_plural": "FloatingIPs Counters",
                "ordering": ["-id"],
            },
        ),
    ]
