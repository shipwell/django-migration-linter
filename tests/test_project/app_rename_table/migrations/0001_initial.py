# Generated by Django 1.11.18 on 2019-04-14 15:00


from __future__ import annotations

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="A",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field", models.IntegerField()),
            ],
        )
    ]
