# Generated by Django 3.2.8 on 2021-11-09 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_employee_emp_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.customer')),
            ],
        ),
    ]
