# Generated by Django 4.1.2 on 2022-11-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpleadoAfiliado', '0002_auto_20221103_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleadoafiliado',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
