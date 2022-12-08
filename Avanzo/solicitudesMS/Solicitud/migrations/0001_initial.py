# Generated by Django 4.1 on 2022-09-30 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("AsesorAvanzo", "0001_initial"),
        ("EmpleadoAfiliado", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Solicitud",
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
                ("cantidad", models.FloatField()),
                ("fechaPago", models.DateField()),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("EE", "En Espera"),
                            ("AP", "Aprobado"),
                            ("RP", "Reprobado"),
                            ("RE", "Reintente subiendo documentos más fiables"),
                        ],
                        default="EE",
                        max_length=2,
                    ),
                ),
                (
                    "asesor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AsesorAvanzo.asesoravanzo",
                    ),
                ),
                (
                    "empleadoAfiliado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmpleadoAfiliado.empleadoafiliado",
                    ),
                ),
            ],
        ),
    ]