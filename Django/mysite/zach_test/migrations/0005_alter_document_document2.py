# Generated by Django 4.2.1 on 2023-05-05 16:18

from django.db import migrations, models
import zach_test.models
import zach_test.validators


class Migration(migrations.Migration):

    dependencies = [
        ("zach_test", "0004_document_document2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="document2",
            field=models.FileField(
                null=True,
                upload_to=zach_test.models.document_upload_path,
                validators=[zach_test.validators.validate_file_extension],
            ),
        ),
    ]