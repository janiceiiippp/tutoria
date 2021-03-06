# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0006_tutor_rate_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotAvailableSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='notavailableslots',
            name='tutor',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='course_taught',
            new_name='courseTaught',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='hourly_rate',
            new_name='hourlyRate',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='private_tutor',
            new_name='privateTutor',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='time_per_slot',
            new_name='timePerSlot',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='tutor',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='introduction',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='university',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='NotAvailableSlots',
        ),
        migrations.AddField(
            model_name='notavailableslot',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutors.Tutor'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='tags',
            field=models.ManyToManyField(to='tutors.Tag'),
        ),
    ]
