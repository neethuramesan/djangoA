# Generated by Django 4.0.5 on 2022-06-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_alter_student_joiningdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='JoiningDate',
            field=models.DateField(blank=True),
        ),
    ]
