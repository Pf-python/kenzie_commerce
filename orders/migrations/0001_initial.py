# Generated by Django 4.1.7 on 2023-03-10 20:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("EM ANDAMENTO", "Em Andamento"),
                            ("ENTREGUE", "Entregue"),
                            ("PEDIDO REALIZADO", "Default"),
                        ],
                        default="PEDIDO REALIZADO",
                        max_length=50,
                    ),
                ),
                ("createdAt", models.DateField(blank=True, null=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
