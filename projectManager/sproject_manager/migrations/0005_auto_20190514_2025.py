# Generated by Django 2.1.7 on 2019-05-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sproject_manager', '0004_auto_20190514_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('PENDING', 'PENDING'), ('CLOSED', 'CLOSED')], default='ACTIVE', max_length=7),
        ),
    ]
