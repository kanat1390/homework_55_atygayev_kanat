# Generated by Django 4.1.1 on 2022-09-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_taskmodel_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('N', 'Новая'), ('C', 'Выполнена')], default='N', max_length=1),
        ),
    ]
