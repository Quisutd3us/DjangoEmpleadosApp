# Generated by Django 3.1.1 on 2020-09-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=255)),
                ('phone_num', models.CharField(max_length=35)),
                ('employee_gender', models.CharField(choices=[('m', 'HOMBRE'), ('f', 'FEMENINO')], max_length=1)),
                ('employee_address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('employee_job', models.ManyToManyField(blank=True, to='employees.AvailableJobs')),
            ],
        ),
    ]
