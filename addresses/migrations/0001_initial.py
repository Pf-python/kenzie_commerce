# Generated by Django 4.1.7 on 2023-03-10 17:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("street", models.CharField(max_length=50)),
                ("district", models.CharField(max_length=50)),
                ("zipCode", models.CharField(max_length=9)),
                ("number", models.IntegerField()),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=2)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
