# Generated by Django 3.2.8 on 2021-11-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_password',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]
