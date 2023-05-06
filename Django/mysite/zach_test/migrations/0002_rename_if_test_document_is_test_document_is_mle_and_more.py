# Generated by Django 4.2.1 on 2023-05-06 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zach_test", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="document", old_name="if_test", new_name="is_test",
        ),
        migrations.AddField(
            model_name="document",
            name="is_mle",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="is_train",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
