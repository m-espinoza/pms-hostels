# Generated by Django 5.1.6 on 2025-03-02 01:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0005_alter_payment_payment_method"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="original_payment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="refunds",
                to="payments.payment",
                verbose_name="Pago original",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_type",
            field=models.CharField(
                choices=[("PAYMENT", "Pago"), ("REFUND", "Reembolso")],
                default="PAYMENT",
                max_length=20,
                verbose_name="Tipo de operación",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Monto"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pendiente"),
                    ("COMPLETED", "Completado"),
                    ("FAILED", "Fallido"),
                    ("REFUNDED", "Reembolsado"),
                    ("PARTIALLY_REFUNDED", "Parcialmente reembolsado"),
                    ("REFUND", "Reembolso"),
                ],
                default="PENDING",
                max_length=20,
                verbose_name="Estado",
            ),
        ),
    ]
