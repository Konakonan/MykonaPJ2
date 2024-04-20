# Generated by Django 4.2.11 on 2024-04-20 15:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("gyoumuhyo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company_name",
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
                ("name", models.CharField(max_length=30, verbose_name="派遣会社名")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="日付"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Syukkin_yobi",
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
                ("name", models.CharField(max_length=10, verbose_name="曜日")),
            ],
        ),
        migrations.RemoveField(model_name="employee", name="club",),
        migrations.RemoveField(model_name="employee", name="department",),
        migrations.RemoveField(model_name="employee", name="id",),
        migrations.AddField(
            model_name="employee",
            name="employee_id",
            field=models.IntegerField(
                default=12345, primary_key=True, serialize=False, verbose_name="社員ID"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="employee",
            name="gender",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "男"), (2, "女"), (3, "その他")],
                null=True,
                verbose_name="性別",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="first_name",
            field=models.CharField(max_length=20, verbose_name="姓"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="last_name",
            field=models.CharField(max_length=20, verbose_name="名"),
        ),
        migrations.DeleteModel(name="Club",),
        migrations.DeleteModel(name="Department",),
        migrations.AddField(
            model_name="employee",
            name="company_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="gyoumuhyo.company_name",
                verbose_name="派遣会社",
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="syukkin_yobi",
            field=models.ManyToManyField(
                to="gyoumuhyo.syukkin_yobi", verbose_name="出勤曜日"
            ),
        ),
    ]
