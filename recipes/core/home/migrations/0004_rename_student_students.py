# Generated by Django 5.0.4 on 2024-04-20 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_car_alter_student_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student',
            new_name='Students',
        ),
    ]
