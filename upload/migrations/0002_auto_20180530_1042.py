# Generated by Django 2.0.5 on 2018-05-30 13:42

from django.db import migrations, models
import upload.validators


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[upload.validators.validate_file_extension]),
        ),
    ]
