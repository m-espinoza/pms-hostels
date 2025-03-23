# Generated by Django 5.1.6 on 2025-03-01 14:57

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CashRegister",
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
                ("name", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Descripción"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Activa")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de actualización"
                    ),
                ),
            ],
            options={
                "verbose_name": "Caja",
                "verbose_name_plural": "Cajas",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="CashRegisterEntry",
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
                    "entry_type",
                    models.CharField(
                        choices=[("DEPOSIT", "Ingreso"), ("WITHDRAWAL", "Retiro")],
                        max_length=20,
                        verbose_name="Tipo de movimiento",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.01)],
                        verbose_name="Monto",
                    ),
                ),
                ("description", models.TextField(verbose_name="Descripción")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "cash_register",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entries",
                        to="payments.cashregister",
                        verbose_name="Caja",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="cash_entries",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creado por",
                    ),
                ),
                (
                    "payment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="cash_entries",
                        to="payments.payment",
                        verbose_name="Pago relacionado",
                    ),
                ),
            ],
            options={
                "verbose_name": "Movimiento de caja",
                "verbose_name_plural": "Movimientos de caja",
                "ordering": ["-created_at"],
            },
        ),
    ]
