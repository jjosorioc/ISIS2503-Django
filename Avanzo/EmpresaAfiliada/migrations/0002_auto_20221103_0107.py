# Generated by Django 3.0 on 2022-11-03 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpresaAfiliada', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresaafiliada',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
