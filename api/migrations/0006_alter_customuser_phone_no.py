# Generated by Django 4.1.7 on 2023-02-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_subjectmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]