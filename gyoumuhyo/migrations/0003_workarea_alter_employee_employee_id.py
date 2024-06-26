# Generated by Django 4.2.11 on 2024-04-21 21:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("gyoumuhyo", "0002_company_name_syukkin_yobi_remove_employee_club_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkArea",
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
                ("name", models.TextField(max_length=10, verbose_name="作業エリア")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="日付"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="employee",
            name="employee_id",
            field=models.IntegerField(
                max_length=6, primary_key=True, serialize=False, verbose_name="社員ID"
            ),
        ),
    ]
