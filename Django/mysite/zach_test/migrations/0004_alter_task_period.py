# Generated by Django 4.2 on 2023-05-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zach_test", "0003_alter_task_task_desc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task", name="period", field=models.FloatField(null=True),
        ),
    ]
