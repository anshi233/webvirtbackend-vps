# Generated by Django 4.2 on 2023-07-14 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("image", "0003_image_source"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageError",
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
                ("event", models.CharField(blank=True, max_length=40, null=True)),
                ("message", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="image.image"
                    ),
                ),
            ],
            options={
                "verbose_name": "Image Error",
                "verbose_name_plural": "Image Errors",
                "ordering": ["-id"],
            },
        ),
    ]
