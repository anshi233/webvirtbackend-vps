# Generated by Django 4.1.3 on 2022-11-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("region", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Size",
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
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("vcpu", models.IntegerField()),
                ("disk", models.BigIntegerField()),
                ("memory", models.BigIntegerField()),
                ("transfer", models.BigIntegerField()),
                ("is_active", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                ("deleted", models.DateTimeField(blank=True, null=True)),
                (
                    "price",
                    models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
                ),
                (
                    "regions",
                    models.ManyToManyField(related_name="regions", to="region.region"),
                ),
            ],
            options={
                "verbose_name": "Size",
                "verbose_name_plural": "Sizes",
                "ordering": ["memory", "vcpu", "disk", "transfer"],
            },
        ),
    ]
