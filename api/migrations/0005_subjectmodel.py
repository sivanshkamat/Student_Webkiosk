# Generated by Django 4.1.7 on 2023-02-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_customuser_is_phone_no_verified_customuser_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=20)),
                ('score', models.IntegerField()),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]
