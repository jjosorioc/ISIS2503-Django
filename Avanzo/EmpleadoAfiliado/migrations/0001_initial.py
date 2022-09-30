# Generated by Django 4.1 on 2022-09-30 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("EmpresaAfiliada", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmpleadoAfiliado",
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
                ("nombre", models.CharField(max_length=50)),
                ("identificacion", models.CharField(max_length=15)),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmpresaAfiliada.empresaafiliada",
                    ),
                ),
            ],
        ),
    ]
