# Generated by Django 4.0.5 on 2022-06-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Mobileno',
            field=models.CharField(max_length=255),
        ),
    ]
