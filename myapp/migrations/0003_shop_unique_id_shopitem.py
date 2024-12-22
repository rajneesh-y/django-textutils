# Generated by Django 5.1.3 on 2024-12-22 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_rename_image_shop"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="unique_id",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.CreateModel(
            name="ShopItem",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="images")),
                ("added_date", models.DateTimeField()),
                (
                    "shopId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.shop"
                    ),
                ),
            ],
        ),
    ]