# Generated by Django 4.2 on 2023-05-03 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zach_test", "0004_document_description"),
    ]

    operations = [
        migrations.RemoveField(model_name="document", name="description",),
        migrations.AddField(
            model_name="document",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="set_description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="vector_size",
            field=models.IntegerField(null=True),
        ),
    ]