# Generated by Django 4.1.5 on 2023-01-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_vehicles_dt_sold"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicles",
            name="dt_sold",
            field=models.DateField(blank=True, null=True),
        ),
    ]
