# Generated by Django 4.1.1 on 2022-09-29 08:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=500, null=True),
        ),
    ]
