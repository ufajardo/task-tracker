# Generated by Django 2.2.1 on 2019-05-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sproject_manager', '0007_task_expected_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='expected_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
